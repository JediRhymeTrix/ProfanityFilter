import re
import sqlite3


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

        regexp = (regexp_insidewords[self.inside_words] %
                  '|'.join(self.badwords))

        r = re.compile(regexp, re.IGNORECASE if self.ignore_case else 0)

        return r.findall(text)


def fetchlist(url=None):
    db_name = 'DirtyWords.db'
    conn = sqlite3.connect(db_name)
    cursor = conn.execute('SELECT word FROM dirty_words')

    output = []
    for row in cursor:
        output.append(row[0].encode('UTF8'))

    if url:
        from urllib2 import urlopen
        resp = urlopen(url)

        for word in resp.read().strip().split('\n'):
            if word != '' or word != ' ':
                output.append(word)

    conn.close()

    return output


def applyFilter(input, url=None):
    f = ProfanityFilter(fetchlist(url))
    return f.filter(input)
