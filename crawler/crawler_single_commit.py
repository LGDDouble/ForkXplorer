# using utf-8
import json

import requests
import csv



def create_auth_header(api_token):
    """create a dictionary for authorization header"""
    return {'Authorization': 'token '+api_token}
def crawler(commit_url):
    api_token = '29b0d680fce2cf8ecf2ced0236d667f897d64f20'
    headers = create_auth_header(api_token)

    "GET /repos/:owner/:repo/commits/:commit_sha"
    try:
        #url = 'https://api.github.com/repos/grafana/loki/commits'
        #print(commit_url)
        result = requests.get(url=commit_url, headers=headers)
        if result.text is not None:
            json_data = json.loads(result.text)
            author = json_data['commit']['author']['name']
            message = json_data['commit']['message']
            sha = json_data['sha']
            date = json_data['commit']['committer']['date']
            parents=json_data['parents'][0]['url']
            return author, message,sha, date,parents


    except Exception as e:
        print(e)

