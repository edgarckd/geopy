import requests as rq
import json as js


parametros = { "key" : "Lyrv1vpGKjuNERqHw0oYFer94QqSc0nn" , "location" : "calle 36 #26-64 la arboledad soledad"}
response = rq.get("http://www.mapquestapi.com/geocoding/v1/address", params=parametros)
data = js.loads(response.text)["results"]
lat = data[0]['locations'][0]['latLng']['lat']
lng = data[0]['locations'][0]['latLng']['lng']

print(lat)
print(lng)