import requests
import io
import json
import pandas as pd

GITHUB_BASE_URL = 'https://api.github.com' 
#https://api.github.com/orgs/Netflix/repos

org_name = 'Netflix' 
organization_repositories_url = f"{GITHUB_BASE_URL}/orgs/{org_name}/repos"

r = requests.get(organization_repositories_url).content
rawData = pd.read_json(io.StringIO(r.decode('utf-8')))
clone_urls = rawData.loc[:, 'clone_url',]
new_list = clone_urls.to_list()
print(new_list)
print(len(new_list))