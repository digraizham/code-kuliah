with open("120 Train/positif.txt", "r", encoding='utf-8') as readpos:
    positif = readpos.read()

with open("120 Train/negatif.txt", "r", encoding='utf-8') as readneg:
    negatif = readneg.read()

pos_sentiment, neg_sentiment = positif.split('\n'), negatif.split('\n')
positive_tf = {}
negative_tf = {}

stopwords = ['pindah', 'kota', 'ibukota', 'yg']

for tweet in pos_sentiment:
    words = tweet.split(' ')
    for word in words:
        if word not in positive_tf:
            positive_tf[word] = 1
            if word in stopwords:
                positive_tf[word] = 0
        elif word in positive_tf:
            positive_tf[word] += 1
            if word in stopwords:
                positive_tf[word] = 0
    
for tweet in neg_sentiment:
    words = tweet.split(' ')
    for word in words:
        if word not in negative_tf:
            negative_tf[word] = 1
            if word in stopwords:
                negative_tf[word] = 0
        elif word in negative_tf:
            negative_tf[word] += 1
            if word in stopwords:
                negative_tf[word] = 0

with open("tf result.txt", "w", encoding='utf-8') as tf:
    print("Positive Term Freq: ", file=tf)
    print(sorted(positive_tf.items(), key=lambda x:x[1], reverse=True), file=tf)
    print(file=tf)
    print("Negative Term Freq: ", file=tf)
    print(sorted(negative_tf.items(), key=lambda x:x[1], reverse=True), file=tf)
