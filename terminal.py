import requests

url = 'http://apis.data.go.kr/B551220/vsslBerthStatService/getVsslBerthStatList'
params ={'serviceKey' : "y38q3Jj1muTXiWPPh2TIe+lzo5aKNYUxgIYzaOpavo8n3YH/4X3Y2i7z6VF/OHdiartQgOF1Yex79p/f8w1WRA==", 'pageNo' : '1', 'numOfRows' : '2', 'startDate' : '20230701', 'endDate' : '20230707', 'trminlCode' : 'BNCT', 'dataType' : 'XML' }

response = requests.get(url, params=params)
print(response.content)