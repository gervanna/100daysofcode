#Write a Python program to access and print a URL's content to the console.

#02_16_21

import requests

def view_webpage(txt):

    contents = requests.get(txt)
    contents_text = contents.text
    print(contents_text)
    return contents_text

view_webpage('https://w3schools.com/python/demopage.htm')

#can also import and use httpconnection or urllib (haven't figured out the urllib yet.)