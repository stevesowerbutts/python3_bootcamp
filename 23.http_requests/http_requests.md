# Http intro

## Request headers
Accept
  - Acceptable content types for response (eg. html, json, xml)
Cache-control
  - Specifying cache control
User-agent
  - Information about the software used to make the request

## Response headers
Access-control-allow-origin
  - specify domains that can make requests
Allowed
  - http verbs that are allowed in the requests

## Response status codes
2XX - Success
3XX - Redirect
4XX - Client Error (your fault)
5XX - Server Error (not your fault)

## HTTP verbs
GET
- Retrieving data
- Data passed in query strngs
- no side effects
- can be cached
- can be bookmarked

POST
- useful for writing data
- data passed in request body
- can have side effects
- not cached
- can not be bookmarked

## APIs
API = Application Programming Interface
Allows you to get data from another application without needing to understand hw the application works

# Writing requests with python

## requests Module
Lets us make HTTP requests from python code
Installed using pip


## Requesting with json
In general we want the response to come back as json:
`requests.get(url, headers={"Accept": "application/json"})`

By itself python reads json as a string, however we can convert it so that python can handle as a dict:
`data = response.json()`

## Query strings
A way to pass data to the server as part of a Get request.
eg. http://www.example.com/?key1=value1,key2=value2

- Can send as a complete url like above, preferred option is with params
```
import requests

response = requests.get(
  "http://www.example.com",
  params={
    "key1":"value1",
    "key2":"value2"
  }
)
```
