import pandas, requests
from geopy.geocoders import Nominatim

#nom = Nominatim(scheme="http")
nom=Nominatim(scheme="http", user_agent="test-application")
#nom = Nominatim(timeout=3, scheme='http')

print(nom.geocode("2 townsend st san francisco").latitude)