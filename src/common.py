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

    def getLastLineFromTable(self, table='', numLines=1):
        if (table == ''):
            return None
        self.cur.execute("""SELECT max(id) FROM temperature""")
        line = self.cur.fetchone()
        if (line[0] == None):
            return (datetime.datetime.now(), -100)
        maxId = int(line[0])
        if (maxId < numLines):
            numLines = maxId
        self.cur.execute("""SELECT * FROM temperature WHERE (id > %s)""", (maxId - numLines,))
        return self.cur.fetchall()


    def getTempFromBase(self):
        """
        Return last date and temperature
        """
        self.cur.execute("""SELECT max(id) FROM temperature""")
        line = self.cur.fetchone()
        if (line[0] == None):
            return (datetime.datetime.now(), -100)
        maxId = int(line[0])
        self.cur.execute("""SELECT *, now() - datetime as dlt FROM temperature WHERE (id = %s)""", (maxId,))
        line = self.cur.fetchone()
        return (line[1], line[2], line[3])

    def getMinMaxInDay(self):
        self.cur.execute("""SELECT * FROM temperature WHERE NOW() - datetime < interval '1 day' ORDER BY temp LIMIT 1""")
        tmin = self.cur.fetchone()
        self.cur.execute("""SELECT * FROM temperature WHERE NOW() - datetime < interval '1 day' ORDER BY temp DESC LIMIT 1""")
        tmax = self.cur.fetchone()
        return (tmin, tmax)


    def addTempToBase(self, temp):
        self.cur.execute("""INSERT INTO temperature (datetime, temp) VALUES (%s, %s)""" , (datetime.datetime.now(), temp))
        self.conn.commit()




if __name__ == '__main__':
    b = base(host = 'localhost', base='heating', user='tempuser', password='password')
    print b.getMinMaxInDay()
