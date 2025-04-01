# APIs
# pypi.org/project/requests
# JSON

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2)

# docs.python.org/3/library/json.html
# json library
#115234 (track name as key for Weezer) "Say It Ain't So"

o = response.json()
for res in o["results"]:
    print(result["trackName"])