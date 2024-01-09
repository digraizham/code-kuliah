import json

data = []
tweet = []
with open("txt files/tweets.jsonl", 'r') as f:
    for line in f:
       data.append(json.loads(line))

with open("txt files/tweets.txt", "w", encoding="utf-8") as outfile:
    for i in range(0, 400, 1):
        tweet.append(data[i]["content"])
        print(tweet[i], "~~", file = outfile)