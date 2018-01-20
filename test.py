from pywsd import disambiguate
from nltk import word_tokenize
import string
from pywsd.similarity import max_similarity as maxsim
from time import time
from nltk.corpus import stopwords


cachedStopWords = stopwords.words("english")
start = time()
sen = "Well, I completely disagree with this 'wonderful' lady who doesn't know anything and acts like she has never set foot in Spain. God, I'd like to gag her! fuck chutiya"
sen = ' '.join([word for word in word_tokenize(sen.lower().translate(None, string.punctuation)) if word not in cachedStopWords])
print (sen)
disambiguate(sen)
end = time()
print (end - start)