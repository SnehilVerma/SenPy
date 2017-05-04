from senticnet.senticnet import Senticnet
from nltk.stem import WordNetLemmatizer


wn=WordNetLemmatizer()




#TEST FILE.

word='hospitality'
word=wn.lemmatize(word,'v')
print word

sn=Senticnet()
concept_info = sn.concept('serious')
print concept_info
'''
polarity_value = sn.polarity_value('love')
print polarity_value
polarity_intense = sn.polarity_intense('love')
print polarity_intense
moodtags = sn.moodtags('love')
print moodtags
semantics = sn.semantics('love')
print semantics
sentics = sn.sentics('love')
print sentics
'''

