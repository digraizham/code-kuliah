import labelling
from textblob.classifiers import NaiveBayesClassifier

with open("txt files/preprocessed tweet.txt", "r", encoding='utf-8') as read:
    cleanedTweet = read.read()

tweets = cleanedTweet.split('\n')

positif_percentage = 0
negatif_percentage = 0
neutral_percentage = 0
data_test = []

data_train1090 = labelling.train1090
data_train2080 = labelling.train2080
data_train3070 = labelling.train3070

cl1090 = NaiveBayesClassifier(data_train1090)
cl2080 = NaiveBayesClassifier(data_train2080)
cl3070 = NaiveBayesClassifier(data_train3070)

for tweet in tweets:
    prob_dist1090 = cl1090.prob_classify(tweet)
    label = prob_dist1090.max()
    data_test.insert(0, [tweet, label])
    # posPerTweet = round(prob_dist.prob('pos'), 3)
    # negPerTweet = round(prob_dist.prob('neg'), 3)
    # neutPerTweet = round(prob_dist.prob('neut'), 3)
    # positif_percentage += posPerTweet
    # negatif_percentage += negPerTweet
    # neutral_percentage += neutPerTweet
data_test = data_test[::-1]

# Accuracy with 10:90
with open("1090/data train.txt", "w", encoding='utf-8') as outfile10:
    data90 = data_test[40:len(data_test)]
    for data in data90:
        if data == '':
            continue
        print(data, file=outfile10)
    
    print(cl1090.accuracy(data90))

# Accuracy with 20:80
with open("2080/data train.txt", "w", encoding='utf-8') as outfile20:
    data80 = data_test[80:len(data_test)]
    for data in data80:
        if data == '':
            continue
        print(data, file=outfile20)
    
    print(cl2080.accuracy(data80))

# Accuracy with 30:70
with open("3070/data train.txt", "w", encoding='utf-8') as outfile30:
    data70 = data_test[120:len(data_test)]
    for data in data70:
        if data == '':
            continue
        print(data, file=outfile30)

    print(cl3070.accuracy(data70))

    
print("positif prob:", round(positif_percentage/400, 3))
print("negatif prob:", round(negatif_percentage/400, 3))
    