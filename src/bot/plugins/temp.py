import xmpp
import sys, datetime
sys.path.append('/home/nimda/TempMonitor/src')
import alert_env

def init():
    return 0

def run(bot, mess):
    temp = alert_env.GetTemp()
    bot.send(xmpp.Message(mess.getFrom(), temp[0].strftime("%d/%m/%y %H:%M:%S") + "\r\nTemp: " + str(temp[1]) + "\r\nDelta: " + alert_env.GetShortDlt(temp[2])))
