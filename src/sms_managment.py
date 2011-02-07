
import alert_env, re
import sms_alert

def WriteSMS2Log(sms):
    file = open('smslog.log', 'a')
    file.write(sms)
    file.write('\n')

text = ''
sms = alert_env.GetSMS()
while (sms != None):
    WriteSMS2Log(sms)
    try:
        p = re.compile('Sender: (\+\d+).*Text:(.+)', re.DOTALL)
        m = re.search(p, sms)
        if m == None:
            break
        sender = m.group(1)
        text = m.group(2)
    except ValueError:
        pass
    print sender
    if sender != "+79199230235" and sender != "+79199230203":
        sender = "+79199230235"

    if text.find('112') != -1:
        sms_alert.SendTempTo(num = sender, force = True)

    if text.find('disdelta') != -1:
        alert_env.SendSMSDelta = False
        alert_env.writeConfig()
        alert_env.SendSMS(num = sender, text = "Send SMS for delta: " + str(alert_env.SendSMSDelta))

    if text.find('endelta') != -1:
        alert_env.SendSMSDelta = True
        alert_env.writeConfig()
        alert_env.SendSMS(num = sender, text = "Send SMS for delta: " + str(alert_env.SendSMSDelta))

    break
    sms = alert_env.GetSMS()
