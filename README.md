# Weather App
This is a weather app built with Python's Tkinter library that allows you to get the current weather conditions and time zone information for a specific city. The app uses the `OpenWeatherMap API` to retrieve the data and display it on the GUI.

## Getting started
To run the app, you need to have Python and Tkinter installed. You can download the latest version of Python from the official website: https://www.python.org/downloads/

You also need an `API key` from OpenWeatherMap in order to access their data. You can sign up for a free API key on their website: https://openweathermap.org/api

Once you have your `API key`, create a new file named api_key.py in the project directory and add the following line of code, replacing YOUR_API_KEY with your actual key:


api_key = 'YOUR_API_KEY'
To run the app, open a terminal window and navigate to the project directory. Then run the following command:

`python main.py`

The app should open in a new window. To get the weather information for a specific city, enter the city name in the search bar and click the search icon.

## Libraries used
```
Tkinter: for creating the GUI
geopy: for geocoding the city name
timezonefinder: for getting the time zone information
datetime: for formatting the time
requests: for making API calls
pytz: for converting time zones
```
## Authors
https://www.youtube.com/watch?v=NCCYWIzN6hU

