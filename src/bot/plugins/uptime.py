import xmpp

def uptime():
    proc_uptime = open("/proc/uptime", "r")
    uptime_raw = proc_uptime.read()
    proc_uptime.close()
     
    uptime_raw = uptime_raw.split(" ")
    uptime_raw = float(uptime_raw[0])
    minute = 60
    hour = minute * 60
    day = hour * 24
     
    days = int(uptime_raw / day)
    hours = int((uptime_raw % day) / hour)
    minutes = int((uptime_raw % hour) / minute)
    seconds = int(uptime_raw % minute)
     
    return (days, hours, minutes, seconds)
 

def init():
    return 0

def run(bot, mess):
    u = uptime()
    text = "Uptime: %s days, %s:%s:%s" % (u[0],u[1],u[2],u[3])
    bot.send(xmpp.Message(mess.getFrom(), text))
