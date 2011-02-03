# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ilyas"
__date__ ="$29.01.2011 2:24:54$"

import common, datetime

if __name__ == "__main__":
    b = common.base(host = 'localhost', base='mydb', user='postgres', password='325616')
    #r = b.getTestTable()
    r = b.getLinesFromTable("temperature")
    b.addTempToBase(49.57)
    for i in r:
        print i[0],
        if i[1] != None:
            print i[1].strftime('%x %X'),
        else:
            print "None",
        print i[2]
    tempDate = b.getTempFromBase()
    print tempDate[0].strftime('%x %X'),
    print tempDate[1]

    #b.setTestTable("6", "45234", "342985723")
