# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
from os import path
import sqlite3
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
class FjsenPipeline(object):

    def __init__(self):
        self.conn=None
        self.filename="fjsen_test"
        dispatcher.connect(self.initialize,signals.engine_started)
        dispatcher.connect(self.finalize,signals.engine_stopped)
    def process_item(self,item,spider):
        print item
        if not item['title'] or not item["link"] or not item["addtime"]:
          pass
        else:
          self.conn.execute('insert into fjsen values(?,?,?,?)',(None,item['title'][0],'http://www.jb51.net/'+item['link'][0],item['addtime'][0]))
        return item
    def initialize(self):
        if path.exists(self.filename):
            self.conn=self.truncate_table(self.filename)
        else:
            self.conn=self.create_table(self.filename)
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn=None
    def create_table(self,filename):
        conn=sqlite3.connect(filename)
        conn.execute("""create table fjsen(id integer primary key autoincrement,title text,link text,addtime text)""")
        conn.commit()
        return conn

    def truncate_table(self,filename):
        conn=sqlite3.connect(filename)
        #conn.execute("""DELETE from fjsen""")
        conn.execute("""drop table fjsen""")
        conn.execute("""create table fjsen(id integer primary key autoincrement,title text,link text,addtime text)""")
        conn.commit()
        return conn
