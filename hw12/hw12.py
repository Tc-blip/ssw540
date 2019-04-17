import urllib.request
import json
import requests
from math import radians, cos, sin, asin, sqrt

def geocoderesult(address,benchmark='Public_AR_Current',vintage='ACS2018_Current'):
	url1='http://geocoding.geo.census.gov/geocoder/geographies/address'
	param1={'street':address['street'],'city':address['city'],'state':address['state'],'benchmark':benchmark,'vintage':vintage,'format':'json'}
	data=requests.get(url1,params=param1).text
	data=json.loads(data)
	try:
		x=data['result']['addressMatches'][0]["coordinates"]['x']
		y=data['result']['addressMatches'][0]['coordinates']['y']
	except:
		x='nan'
		y='nan'
	return x,y


def cal_distance(loc1, loc_w):
    lat1,lon1 = loc1
    lat2,lon2 =loc_w
    
    lon1 = lon1 * (3.14 / 180)
    lon2 = lon2 * (3.14 / 180)
    lat1 = lat1 * (3.14 / 180)
    lat2 = lat2 * (3.14 / 180)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(min(1, sqrt(a)))
    kms = 6367 * c
    miles = (kms * 5) / 8
    return miles

if __name__ == "__main__":
    street = input("street: ")
    city = input("City name (optional): ")
    state = input("State (optional): ")
 
    input_address={}
    white_house ={'street':"1600 Pennsylvania Avenue",'city':'Washington','state':'DC'}
    input_address['street'] = street
    input_address['city'] = city
    input_address['state'] = state
    white_house_loc = geocoderesult(white_house)
    user_loc = geocoderesult(input_address)
    dis = round(cal_distance(user_loc,white_house_loc))
    print(f"The distance between my home and the White house is about {dis} miles. ")