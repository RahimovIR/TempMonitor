#!/usr/bin/python

import alert_env, datetime


def SendTempTo(num = '+79199230235', force = False):
    curTemp = alert_env.GetTemp(0)
    if (alert_env.HighTempLevel < curTemp[1]) or (curTemp[1] < alert_env.LowTempLevel) or force:
        print "send sms to " + str(num)
        time = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        alert_env.SendSMS(num, time + ' Temperatura: ' + str(curTemp))

if __name__ == "__main__":
    SendTempTo(num = "+79199230235")
    SendTempTo(num = "+79199230203")
