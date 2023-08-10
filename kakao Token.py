import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '69b1c13ece9c8ead7776149823062dc2'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'JR9UZc8zaV6v-dnvWF8TRpVb26qux0fnCf2-e9m_AjJDEaJUlXpqU7aGD7LHUj0Ku3xKVwo9cuoAAAGJ3PtXgw'
#authorize_code = 'CPMvKQMvVuihgy2nEGXhip6Ksp0PEl74EniyOy6SqWDAMD1zSQTzAc7Bk8QHUYn4UzkVrAo9dBEAAAGJ3PhDoQ'
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
with open(r"C:\Users\poongsan\Desktop\kakao_code_nuri.json","w") as fp:
    json.dump(tokens, fp)