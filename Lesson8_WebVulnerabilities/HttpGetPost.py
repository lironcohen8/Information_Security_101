# Use the requests module to:
#
# In get, send a GET request to http://httpbin.org/status/204 and return the status code
# In post, send a POST request to http://httpbin.org/post with the data  x=1  and  y=2  and return the response

import requests
import json


def get():
    response = requests.get("http://httpbin.org/status/204")
    return response.status_code


def post():
    request_body = json.loads('{"x": "1", "y": "2"}')
    response = requests.post("http://httpbin.org/post", request_body)
    return response
