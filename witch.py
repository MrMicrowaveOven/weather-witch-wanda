import env_vars

import time
from time import sleep
import requests
import json

YELLOW = 16500
GREEN = 25500
BLUE = 46920

def get_prob_of_rain():
    r = requests.get(env_vars.weather_url)
    content = json.loads(r.content)

    daily = content['daily']

    return daily['data'][0]['precipProbability']

def continuously_look_for_rain():
    while True:
        prob = get_prob_of_rain()
        color_int = 30420 * prob + YELLOW
        # change_color_of_lightbulb
        sleep(600)


print continuously_look_for_rain()
