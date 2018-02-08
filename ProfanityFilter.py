import re
import sqlite3
from utils.regex_safe import make_regex_safe

db_name = 'data/DirtyWords.db'
conn = sqlite3.connect(db_name)
cursor = conn.execute('SELECT word FROM dirty_words')

wordlist = []
for row in cursor:
    wordlist.append(make_regex_safe(row[0].encode('UTF8').strip()))

conn.close()


class ProfanityFilter(object):

    def __init__(self, filterlist, ignore_case=True, inside_words=False):
        self.badwords = filterlist
        self.ignore_case = ignore_case
        self.inside_words = inside_words

    def filter(self, text):
        regexp_insidewords = {
            True: r'(%s)',
            False: r'\b(%s)\b',
        }

        exp = '|'.join(self.badwords)
        regexp = (regexp_insidewords[self.inside_words] % exp)
        r = re.compile(regexp, re.IGNORECASE if self.ignore_case else 0)

        res = r.findall(text)
        if isinstance(res[0], list):
            return res
        else:
            words = []
            for wordlist in res:
                for word in wordlist:
                    if word != '':
                        words.append(word)
            return words


def fetchlist(url):
        from urllib2 import urlopen
        resp = urlopen(url)

        for word in resp.read().strip().split('\n'):
            if word != '' or word != ' ':
                wordlist.append(word)


def applyFilter(input, url=None):
    if url:
        fetchlist(url)

    f = ProfanityFilter(wordlist)
    res = f.filter(input)

    return res
