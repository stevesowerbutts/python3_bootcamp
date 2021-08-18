from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Basic to get the first entry
print(soup.body.div)

# Using `find`
print(soup.find("div"))
print("Select by id")
print(soup.find(id="first"))

# Find_all
l = soup.find_all("div")
print(l)
print("find all class")
c = soup.find_all(class_="special")
print(c)
print("select by attributes")
a = soup.find_all(attrs={"data-example": "yes"})
print(a)

# select
print("Using select")
# Select id
print(soup.select("#first"))
# Select first instance of class
print(soup.select(".special")[0])
# Select from attributes uses []
d = soup.select("[data-example]")
print(d)
