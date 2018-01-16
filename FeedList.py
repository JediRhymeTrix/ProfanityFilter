import sys
import sqlite3

db_name = 'DirtyWords.db'
conn = sqlite3.connect(db_name)


def feed(src, lang):
    for word in open(src, 'r'):
        t = (word.strip(), lang, )
        conn.execute('INSERT INTO dirty_words (word, language) values(?, ?)', t)


feed('test.txt', 'en')