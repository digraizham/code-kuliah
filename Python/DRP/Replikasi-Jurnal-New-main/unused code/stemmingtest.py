from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

with open("testing txt/stopword test.txt", "r", encoding='utf-8') as postext:
    postweet = postext.read()
    
splitter = postweet.split('\n')

factory = StemmerFactory()
stemmer = factory.create_stemmer()

with open("testing txt/stemming test.txt", "w", encoding='utf-8') as outfile:
    for tweet in splitter:
        newtweet = stemmer.stem(tweet) 
        print(newtweet, file=outfile)

