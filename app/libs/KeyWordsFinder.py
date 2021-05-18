import RAKE
from unidecode import unidecode


def findKeywords(text):
    text = unidecode(text).encode('UTF-8', 'ignore')

    Rake = RAKE.Rake(RAKE.SmartStopList())
    words = Rake.run(text, minCharacters=3, maxWords=2)

    return words
