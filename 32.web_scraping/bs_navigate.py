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
    <li class="special super-special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

#data = soup.body.contents

# Navigating using tags
print(soup.find(class_="super-special"))
# <li class="special super-special">This list item is also special.</li>
data = soup.find(class_="super-special").parent
print(data)
# <ol>
# <li class="special">This list item is special.</li>
# <li class="special super-special">This list item is also special.</li>
# <li>This list item is not special.</li>
# </ol>

# Navigating using search
print("Navigating using search")
print(soup.find("h3").find_parent("html"))
