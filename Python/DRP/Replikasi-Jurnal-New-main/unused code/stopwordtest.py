from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

with open("labelling/positif.txt", "r", encoding='utf-8') as postext:
    postweet = postext.read()

splitter = postweet.split('\n')

factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

with open("testing txt/stopword test.txt", "w", encoding='utf-8') as outfile:
    for tweet in splitter:
        newtweet = stopword.remove(tweet) 
        print(newtweet, file=outfile)
