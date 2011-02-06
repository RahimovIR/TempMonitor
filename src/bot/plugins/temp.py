import xmpp
import sys, datetime
sys.path.append('/home/nimda/TempMonitor/src')
import alert_env

def init():
    return 0

def run(bot, mess):
    text = alert_env.GetTemp()
    bot.send(xmpp.Message(mess.getFrom(), text[0].strftime("%d/%m/%y %H:%M:%S") + "\r\nTemp: " + str(text[1])))
