import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
import nltk
import csv
import sys
import pickle
from collections import Counter
from nltk.corpus import stopwords


#aspect term categories
categories=['service','internet','food','location']



class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(addr=("127.0.0.1", 8080)))
    
    def parse(self, text):
        return json.loads(self.server.parse(text))

nlp = StanfordNLP()


fp=csv.reader(open("posneg.csv",'rb'))
parsedtext=[]
j=0
i=0
aspects=[]

#lexicon words positive and negative
#used to assign polarity to all the words.
with open('posw.csv','rb') as f:
	reader=csv.reader(f)
	poslist=list(reader)

with open('negw.csv','rb') as f:
	reader=csv.reader(f)
	neglist=list(reader)

'''
poslist=[]
neglist=[]
f1=csv.reader(open("posw.csv",'rb'))
for item in f1:
	poslist.append(item)



f2=csv.reader(open("negw.csv",'rb'))
for item in f2:
	neglist.append(item)
'''



def extract_jjterm(sentence):
	print 'hello'


def polarity_from_aspects(word):
	
	'''
	for item in poslist:
		if item==word:
			return 'positive'
	for item in neglist:
		if item==word:
			return 'negative'
	'''

	
	if word in poslist:
		return 'positive'
	elif word in neglist:
		return 'negative'
	else:
		return 'neutral'
	




def aspects_from_tagged_sents(tagged_sentences):
	"""
	INPUT: list of lists of strings
	OUTPUT: list of aspects
	Given a list of tokenized and pos_tagged sentences from reviews
	about a given restaurant, return the most common aspects
	"""

	STOPWORDS = set(stopwords.words('english'))

	# find the most common nouns in the sentences
	noun_counter = Counter()

	
	#jjterm=['good','bad','ok']
	for sent in tagged_sentences:
		for i in range(len(sent)): 
			word=sent[0]
			pos=sent[1]

			if pos=='NNP' or pos=='NN' or pos=='NNPS' or pos=='NNS' and word not in STOPWORDS:
				#extract polarity of the word using seed lexicon of pos and neg words.
				#send the jj_term corresponding to the noun.
				#jjterm=extract_jjterm(sent)
				#print jjterm
				#pol=polarity_from_aspects([jjterm])
				#print pol

				noun_counter[word] += 1

			i+=1

	# list of tuples of form (noun, count)
	return [noun for noun, _ in noun_counter.most_common(10)]




for words,sentiment in fp:

	#parsedtext.append(nlp.parse(words))
	tok=nltk.tokenize.word_tokenize('John loves Mary but he dislikes Juliet')

	#print(tok)
	pos=nltk.pos_tag(tok)
	print pos
	pickle.dump(pos,open('token_dump.p','wb'))
	#print "\n"
	
	k=0
	result=[]
	result=aspects_from_tagged_sents(pos)
	

	for item in result:
		item=item.lower()
		if item not in aspects:
			aspects.append(item)

	#print(result)
	
	'''
	for item in pos:
		#result=aspects_from_tagged_sents(item)
		print(item)
		#print(result)
		print("\n")'''

	j=j+1
	if j==1:
		break
	#limit can be increased upto the desired value.
	#parsedsen.append(i,sentiment)
print aspects
#print aspects	











'''for item in parsedtext:
	print(item)
	print("\n\n")'''
#result = nlp.parse("I liked the food and the service was good.")
#pprint(result)

'''for item in parsedtext:
	#tree = Tree.parse(result['sentences'][0]['parsetree'])
	pprint(Tree(item))'''
