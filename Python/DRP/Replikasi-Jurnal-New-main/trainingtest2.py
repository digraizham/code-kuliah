import labelling
from textblob.classifiers import NaiveBayesClassifier

def remove_common(a, b):
    for i in a[:]:
        if i in b:
            a.remove(i)
            b.remove(i) 
    return(b)

data_train = labelling.train5050
data_testing = labelling.train3070    
cl = NaiveBayesClassifier(data_train)   

data_test = remove_common(data_train, data_testing)

with open("For PPT/accuracy2.txt", "w", encoding='utf-8') as accuracy:
    print("Accuracy for 60 Data Train and 60 Data Test :", file=accuracy)
    print(cl.accuracy(data_test), file=accuracy)