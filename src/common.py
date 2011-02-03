import datetime

import psycopg2

class base:
    def __init__(self, host, base, user, password):
        self.host = host
        self.base = base
        self.user = user
        self.password = password
        self.conn = psycopg2.connect(host=host, database=base, user=user, password=password)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def getLinesFromTable(self, table='', numStart=0, numEnd=0):
        if (table == ''):
            return None
        if (numStart > numEnd):
            self.cur.execute("""SELECT * FROM %s WHERE (id >= %s) and (id <= %s) """ % (table, str(numStart), str(numEnd)))
        else:
            self.cur.execute("""SELECT * FROM %s """ % table)
        return self.cur.fetchall()

    def getTempFromBase(self):
        self.cur.execute("""SELECT max(id) FROM temperature""")
        line = self.cur.fetchone()
        if (line[0] == None):
            return (datetime.datetime.now(), -100)
        maxId = int(self.cur.fetchone()[0])
        self.cur.execute("""SELECT * FROM temperature WHERE (id = %s)""", (maxId,))
        line = self.cur.fetchone()
        return (line[1], line[2])
        

    def addTempToBase(self, temp):
        self.cur.execute("""INSERT INTO temperature (datetime, temp) VALUES (%s, %s)""" , (datetime.datetime.now(), temp))
        self.conn.commit()




if __name__ == '__main__':
    pass
