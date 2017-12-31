import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
import ast
import sys

if len(sys.argv) != 2:
    print("Not enough input arguments")
    sys.exit(1)

url_price_history = 'https://www.heureka.cz/direct/vyvoj-cen/?id='

# read json using pandas
all_urls = pd.read_json(sys.argv[1], lines=True)

# filter which urls should be selected
urls_to_process = all_urls[all_urls.url.str.contains(r'samsung-galaxy-s[5,6,7,8]')].url


# list of concrete urls can be provided too
# urls_to_process = [
#     'https://mobilni-telefony.heureka.cz/samsung-galaxy-s7-g930f-32gb/',
#     'https://mobilni-telefony.heureka.cz/samsung-galaxy-s6-edge-plus-g928f-32gb/'
# ]


# returns dictionary with product data : name, id, category, brand
def get_product_data(url):
    # get url result as a text
    r_text = requests.get(url).text

    # get dataLayer variable. Result is list -> extract first element
    data_string = re.findall(r'dataLayer = \[(\{.*\})\];', r_text)[0]

    # convert string JSON to dictionary
    data = ast.literal_eval(data_string)

    # some products do not have product_brand value
    if 'product_brand' not in data:
        data['product_brand'] = 'unknown'

    return data


# returns historical data of min/average price, dates, product age
def get_historical_data(product_id):
    # get text from heureka/direct/vyvoj-cen/id=
    r_text = requests.get(url_price_history + product_id).text

    # find prices and datetimes
    min_prices = re.findall(r'values=(.*)&', r_text)[0].split(',')
    av_prices = re.findall(r'values_2=(.*)&', r_text)[0].split(',')
    dates = re.findall(r'x_labels=(.*)&', r_text)[0].split(',')

    # create pandas DataFrame from dictionary
    df = pd.DataFrame({'min_price': list(map(int, min_prices)), 'av_price': list(map(int, av_prices)), 'date': dates})

    # convert date to pandas datetime format
    df['date'] = pd.to_datetime(df.date, format='%d.%m.%Y')

    # compute how old product is
    df['age'] = (pd.Timestamp.today() - df['date']).dt.days

    return df


# --- ITERATE THROUGH ALL URLS AND PLOT RESULTS ---

# variables to show how many urls processed
i = 1
num_urls = len(urls_to_process)

for url in urls_to_process:
    # get product information as dictionary
    product_data = get_product_data(url)

    # get historical data as pandas DataFrame - min/average prices, dates, age
    historical_data = get_historical_data(product_data['product_id'])

    # -- PLOT PRICES ---

    # convert phone age and prices to numpy array so these values can be plotted
    product_age = historical_data.age.as_matrix()
    av_prices = historical_data.av_price.as_matrix()

    # plot results
    plt.plot(product_age, av_prices, label=product_data['product_name'])

    # uncomment to show datetimes on x axis
    #     plt.xticks(product_age, historical_data.date.dt.date, rotation=45)

    # print how many urls processed
    sys.stdout.write('\r' + 'Processed ' + str(i) + ' of ' + str(num_urls))
    i += 1

# style and show plot
plt.gca().invert_xaxis()
plt.legend()
plt.xlabel('Product age [days]')
plt.ylabel('Price')
plt.grid()
plt.show()
