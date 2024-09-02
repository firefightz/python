import requests
import io
import json
import pandas as pd

r = requests.get("https://opentdb.com/api.php?amount=10")
print(help(r))
print(r.url)
# variable = json.dumps(r.json(), indent=2)
# print(variable)
# print(json.dumps(json_stuff, indent=2))
# rawData = pd.read_json(io.StringIO(r.decode('utf-8')))
# clone_urls = rawData.loc[:, 'clone_url',]
# new_list = clone_urls.to_list()
# print(new_list)
# print(len(new_list))