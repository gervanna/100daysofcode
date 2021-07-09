#02_20_21

import bs4
import requests

#1
#Write a Python program to find the title tags from a given html document.
get_page = requests.get("https://www.lipsum.com/")
get_page.raise_for_status()

soup = bs4.BeautifulSoup(get_page.text, "html.parser")
title = soup.find("title").text #why does .text work here

print(f"Title of the page is:\n{title}")

#2 - Retrieve all the paragraph tags from a given html document.
paragraph = soup.find_all("p") #.text doesn't work here
print(f"\nThese are all the paragraph tags:\n{paragraph}")

#3
#Write a Python program to get the number of paragraph tags of a given html document. 

print(f"\nTotal paragraph tags:\n{len(paragraph)}")

#4 - Extract the text in the first paragraph tag of a given html document.

first_p = paragraph[0].text #and here
print(f"\nFirst paragraph:\n{first_p}")

#5 - Find the length of the text of the first <h2> tag of a given html document.

h2_tags = soup.find("h2")
first_h2 = h2_tags.text

print(f"\nLength of 1st h2 tag:\n{len(first_h2)}")

#6 - Find the text of the first <a> tag of a given html text.

a_tags = soup.find("a")
first_a = a_tags.text

print(f"\nFirst <a> tag:\n{first_a}")

#7 - Find the href of the first <a> tag of a given html document.

first_href = a_tags.attrs['href']
print(f"\nFirst <href> tag:\n{first_href}")