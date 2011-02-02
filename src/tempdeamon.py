#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ilyas"
__date__ ="$02.02.2011 22:10:31$"

import common
import time, random


DigiTemp = "/usr/bin/digitemp_DS9097"
TimeOut = 1

def GetTemp(IdSensor = 0):
    return random.randint(40, 50)
    parametr = ' -t %d -q -o "%%.2C" -c /home/nimda/.digitemprc' % (IdSensor)
    command = DigiTemp + parametr
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        out = process.communicate()[0]
        return float(out)
    except ValueError:
        return -100

tempBase = common.base(host = 'localhost', base='mydb', user='postgres', password='325616')
isWork = False
i = 0
while isWork:
    curTemp = GetTemp(0)
    tempBase.addTempToBase(curTemp)
    time.sleep(TimeOut)
    if i > 0: isWork = False
    i += 1

#r = tempBase.getLinesFromTable("temperature")
#for i in r:
#    print i[0],
#    if i[1] != None:
#        print i[1].strftime('%x %X'),
#    else:
#        print "None",
#    print i[2]
tempDate = tempBase.getTempFromBase()
print tempDate[0].strftime('%x %X'),
print tempDate[1]