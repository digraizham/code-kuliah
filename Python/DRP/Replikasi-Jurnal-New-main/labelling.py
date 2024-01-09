train1090 = []
train2080 = []
train3070 = []
train5050 = []

# Label Function for Data Training
def labelling(string, label, arr):
    splitter = string.split('\n')
    for tweet in splitter:
        if tweet == '':
            continue
        arr.insert(0, [tweet, label])

    # arr = arr[::-1]
    return arr

#Labeling with 40 Data Test  
with open("40 Train/positif.txt", "r", encoding='utf-8') as postext1090:
    postweet1090 = postext1090.read()
    labelling(postweet1090, label='pos', arr=train1090)   
with open("40 Train/negatif.txt", "r", encoding='utf-8') as negtext1090:
    negtweet1090 = negtext1090.read()
    labelling(negtweet1090, label='neg', arr=train1090)

#Labeling with 80 Data Test
with open("80 Train/positif.txt", "r", encoding='utf-8') as postext2080:
    postweet2080 = postext2080.read()
    labelling(postweet2080, label='pos', arr=train2080)   
with open("80 Train/negatif.txt", "r", encoding='utf-8') as negtext2080:
    negtweet2080 = negtext2080.read()
    labelling(negtweet2080, label='neg', arr=train2080)

#Labelling with 60 Data Test
with open("60 Train/positif.txt", "r", encoding='utf-8') as postext5050:
    postweet5050 = postext5050.read()
    labelling(postweet5050, label='pos', arr=train5050)   
with open("60 Train/negatif.txt", "r", encoding='utf-8') as negtext5050:
    negtweet5050 = negtext5050.read()
    labelling(negtweet5050, label='neg', arr=train5050)

#Labeling with 120 Data Test
with open("120 Train/positif.txt", "r", encoding='utf-8') as postext3070:
    postweet3070 = postext3070.read()
    labelling(postweet3070, label='pos', arr=train3070)
with open("120 Train/negatif.txt", "r", encoding='utf-8') as negtext3070:
    negtweet3070 = negtext3070.read()
    labelling(negtweet3070, label='neg', arr=train3070)

train1090, train2080, train3070, train5050 = train1090[::-1], train2080[::-1], train3070[::-1], train5050[::-1]

with open("40 Train/traininglist.txt", "w", encoding='utf-8') as outfile1090:
    for label in train1090:
        print(label, file=outfile1090) 
with open("80 Train/traininglist.txt", "w", encoding='utf-8') as outfile2080:
    for label in train2080:
        print(label, file=outfile2080) 
with open("60 Train/traininglist.txt", "w", encoding='utf-8') as outfile5050:
    for label in train5050:
        print(label, file=outfile5050) 
with open("120 Train/traininglist.txt", "w", encoding='utf-8') as outfile3070:
    for label in train3070:
        print(label, file=outfile3070) 