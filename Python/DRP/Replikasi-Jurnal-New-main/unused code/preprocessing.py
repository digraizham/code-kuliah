import re
from cleantext import clean
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

with open("txt files/tweets.txt", "r", encoding = "utf-8") as text_file:
    # Casefolding
    read_file = text_file.read().casefold().replace('\n\n', '\n').replace('\n', '')

#Cleaning URL
url_clean = clean(read_file, no_urls=True, replace_with_url='')

arr = []
stemmed_word = []
stemperword = []
ps = PorterStemmer()

# Tokenizing ()
splitter = url_clean.split("~~")
i = 0
for tweet in splitter:
    stemperword = []
    #Cleaning Punctuation
    tweet = re.sub('[^A-Za-z0-9]+', ' ', tweet)
    tweet = re.sub(r'\b[a-zA-Z]\b', ' ', tweet)
    tweet = re.sub(' +', ' ', tweet)

    #Stemming
    # tweet = tweet.strip()
    token_tweet = word_tokenize(tweet)
    for word in token_tweet:
        stem_tweet = word
        stemperword.append(stem_tweet)
    arr.insert(1, stemperword)
# print(stemmed_word)
# # print(arr)

with open("txt files/preprocessedsaddw.txt", "w", encoding="utf-8") as outfile:

    for word in arr:
        # #cleaning url
        # filtered = fnmatch.filter(word, '*https*')
        # if filtered == []:
        #     filtered = "uvuvuvuvuevww onyeteacjkcasb"
        # matchfilter = ''.join(filtered)
        back2string = ' '.join(word)

        # cleaned_url = back2string.replace(matchfilter, '')

        #cleaning emoji
        final_clean = clean(back2string, no_emoji=True)
        print(final_clean, "~~", file=outfile)
