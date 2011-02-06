
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
    if text.find('112'):
        print sender
        print text
        sms_alert.SendTempTo(num = sender, force = True)
    break
    sms = alert_env.GetSMS()
