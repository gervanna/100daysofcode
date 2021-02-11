import requests
import bs4

def get_price(url):
    '''Gets prices'''
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#product-content > div.product-price > span > span')

    return elems[0].text.strip()

price = get_price('https://www.warehouseone.com/mens-hedge-waffle-henley-hoodie/1421700443.html?dwvar_1421700443_colour=001')
print(f"The price is ", {price})

#doesn't work