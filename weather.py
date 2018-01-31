from rapidconnect import RapidConnect
import json
from urllib.request import urlopen

def get_weather(city):
	rapid = RapidConnect("default-application_5a68be4ce4b09c6b06da6c08", "551285ee-2f7d-45e2-8471-bc4aaae024ed")
	result = rapid.call('YahooWeatherAPI', 'getWeatherForecast', { 
	'location': city	,
	'filter': ['item.condition,item.forecast'] 
	})
	return result

def getCity(lat,lon):
   url = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyBdWsMTk1r9z49-_Nh0XIq4kisJ2T49gsY&"
   url += "latlng=%s,%s&sensor=false" % (lat,lon)
   v = urlopen(url).read()
   v = json.loads(v.decode('utf-8'))
 
   for i in range(0,len(v["results"][0]['address_components'])):
       if "locality" in v["results"][0]['address_components'][i]['types'] :
           
           return v["results"][0]['address_components'][i]["long_name"]


