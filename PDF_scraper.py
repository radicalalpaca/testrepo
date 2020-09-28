import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

input_url = "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
response = requests.get(input_url)
soup = BeautifulSoup(response.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]

periods = [pt.get_text() for pt in seven_day.select(".tombstone-container .period-name")]
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]

print(temps)