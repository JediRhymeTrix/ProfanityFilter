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
        if res != [] and isinstance(res[0], list):
            return res
        else:
            words = []
            for wordlist in res:
                for word in wordlist:
                    if word != '':
                        words.append(word)
            return words


def fetchlist(url, ignore_words_url, wordlist_local):
        from urllib2 import urlopen

        if url is not None:
            resp = urlopen(url)

            for word in resp.read().strip().split('\n'):
                if word != '' or word != ' ':
                    wordlist_local.append(word)
        if ignore_words_url is not None:
            resp = urlopen(ignore_words_url)

            for word in resp.read().strip().split('\n'):
                if word in wordlist:
                    wordlist_local.remove(word)

        return wordlist_local


def applyFilter(input, url=None, ignore_words_url=None):
    wordlist_local = wordlist
    if url != None or ignore_words_url != None:
        wordlist_local = fetchlist(url, ignore_words_url, wordlist_local)

    f = ProfanityFilter(wordlist_local)
    res = f.filter(input)

    return res
