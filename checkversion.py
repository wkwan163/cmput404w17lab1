#!/usr/bin/env python

import requests

print requests.__version__

response = requests.get("https://raw.githubusercontent.com/wkwan163/cmput404w17lab1/master/checkversion.py")

print response.status_code

print response.text
