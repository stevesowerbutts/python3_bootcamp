# Create a web crawler with scrapy

https://docs.scrapy.org/en/latest/

Framework for extracting data
- bundles making the http request with the extraction of the data, and writing the data to a file

Have to follow the rules of the Framework
- works similar to BeautifulSoup but with its own syntax
- Uses selectors: https://docs.scrapy.org/en/latest/topics/selectors.html
- extract() and extract_first have now been replaced by getall() and get():
  - `SelectorList.get()` is the same as `SelectorList.extract_first()`
    - output will be a single item
  - `SelectorList.getall()` is the same as `SelectorList.extract()`
    - output will be a list



Need to install the scrapy module - `python3 -m pip install scrapy`

See book_scrapy.py for example of how to write the scaper.

Then to run the scraper, need to use the scrapy `runspider` command:
```
scrapy runspider book_scrapy.py -o books.csv
```

- Uses append mode by default
- Can change the output to any other file type just by changing the extension.
```
scrapy runspider book_scrapy.py -o books.json
```
