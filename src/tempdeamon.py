#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ilyas"
__date__ ="$02.02.2011 22:10:31$"

import common
import time, random, os, subprocess


DigiTemp = "/usr/bin/digitemp_DS9097"
testhost = ('ilyas-HP-2140',)
TimeOut = 60
hostname = os.uname()[1]

def GetTemp(IdSensor = 0):
    if (hostname in testhost):
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

tempBase = common.base(host = 'localhost', base='heating', user='tempuser', password='password')

isWork = True
if (hostname in testhost):
    isWork = False
    print GetTemp(0)

while isWork:
    curTemp = GetTemp(0)
    tempBase.addTempToBase(curTemp)
    print curTemp
    time.sleep(TimeOut)

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