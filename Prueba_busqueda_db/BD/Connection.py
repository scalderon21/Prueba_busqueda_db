import mysql.connector
import sys

class Connection(object):
    def __init__(self, db_local):
        self.db_local = db_local
        self.db_conn = mysql.connector.connect(**self.db_local)
        self.db_cursor = self.db_conn.cursor()

    def get_rows(self,sql):
        cur = self.db_conn.cursor()
        cur.execute(sql)
        return(cur)
       





