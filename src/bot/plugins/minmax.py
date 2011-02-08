import xmpp
import sys, datetime
sys.path.append('/home/nimda/TempMonitor/src')
import alert_env

def init():
    return 0

def run(bot, mess):
    (tmin, tmax)=alert_env.GetMinMaxInDay()
    strmin = tmin[1].strftime("%d/%m/%y %H:%M:%S") + " Temp min: " + str(tmin[2])
    strmax = tmax[1].strftime("%d/%m/%y %H:%M:%S") + " Temp max: " + str(tmax[2])
    bot.send(xmpp.Message(mess.getFrom(), strmin + "\r\n" + strmax))
