#8 - Extract all the URLs from the webpage python.org that are nested within <li> tags.

import bs4
import requests
from pprint import pprint

py_page = requests.get("https://www.python.org/")
py_page.raise_for_status()

soup = bs4.BeautifulSoup(py_page.text, "html.parser")
url = soup.find_all("li")

urls = []

for x in url:
    a = x.find("a")
    urls.append(a.attrs["href"])
pprint(urls)

#9 - Find all the h2 tags and list the first four from the webpage python.org

h2_tags = soup.find_all("h2")
print("\nFirst 4 h2 tags:\n")
pprint(h2_tags[0:4])

#10 - Find all the link tags and list the first ten from the webpage python.org.

link_tags = soup.find_all("link")
print("\nFirst 10 link tags:\n")
pprint(link_tags[0:10])