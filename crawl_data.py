import time
import requests
import json

file_name = 'db.json'
url = "https://www.ebi.ac.uk/ols/api/search?q=*&groupField=iri&start={}&ontology=envo"
count = 1
dict_data = {}
start = 0
end = 6400

for i in range(start, end, 10):
    res = requests.get(url.format(i))
    response_json = json.loads(res.text)
    response = response_json["response"]
    docs = response["docs"]
    for row in docs:
        dict_data.update({count: {"keyword": row["label"], "link": row["iri"]}})
        count += 1
    time.sleep(2)

with open(file_name, "w") as file:
    json.dump(dict_data, file, indent=4)
