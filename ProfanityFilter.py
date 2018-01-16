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


def fetchlist():
    db_name = 'DirtyWords.db'
    conn = sqlite3.connect(db_name)
    cursor = conn.execute('SELECT word FROM dirty_words')

    output = []
    for row in cursor:
        output.append(row[0].encode('UTF8'))

    conn.close()

    return output


f = ProfanityFilter(fetchlist())
example = raw_input()
print f.filter(example)