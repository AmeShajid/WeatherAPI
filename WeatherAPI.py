#this is a weather api

#import and pip install requests
import requests

#first go to the weather website and then copy and paste your API key
API_KEY = "91750d4ec8c0d386b574c2129e41ee15"

#this is where we sending and request the data
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#this is where we send the query parameters basically what kind of data we want
#we will ask for the city first
city = input("Enter city name: ")
#basicaly we have the base url which is the weather then the query parameters(anythign after the questionmark) so we are passing along our api key and the the q which means query we are asking for data associted with city which is the input user types
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
#now this is where we are getting the data by sending a get requests
response = requests.get(requests_url)

#now checking the status code of the response so if its 200 that means its successful
if response.status_code == 200:
    #here we are getting the data in json format
    data = response.json()
    #now we are getting the data we want from the json data so we are getting weather
    weather = data['weather'][0]['description']
    #here we are getting the temperature and converting it to celcius
    temperature = round(data['main']['temp'] - 273.15)
    print("Weather is: ", weather)
    print("Temperature is: ", temperature, "Celcius")
else:#if its longer than 200 than basically an error has occuered
    print("Error has occured")




























