import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '5c86b993d2e4246020b4d50bdb8641e3'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'pAh4_kl_-nwrN6UCPONl7pZDz8Zo4gIWMYi8cquRDpGQcxOPgLTfom76DLQienDudUNbYAo9dZwAAAGCtH1kPQ'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data, verify=False)
tokens = response.json()
print(tokens)

# json 저장
import json

with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)

with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# kapi.kakao.com/v2/api/talk/memo/default/send

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

data={
    "template_object": json.dumps({
        "object_type":"text",
        "text":"Hello, world!",
        "link":{
            "web_url":"www.naver.com"
        }
    })
}
response = requests.post(url, headers=headers, data=data,verify=False)
response.status_code