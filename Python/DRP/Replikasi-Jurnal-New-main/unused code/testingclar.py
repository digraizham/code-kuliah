from textblob.classifiers import NaiveBayesClassifier

train = []

with open("txt files/dummy.txt", "r", encoding='utf-8') as postext:
    postweet = postext.read()

with open("txt files/dummy n.txt", "r", encoding='utf-8') as negtext:
    negtweet = negtext.read()

tokenpos = postweet.split('\n')
for tweet in tokenpos:
    train.insert(0, [tweet, 'pos'])

tokenneg = negtweet.split('\n')
for tweet in tokenneg:
    train.insert(0, [tweet, 'neg'])
train = train[::-1]

cl = NaiveBayesClassifier(train)

string = "positif harusnya"
print(cl.classify(string))