import labelling
from textblob.classifiers import NaiveBayesClassifier

with open("txt files/preprocessed tweet.txt", "r", encoding='utf-8') as read:
    cleanedTweet = read.read()

tweets = cleanedTweet.split('\n')

counter = 1
accuracy = 0
data_test = []

data_train = labelling.train1090
cl = NaiveBayesClassifier(data_train)

for tweet in tweets:
    prob_dist = cl.prob_classify(tweet)
    label = prob_dist.max()
    data_test.insert(0, [tweet, label])
    if tweet in data_train:
        continue
    posPerTweet = round(prob_dist.prob('pos'), 3)
    accuracy += posPerTweet
    counter += 1

data_test = data_test[::-1]

# Accuracy with 10:90
with open("1090/data train.txt", "w", encoding='utf-8') as outfile10:
    for data in data_test:
        if data == ['', label]:
            continue
        print(data, file=outfile10)
        
print(counter)

with open("1090/result.txt", "w", encoding='utf-8') as result:
    print("Accuracy ", round(accuracy/counter, 3), file=result)
        