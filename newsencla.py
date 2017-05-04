import csv
import nltk
import pickle


fp = csv.reader(open("posneg.csv", 'rb'))
senrev = []
for words,sentiment in fp:
	words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
	senrev.append((words_filtered, sentiment))
#split the reviews and store them in senrev list.
#words in a sentence are stored as separate entities.
#the sentiment is appended in the end


test_rev= [
    (['feel', 'happy', 'this', 'morning'], 'pos'),
    (['larry', 'friend'], 'pos'),
    (['not', 'like', 'that', 'man'], 'neg'),
    (['house', 'not', 'great'], 'neg'),
    (['your', 'song', 'annoying'], 'neg')]
    	
    	



def get_words_in_senrev(senrev):
    all_words = []
    for (words, sentiment) in senrev:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    print(wordlist)
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_senrev(senrev))
#print(word_features)


pickle.dump(word_features,open('features.p','wb'))


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features



training_set = nltk.classify.apply_features(extract_features, senrev)
#print(training_set)

#BUTTON TO TRAIN THE MODEL.
classifier = nltk.NaiveBayesClassifier.train(training_set)
#print(nltk.classify.util.accuracy(classifier, test_rev))


pickle.dump(classifier,open('nbclassifier.p','wb'))






