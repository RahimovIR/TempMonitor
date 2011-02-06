import xmpp
import imp

def init():
    return 0

def run(bot, mess):
    alert_env = imp.load_source('alert_env', '../alert_env.py')
    text = alert_env.GetTemp()
    bot.send(xmpp.Message(mess.getFrom(), text))
