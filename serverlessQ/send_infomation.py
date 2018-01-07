import requests

url = "https://9bqcyrr7bb.execute-api.ap-northeast-1.amazonaws.com/dev/Q15"
s = requests.session()
params = {"id": "A","passwd": "123456"}
r =  s.post(url, data=params)
print (r.text.encode("utf-8"))
