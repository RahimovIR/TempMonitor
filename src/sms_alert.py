#!/usr/bin/python

import alert_env, datetime


def SendTempTo(num = '+79199230235', force = False):
    curTemp = alert_env.GetTemp(0)
    if (alert_env.HighTempLevel < curTemp[1]) or (curTemp[1] < alert_env.LowTempLevel) or force:
        print "send sms to " + str(num)
        time = curTemp[0].strftime("%d/%m/%y %H:%M:%S")
        alert_env.SendSMS(num, time + ' Temperatura: ' + str(curTemp[1]))

if __name__ == "__main__":
    SendTempTo(num = "+79199230235")
    SendTempTo(num = "+79199230203")
