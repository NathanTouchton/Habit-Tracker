from os import environ
from datetime import datetime
from requests import post

TODAY = datetime.now()

USERNAME = environ["PIXELA_USER"]
TOKEN = environ["PIXELA_TOKEN"]

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
STAT_ENDPOINT = f"{GRAPH_ENDPOINT}/graph1"

# GRAPH_PARAMS = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "Minutes",
#     "type": "int",
#     "color": "ajisai",
#     "timezone": "America/Chicago",
# }

HEADERS = {
    "X-USER-TOKEN": TOKEN,
}

PIXELA_STAT_PARAMS = {
    "date": TODAY.strftime("%Y%m%d"),
    "quantity": "200",
}

RESPONSE = post(url=STAT_ENDPOINT, json=PIXELA_STAT_PARAMS, headers=HEADERS)
print(RESPONSE.text)
