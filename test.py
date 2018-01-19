from time import time

from nltk.corpus import wordnet as wn

start = time()
wn_lemmas = set(wn.all_lemma_names())
x = wn.synsets('well')
print time() - start
print x
