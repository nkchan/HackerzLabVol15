import requests

#URLを変更してください
url = "https://9bqcyrr7bb.execute-api.ap-northeast-1.amazonaws.com/dev/Q15"
s = requests.session()
# POSTするデータを変更してください
params = {"id": "aaa","passwd": "bbbbb"}
r =  s.post(url, data=params)
print (r.text.encode("utf-8"))
