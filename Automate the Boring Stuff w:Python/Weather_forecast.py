import requests
import bs4 #beautiful soup is imported as bs4

def get_weather_forecast(url):
    '''Gets current weather forecast'''
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#main_content > div.wx-content > div > div:nth-child(1) > h1 > span')
    
    return elems[0].text.strip()

current_forecast = get_weather_forecast('https://www.theweathernetwork.com/ca/hourly-weather-forecast/alberta/bonnyville?wx_auto_reload=')
print("The current forecast is " + current_forecast)

#doesn't work