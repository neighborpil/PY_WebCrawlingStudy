import urllib.request
import urllib.parse
import urllib.error
import json
import sqlite3

URL = 'http://api.plos.org/search?q=title:DNA'

class ClassifyURL:
    conn = sqlite3.connect('ApiPlosDB.sqlite')
    cur = conn.cursor()
    
    def __init__(self):
        self.createTables() 

    """
    테이블 생성
    """
    def createTables(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS "docs" 
        ( `idx` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, `id` TEXT NOT NULL, `journal` TEXT, `eissn` TEXT, 
        `publication_date` TEXT, `article_type` TEXT, `abstract` TEXT, `title_display` TEXT, `score` REAL )''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS `author`
        ( `idx` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, `author` TEXT, `docs_idx` INTEGER )''')

    """
    url 받아 json 변환
    """
    def crawlingJSON(self):
        try:
            connection = urllib.request.urlopen(URL)
            data = connection.read().decode()

        except Exception as err:
            print('Failed to Retrieve', err)
            return

        try:
            js = json.loads(data)
            
            return js
        except:
            print('Unable to parse json')
            print(data)

    """
    DNA에 관한 내용 파싱
    """
    def parseDNA(self, js):
        if js is None:
            print('js is None')
            return

        for doc in js['response']['docs']:
            try:
                id = doc['id']
                journal = doc['journal']
                eissn = doc['eissn']
                publication_date = doc['publication_date']
                article_type = doc['article_type']
                author_display = doc['author_display']
                abstract = doc['abstract']
                title_display = doc['title_display']
                score = doc['score']
            except:
                print('json error')
                continue

            self.cur.execute("SELECT idx FROM docs WHERE id = ?", (id,))

            try:
                idx = self.cur.fetchone()[0]
            except:
                idx = None
            
            if idx is None:
                # insert new
                query = 'INSERT OR IGNORE INTO docs (id, journal, eissn, publication_date, article_type, abstract, title_display, score)'
                query += 'VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
                self.cur.execute(query, (id, journal, eissn, publication_date, article_type, ",".join(abstract), title_display, float(score)))

                self.conn.commit()
                if self.cur.rowcount != 1:
                    print('Error inserting data')
                    continue
                # insert author
                
                docs_idx = self.selectIdx(id)
                self.insertAuthor(docs_idx, author_display)
                
            else:
                self.cur.execute('UPDATE docs SET journal=?, eissn=?, publication_date=?, article_type=?, abstract=?, title_display=?, score=? WHERE id = ?',
                            (journal, eissn, publication_date, article_type, ",".join(abstract), title_display, float(score), id))
                self.conn.commit()
                if self.cur.rowcount != 1:
                    print('Error update docs')
                    continue
                # insert author
                docs_idx = self.selectIdx(id)
                self.insertAuthor(docs_idx, author_display)

    def selectIdx(self, id):
        self.cur.execute('SELECT idx FROM docs WHERE id = ?', (id,))
        try:
            idx = self.cur.fetchone()[0]
        except:
            idx = None
        return idx

    """
    author 테이블 insert
    """
    def insertAuthor(self, docs_idx, author_display):
        # insert author_display
        self.cur.execute('DELETE FROM author WHERE docs_idx = ?', (docs_idx,))
        for author in author_display:
            self.cur.execute('INSERT OR IGNORE INTO author (author, docs_idx) VALUES(?, ?)', (author, docs_idx))

    """
    결과 select
    """
    def getDocs(self):
        self.cur.execute('SELECT docs.*, author.* FROM docs JOIN author ON docs.idx = author.docs_idx')
        try:
            for row in self.cur.fetchall():
                print(row)
        except:
            print('couldn\'t select datas')

    def __del__(self):
        self.cur.close()

# __main__
cl = ClassifyURL()
# Debugging
# print(json.dumps(cl.crawlingJSON(), indent=4))
js = cl.crawlingJSON()

if js is not None:
    js = cl.parseDNA(js)
    cl.getDocs()
    
