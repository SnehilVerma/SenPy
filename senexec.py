import pickle
classifier=pickle.load(open('nbclassifier.p','rb'))
word_features=pickle.load(open('features.p','rb'))


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features







review=raw_input("Enter a sentence!\n")

#print(extract_features(review.split()))
features=extract_features(review.split())

print classifier.classify(features)
