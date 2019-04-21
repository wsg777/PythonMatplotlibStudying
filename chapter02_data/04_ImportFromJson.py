import requests

url = 'https://github.com/timeline.json'
r = requests.get(url)
json_obj = r.json()
# print(json_obj)
for key, value in json_obj.items():
    print(key, ':', value)
