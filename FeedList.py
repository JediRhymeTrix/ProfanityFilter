import sys
import sqlite3

db_name = './data/DirtyWords.db'
conn = sqlite3.connect(db_name)
# conn.text_factory = str

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


feed('./data/feed_list.txt', 'en')