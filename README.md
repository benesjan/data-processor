# data-processor's README

To remove url duplicates run:
```
python url_deduplicator.py /path/to/input/file /path/to/output/file
```

To visualize the price of selected products run:
```
python price_visualization.py /path/to/input/file
```

To select urls by sections run:
```
python url_selector.py /path/to/file/with/section/urls /path/to/input/file /path/to/output/file
```

To get remaining urls (those that were not crawled yet according to products_data.jl) run:
```
python get_remaining_urls.py /path/to/file/with/product/data /path/to/file/with/urls /path/to/output/file
```