import json
with open('data_light.json','r',encoding='utf-8') as f:
  data = json.load(f)
print(data)