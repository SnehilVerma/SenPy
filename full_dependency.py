import pickle
import json
from nltk.parse import DependencyGraph
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from nltk.parse.stanford import StanfordDependencyParser
from sklearn import tree
import csv
from senticnet.senticnet import Senticnet
from nltk.stem import WordNetLemmatizer


#graph for polarity vs categories
pospol=[]
negpol=[]



#//////CATPOL ORDER : SERVICE> STAFF> FOOD> COMFORT>VALUE FOR MONEY>INTERNET>LOCATION./////////////////

fp=csv.reader(open("posneg.csv",'rb'))

sn=Senticnet()
cat_score=[0,0,0,0,0,0,0]




#TO CONVERT PLURAL,PAST TENSE WORDS TO ITS ORIGINAL FORM. 
wnl = WordNetLemmatizer()




#load the sentence token file.
#tokens=pickle.load(open('token_dump.p','rb'))


#LOAD THE CATEGORY TERM FILES.
service=pickle.load(open('service.p','rb'))
food=pickle.load(open('food.p','rb'))
internet=pickle.load(open('internet.p','rb'))
staff=pickle.load(open('staff.p','rb'))
valuemoney=pickle.load(open('value for money.p','rb'))
comfort=pickle.load(open('comfort and cleanliness.p','rb'))
location=pickle.load(open('location.p','rb'))



with open('posw.csv','rb') as f:
	reader=csv.reader(f)
	poslist=list(reader)

with open('negw.csv','rb') as f:
	reader=csv.reader(f)
	neglist=list(reader)



class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(addr=("127.0.0.1", 8080)))
    
    def parse(self, text):
        return json.loads(self.server.parse(text))

nlp = StanfordNLP()

path_to_jar = '/home/snehil/Desktop/ML PROJECT FINAL/AspectPhase2/Aspect-Based-Sentiment-Analysis/stanford-corenlp-python/stanford-parser-full-2016-10-31/stanford-parser.jar'
path_to_models_jar = '/home/snehil/Desktop/ML PROJECT FINAL/AspectPhase2/Aspect-Based-Sentiment-Analysis/stanford-corenlp-python/stanford-parser-full-2016-10-31/stanford-parser-3.7.0-models.jar'
dep_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)




#print triples





def find_category(item):
	if item in service:
		return 'service'
	elif item in staff:
		return 'staff'
	elif item in food:
		return 'food'
	elif item in comfort:
		return 'comfort'
	elif item in valuemoney:
		return 'value for money'
	elif item in location:
		return 'location'
	elif item in internet:
		return 'internet and wifi'



def find_polarity(word,aspect,POS_tag):
	
	wa=[]
	wa.append(aspect)

	
	
	
	#GET THE WORD TO ITS SINGULAR PRESENT TENSE FORM.
	word=wnl.lemmatize(word)
	word=wnl.lemmatize(word,'v')
	

	#/////////TEST CODE FOR CATEGORY POLARITY/////////
	polarity=sn.polarity_value(word)




	print word
	#print the polarity word
	cat=find_category(aspect)
	if (cat=='location'):
		cat_score[5]+=1
	elif (cat=='staff'):
		cat_score[1]+=1
	elif (cat=='food'):
		cat_score[2]+=1
	elif (cat=='service'):
		cat_score[0]+=1
	elif (cat=='internet and wifi'):
		cat_score[6]+=1
	elif (cat=='value for money'):
		cat_score[4]+=1
	elif (cat=='comfort'):
		cat_score[3]+=1






	polarity_score=sn.polarity_intense(word)
	wa.append(polarity_score)
	if wa not in wa_list:
		global netscore
		netscore+=float(polarity_score)
		wa_list.append(wa)

	

	net=polarity+' '+polarity_score

	return net






def display_info(pol_aspect,aspect,netscore):
	print "ASPECTS POLARITY AND SCORE"
	used=[]

	for item in pol_aspect:
		if item not in used:
			print item
			used.append(item)


	cat_aspect=[]
	#CLUB THE ASPECT TERM AND ITS CATEGORY TOGETHER temporary.


	print "ASPECT CATEGORIES:"

	if flag==1:
		for item in aspect:
			category=find_category(item)
			cat_aspect.append(item)
			cat_aspect.append(category)
			cat_aspect_list.append(cat_aspect)


	used2=[]
	for item in cat_aspect_list:
		if item not in used2:
			print item
			used2.append(item)


	print  'FINAL POL SCORE'
	print netscore
	if(netscore >0):
		print "overall sentiment is positive!"
	else:
		print "overall sentiment is negative!"

	print "\n\n"










j=0
for rev,sentiment in fp:

	netscore=0.0
	#VARIABLE TO SCORE THE NET POLARITY OF ASPECTS.
	wa_list=[]
	#LIST TO STORE ASPECT AND SCORE FOR UNIQUNESS.
	aspect=[]
	#list to store the aspects occuring in a review
	cat_aspect_list=[]
	#list to store the aspect and its category in a review.

	temp_list=[]
	pol_aspect=[]
	#list to store the aspect and its polarity in a review.

	rev=rev.lower()
	result = dep_parser.raw_parse(rev)

	#result = dep_parser.raw_parse('we admired the location of the hotel.')
	dep = result.next()
	triples= list(dep.triples())
	#print triples


	flag=0
	for item in triples:

	#IMPORTANT : USING NOUN ADJECTIVE RELATION TO EXTRACT ASPECTS.
		if (item[0][1]=='JJ' and (item [2][1]=='NN' or item[2][1]=='NNP' or item[2][1]=='NNS' or item[2][1]=='NNPS') and item[1]=='nsubj'):
			#print item[2][0]
			#USE THE IMM. BELOW EXPRESSION TO USE POS AND NEG WORDNET LIST
			#pol=find_polarity([item[0][0]])

			pol=find_polarity(item[0][0],item[2][0],0)
			#0 is for noun tag

			temp_list.append(item[2][0])
			temp_list.append(pol)
			pol_aspect.append(temp_list)
			aspect.append(item[2][0])
			flag=1


		if ((item[0][1]=='NN' or item[0][1]=='NNP' or item[0][1]=='NNS' or item[0][1]=='NNPS') and item[2][1]=='JJ' and item[1]=='nsubj'):
			#print item[0][0]
			#USE THE IMM. BELOW EXPRESSION TO USE POS AND NEG WORDNET LIST
			#pol=find_polarity([item[2][0]])
			pol=find_polarity(item[2][0],item[0][0],0)
			temp_list.append(item[0][0])
			temp_list.append(pol)
			pol_aspect.append(temp_list)
			aspect.append(item[0][0])
			flag=1


			#EXTRACT ASPECTS USING VERB AND NOUN RELATION AND ASPECT IS THE TERM THE VERB IS USED FOR , LIKE : I LOVED THE FOOD
			#HERE, FOOD IS ASPECT ( NOUN ) AND VERB IS 'LOVED' WHICH IS FORMING THE OPINION ABOUT THE ASPECT.
		if ((item[0][1]=='VBD' or item[0][1]=='VBN') and (item [2][1]=='NN' ) and item[1]=='dobj'):
			#print item[2][0]
			#USE THE IMM. BELOW EXPRESSION TO USE POS AND NEG WORDNET LIST
			#pol=find_polarity([item[0][0]])


			pol=find_polarity(item[0][0],item[2][0],1)
			# '1' is for verb tag

			temp_list.append(item[2][0])
			temp_list.append(pol)
			pol_aspect.append(temp_list)
			aspect.append(item[2][0])
			flag=1


		if ((item[0][1]=='NN') and (item[2][1]=='VBD' or item[2][1]=='VBN') and item[1]=='dobj'):
			#print item[0][0]
			#USE THE IMM. BELOW EXPRESSION TO USE POS AND NEG WORDNET LIST
			#pol=find_polarity([item[2][0]])
			pol=find_polarity(item[2][0],item[0][0],1)
			temp_list.append(item[0][0])
			temp_list.append(pol)
			pol_aspect.append(temp_list)
			aspect.append(item[0][0])
			flag=1

	if(flag==1):
		print j+1
		display_info(pol_aspect,aspect,netscore)
	else:
		print j+1
		print "NO ASPECT FOUND, TRY PLAIN SENTIMENT ANALYSIS\n\n"
		

	j=j+1
	if j==150:
		break
	
print cat_score

pickle.dump(cat_score,open('cat_weight.p','wb'))




#PRINT THE COUNT OF CATEGORIES ENCOUNTERED DURING THE FIRST ITERATION
#PREPARE FOR NEXT ITERATION WHERE CATEGORY SCORE WILL BE CALCULATED.



###########################################PLOT DATA.
import plotly
from plotly.graph_objs import Bar, Layout

trace1 = Bar(
    x=['Service', 'Staff', 'Food', 'Comfort', 'Value', 'Location', 'Internet'],
    y=cat_score,
    name='Positive',
    marker=dict(
        color = 'rgb(64,219,59)'
    )
)

'''
trace2 = Bar(
    x=['Cleanliness', 'Comfort & Facilities', 'Food', 'Internet', 'Location', 'Staff', 'Value for money'],
    y=negpol,
    name='Negative',
    marker=dict(
        color = 'rgb(235,54,72)'
    )
)
'''

plotly.offline.plot({
"data": [
            trace1
],
"layout": Layout(
    title="Reviews by topic",
    barmode="group"
)
})




















