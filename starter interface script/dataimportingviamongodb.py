import requests
import json
url = "https://data.mongodb-api.com/app/data-ogpla/endpoint/data/v1/action/findOne"
payload = json.dumps({
    "collection": "logindetails",
    "database": "rapidfigure",
    "dataSource": "rapidsnapshot",
    "filter":{
            "user_id":" sample_user"
        },
    "projection" : {
        "_id":0,
        "user_id":1,
        "passwords":1,
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': " insert API key given in google doc", 
}
response = requests.request("POST", url, headers=headers, data=payload)


print(response.json)
