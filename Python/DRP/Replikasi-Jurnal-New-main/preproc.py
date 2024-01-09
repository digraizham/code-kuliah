from cleantext import clean
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

stemmer = StemmerFactory().create_stemmer()
stopword = StopWordRemoverFactory().create_stop_word_remover()

cleaned = []
with open("txt files/tweets.txt", "r", encoding = "utf-8") as text_file:
    # Casefolding
    read_file = text_file.read().lower()

#Cleaning URL
url_clean = clean(read_file, no_urls=True, replace_with_url='')

#Remove Extra White Spaces (Cleaning)
url_clean = url_clean.replace('\n\n', '\n').replace('\n', '')

#Tokenizing per tweet
splitter = url_clean.split("~~")

for tweet in splitter:
    # Cleaning Hashtags, Mentions, and Punctuations
    tweet = re.sub("@[A-Za-z0-9_]+","", tweet)
    tweet = re.sub("#[A-Za-z0-9_]+","", tweet)
    tweet = re.sub('[^A-Za-z0-9]+', ' ', tweet)
    tweet = re.sub(r'\b[a-zA-Z]\b', ' ', tweet)
    tweet = re.sub(' +', ' ', tweet)
    tweet = tweet.strip()

    # Stopword Removal
    tweet = stopword.remove(tweet)

    # Stemming
    tweet = stemmer.stem(tweet)

    cleaned.insert(0, tweet)
cleaned = cleaned[::-1]
cleaned.remove('')

# Preparing for Labelling
i = 0

with open("txt files/preprocessed tweet.txt", "w", encoding="utf-8") as outfile:
    for tweet in cleaned:
        print(tweet, file=outfile)