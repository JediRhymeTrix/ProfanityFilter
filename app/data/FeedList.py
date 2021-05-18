import sys
import sqlite3
import argparse


db_name = 'DirtyWords.db'
conn = sqlite3.connect(db_name)
# conn.text_factory = str


def parseLang():
    parser = argparse.ArgumentParser(description='Accepts a 2-letter language code. Default is en.')
    parser.add_argument('-l', default='en', help='Accepts a 2-letter language code. Default is en')
    args = parser.parse_args()
    
    return args.l


def feed(src, lang):
    for word in open(src, 'r'):
        t = (word.strip(), lang, )
        try:
            conn.execute('INSERT INTO dirty_words (word, language) values(?, ?)', t)
        except Exception as e:
            try:
                print 'skipped duplicate - ', t[0]
            except Exception as e:
                continue
    print 'Done!'
    conn.commit()
    conn.close()

parseLang()
feed('feed_list.txt', lang)
