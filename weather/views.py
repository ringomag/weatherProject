from django.shortcuts import render
import json
import urllib.request


# Create your views here.

def index(request):
    
    if request.method == 'POST':
        
        city = request.POST['city']
        
        req = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=1237fc1eecd4c45616daae1c9d2c542c').read()
        json_data = json.loads(req)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": "lon: " + str(json_data['coord']['lon'])+ ' lat: ' + str(json_data['coord']['lat']),
            "temperature": str(round(json_data['main']['temp'] -273.15)) + "C",
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "city": city,
        }

    else:
        data = {}
    return render(request, 'index.html', data)