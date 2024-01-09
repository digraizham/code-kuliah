import json

data = []
with open("twitter.jsonl", 'r', encoding='utf-8') as f:
    for line in f:
       data.append(json.loads(line))

with open("datacrawl.txt", "w", encoding="utf-8") as data_write:  
    for cont in range(0, 1000):
        print(data[cont]["content"], file = data_write, end = '\n')
        print(file = data_write)