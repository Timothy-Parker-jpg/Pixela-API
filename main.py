import requests
import os
import datetime as dt


#Credentials
USERNAME = os.environ["Pixela_Username"]
TOKEN = os.environ["Pixela_API_KEY"]

#data globals
QUANTITY = "5"
DATE = dt.datetime.now().strftime("%Y%m%d")

#create user params
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#create graph params
graph_config = {
    "id": "coding-graph",
    "name": "Coding Habit",
    "unit": "commit",
    "type": "int",
    "color": "momiji",
}

#FORMAT FOR SENDING TOKEN IN HEADER
headers = {
    "X-USER-TOKEN": TOKEN
}

#POSTING PIXELS TO GRAPH
post_pixel = {
    "date": DATE,
    "quantity": QUANTITY
}
update_pixel = {
    "quantity":QUANTITY
}
update_graph = {
    "name": "Code"
}
#endpoints
create_user_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_config['id']}"
pixel_endpoint = f"{graph_endpoint}/{DATE}"
#MAKE REQUEST
#r = requests.post(url=graph_endpoint, json=post_pixel, headers=headers)
#r = requests.put(url=pixel_endpoint, headers=headers, json=update_pixel)

r = requests.put(url=graph_endpoint, headers=headers, json=update_graph)
print(r.text)

