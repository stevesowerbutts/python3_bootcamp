# Intro to web scraping

Write code that programatically grabs data from a web page.

3 steps
- Download
- Extract data
- Do something with the data

Best practice: Consult the robots.txt file
If making many requests - time them out
Ip can be blocked if too aggressive.

## Beautiful soup

Pip Install bs4 (beautiful soup)

Use beatutiful soup to extract data from html
Install with pip Install bs4 (beautiful soup)
Beautiful soup does not download html
  - Need to use the `requests` module

### Parse and navigate html

BeautifulSoup(html_string, "html.parser") - parse HTML

Once parsed, several ways to navigate:
- by Tag Name
- Using `find` - returns one matching Tag
- Using `find_all` - returns a list of matching tags

To use find/find_all based on html class need to use `class_`

BeautifulSoup parses the html and saves as an instance, which you can now run methods against

Have to import BeautifulSoup from bs4

save the html to a variable for parsing:
`soup = BeautifulSoup(html, "html.parser")`

see bs_basics.py for examples.

#### Navigating with CSS selectors

`select` - returns a list of elements matching CSS selector
- select by id of foo: `#foo`
- select by class of bad: `.bar`
- select children: `div > p`
- select descendents: `div p`
- select attributes: `[foobar]`


### Accessing data in elements

- get_text - gets the inner text from the element (returns nothing for elements with no text)
- name - gets the elements name. eg. `li`,
- attrs - gets all key:value dict of attributes
- can also access attribute values using []
  `soup.find("div")["id"]`

see bs_elements.py for examples

### Navigating with BeautifulSoup

via tags
  - parent / parents
  - contents
  - next_sibling / next_siblings
  - previous_sibling / previous_siblings

via searching
  - find_parent / find_parents
  - find_next_sibling / find_next_siblings
  - find_previous_sibling / find_previous_siblings

# Web scraping project (web_project.py)
Scrape the below site using BeautifulSoup & requests to acheive below:
- url: https://www.rithmschool.com/blog
- Scrape data to csv
- Goal: Grab all links from Rithm school blog
- Data: store URL, anchor tag text, and date

Simplest way to start is to use chrome dev tools to inspect, understand the structure and find the elements you are looking for.
