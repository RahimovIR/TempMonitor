import xmpp

def init():
    return 0

def run(bot, mess):
    text = mess.getBody()[5:]
    bot.send(xmpp.Message(mess.getFrom(), text))
