import urllib2
import re

class ProfanityFilter(object):
	
    def __init__(self, filterlist, ignore_case=True, inside_words=False):
        self.badwords = filterlist
        self.ignore_case = ignore_case
        self.inside_words = inside_words

    def clean(self, text):     
        regexp_insidewords = {
            True: r'(%s)',
            False: r'\b(%s)\b',
            }

        regexp = (regexp_insidewords[self.inside_words] % 
                  '|'.join(self.badwords))

        r = re.compile(regexp, re.IGNORECASE if self.ignore_case else 0)

        return r.findall(text)
        
def fetchList(url): 
    	resp = urllib2.urlopen(url) 
    	badwords = str(resp.read()).strip().split('\n') 
    	return badwords

url = 'http://www.cs.cmu.edu/~biglou/resources/bad-words.txt'
f = ProfanityFilter(fetchList(url))    
example = "i have been assigned a fucking hell task by an asshole dumbass ass"
print f.clean(example)
