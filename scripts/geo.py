import requests
import json

send_url = "http://api.ipstack.com/check?access_key=d12f72d834c71d8c72ca5face5f22bac&security=1"
#secure key
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)

latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']
country = geo_json['country_name']



print("I've always wanted to go to " + city + ", " + country)



