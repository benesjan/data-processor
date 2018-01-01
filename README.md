# data-processor's README

To remove url duplicates run:
```
python url_deduplicator.py /path/to/input/file /path/to/output/file
```

To visualize the price of selected products run:
```
python price_visualization.py /path/to/input/file
```

To select urls from sections run:
```
python url_selector.py /path/to/file/with/section/urls /path/to/input/file /path/to/output/file
```

To get remaining urls run:
```
python get_remaining_urls.py /path/to/file/with/product/data /path/to/file/with/urls /path/to/output/file
```