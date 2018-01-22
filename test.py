from textblob import TextBlob

text = TextBlob(
    "bengal is culturally the most superior and richestthan all other indian states , and that's why you beggar indians come to eat bengali sweets. if we are weak then all you indians are dead literally")
for sen in text.sentences:
    print sen.sentiment
