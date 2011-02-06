import xmpp

def init():
    return 1

def run(bot, mess):
    text = "by :)"
    bot.send(xmpp.Message(mess.getFrom(), text))
    bot.online = 0
