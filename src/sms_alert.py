#!/usr/bin/python

import alert_env, datetime


def SendTempTo(num = '+79199230235', force = False):
    temp = alert_env.GetTemp(0)
    delta = datetime.timedelta(minutes = 5)
    strDelta = ':'.join(str(temp[2]).split(':')[:-1])
    time = temp[0].strftime("%d/%m/%y %H:%M:%S")

    if alert_env.SendSMSTemp and ( (alert_env.HighTempLevel < temp[1]) or (temp[1] < alert_env.LowTempLevel) ):
        alert_env.SendSMS(num, time + ' Temperatura: ' + str(temp[1]) + ' dlt: ' + strDelta)

    if alert_env.SendSMSDelta and ( (temp[2] > delta) or force ):
        alert_env.SendSMS(num, time + ' Temperatura: ' + str(temp[1]) + ' dlt: ' + strDelta)

if __name__ == "__main__":
    SendTempTo(num = "+79199230235")
    SendTempTo(num = "+79199230203")
