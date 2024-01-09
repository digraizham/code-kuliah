import labelling
from textblob.classifiers import NaiveBayesClassifier

with open("txt files/preprocessed tweet.txt", "r", encoding='utf-8') as read:
    cleanedTweet = read.read()
with open("120 Train/positif.txt", "r", encoding='utf-8') as pos:
    positif = pos.read()
    postweet = positif.split('\n')
with open("120 Train/negatif.txt", "r", encoding='utf-8') as neg:
    negatif = neg.read()
    negtweet = negatif.split('\n')

def remove_common(a, b):
    for i in a[:]:
        if i in b:
            a.remove(i)
            b.remove(i) 
    return(b)

tweets = cleanedTweet.split('\n')
sentiment = remove_common(postweet, tweets)
sentiment2 = remove_common(negtweet, sentiment)

counter = 0

data_sentiment = []
pos_counter = 0
neg_counter = 0

pos_percentage = 0
neg_percentage = 0

data_train = labelling.train3070
cl = NaiveBayesClassifier(data_train)

for tweet in sentiment2:
    if tweet == '':
        continue
    prob_dist = cl.prob_classify(tweet)
    label = prob_dist.max()

    posPerTweet = round(prob_dist.prob('pos'), 3)
    negPerTweet = round(prob_dist.prob('neg'), 3)

    if label == 'pos':
        pos_counter += 1
    elif label == 'neg':
        neg_counter += 1
    data_sentiment.insert(0, [tweet, label])
    counter += 1

    pos_percentage += posPerTweet
    neg_percentage += negPerTweet

data_sentiment = data_sentiment[::-1]

with open("For PPT/result.txt", "w", encoding='utf-8') as result:
    for data in data_sentiment:
        if data == ['', label]:
            continue
            
    print("Positif :", pos_counter, '\n' "Negatif :", neg_counter, '\n', file=result)
    print("Persentase Masyarakat bertanggapan positif:", round(pos_percentage/counter, 3)*100, '%', '\n'+"Persentase Masyarakat bertanggapan negatif:", round(neg_percentage/counter, 3)*100, '%', file=result)
        
    