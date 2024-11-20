import os
import json


PATH = os.path.dirname(os.path.realpath(__file__))
COOKIES_FILE = os.path.join(PATH, "cookies.json")


print(type(json.load(open(COOKIES_FILE))))