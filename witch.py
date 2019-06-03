import env_vars

import time
from time import sleep
import requests
import json

YELLOW = 8000
# GREEN = 25500
BLUE = 42000

def get_prob_of_rain():
    r = requests.get(env_vars.weather_url)
    content = json.loads(r.content)

    daily = content['daily']

    return daily['data'][0]['precipProbability']

def continuously_look_for_rain():
    while True:
        prob = get_prob_of_rain()
        print prob
        color_int = int(32000 * prob + YELLOW)
        change_color_of_lightbulb(color_int)
        sleep(6)

def change_color_of_lightbulb(color_int):
    print "turning " + str(color_int)
    r = requests.put(env_vars.HUE_PUT_LINK, json.dumps({"on":True, "sat":254, "bri":254,"hue":color_int}))
    print r
    print r.content
continuously_look_for_rain()
