import json

data = []
with open("crawl.jsonl", 'r') as f:
    for line in f:
       data.append(json.loads(line))

with open("crawl.txt", "w", encoding="utf-8") as outfile:
    for i in range(0, 20, 1):
        tweet = data[i]["content"]
        print(f"{i+1}. {tweet}\n", file = outfile)