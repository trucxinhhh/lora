
import urllib.request
import urllib.parse
from time import sleep 
from random import randint

def make_param_thingspeak(fields):
    params = urllib.parse.urlencode(fields).encode()
    return params

def thingspeak_post(params):
    api_key_write = "KKB6HW3VK8PNIRRQ"
    url = "https://api.thingspeak.com/update"

    method = "POST"
    req = urllib.request.Request(url, data=params, method=method)
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("X-THINGSPEAKAPIKEY", api_key_write)

    response = urllib.request.urlopen(req)
    response_data = response.read().decode("utf-8")
    
    return response_data


while True:

    CT1_Status = randint(0, 1)
    CT2_Status = randint(0, 1)
    CT3_Status = randint(0, 1)
    Lamp_Status = randint(0, 1)
    Warning_lights_Status = randint(0, 1)
    Temperature = randint(0, 100)
    Humidity = randint(0, 100)

    data = {
        'field1': CT1_Status,
        'field2': CT2_Status,
        'field3': CT3_Status,
        'field4': Lamp_Status,
        'field5': Warning_lights_Status,
        'field6': Temperature,
        'field7': Humidity
    }

    print(data)
    params_thingspeak = make_param_thingspeak(data)
    thingspeak_post(params_thingspeak)

    sleep(20)
