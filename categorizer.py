from nltk.corpus import wordnet as wn
import pickle



service=[]
for synset in wn.synsets('service'):
    for lemma in synset.lemmas():
        service.append(lemma.name())
for synset in wn.synsets('room'):
    for lemma in synset.lemmas():
        service.append(lemma.name())
for synset in wn.synsets('hotel'):
    for lemma in synset.lemmas():
        service.append(lemma.name())




staff=[]
for synset in wn.synsets('staff'):
    for lemma in synset.lemmas():
        staff.append(lemma.name())

for synset in wn.synsets('waiter'):
    for lemma in synset.lemmas():
        staff.append(lemma.name())

for synset in wn.synsets('driver'):
    for lemma in synset.lemmas():
        staff.append(lemma.name())

for synset in wn.synsets('cook'):
    for lemma in synset.lemmas():
        staff.append(lemma.name())
for synset in wn.synsets('maid'):
    for lemma in synset.lemmas():
        staff.append(lemma.name())
for synset in wn.synsets('bellboy'):
    for lemma in synset.lemmas():
        staff.append(lemma.name())






food=[]
for synset in wn.synsets('food'):
    for lemma in synset.lemmas():
        food.append(lemma.name())
for synset in wn.synsets('lunch'):
    for lemma in synset.lemmas():
        food.append(lemma.name())
for synset in wn.synsets('dinner'):
    for lemma in synset.lemmas():
        food.append(lemma.name())
for synset in wn.synsets('restaurant'):
    for lemma in synset.lemmas():
        food.append(lemma.name())



location=[]
for synset in wn.synsets('location'):
    for lemma in synset.lemmas():
        location.append(lemma.name())
for synset in wn.synsets('scene'):
    for lemma in synset.lemmas():
        location.append(lemma.name())
for synset in wn.synsets('view'):
    for lemma in synset.lemmas():
        location.append(lemma.name())



money=[]
for synset in wn.synsets('money'):
    for lemma in synset.lemmas():
        money.append(lemma.name())
for synset in wn.synsets('value'):
    for lemma in synset.lemmas():
        money.append(lemma.name())
for synset in wn.synsets('economic'):
    for lemma in synset.lemmas():
        money.append(lemma.name())
for synset in wn.synsets('cheap'):
    for lemma in synset.lemmas():
        money.append(lemma.name())



comfort=[]
for synset in wn.synsets('comfort'):
    for lemma in synset.lemmas():
        comfort.append(lemma.name())
for synset in wn.synsets('clean'):
    for lemma in synset.lemmas():
        comfort.append(lemma.name())
for synset in wn.synsets('bed'):
    for lemma in synset.lemmas():
        comfort.append(lemma.name())
for synset in wn.synsets('shower'):
    for lemma in synset.lemmas():
        comfort.append(lemma.name())
for synset in wn.synsets('tub'):
    for lemma in synset.lemmas():
        comfort.append(lemma.name())
for synset in wn.synsets('bathroom'):
    for lemma in synset.lemmas():
        comfort.append(lemma.name())





internet=[]
for synset in wn.synsets('internet'):
    for lemma in synset.lemmas():
        internet.append(lemma.name())
for synset in wn.synsets('wifi'):
    for lemma in synset.lemmas():
        internet.append(lemma.name())




pickle.dump(service,open('service.p','wb'))
pickle.dump(staff,open('staff.p','wb'))
pickle.dump(food,open('food.p','wb'))
pickle.dump(location,open('location.p','wb'))
pickle.dump(internet,open('internet.p','wb'))
pickle.dump(comfort,open('comfort and cleanliness.p','wb'))
pickle.dump(money,open('value for money.p','wb'))









