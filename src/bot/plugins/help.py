import xmpp

def init():
    return 0

def run(bot, mess):
    sender = mess.getFrom()
    sender = str(sender).split('/')[0]
    text = '\r\npublic commands: '
    for i in bot.plugins['public_commands']:
        text += str(i) + ', '
    text = text[:-2]
    if sender in bot.config['user_no_pass']:
        text += '\r\nadmin commands: '
        for i in bot.plugins['commands']:
            text += str(i) + ', '
        text = text[:-2]
    bot.send(xmpp.Message(mess.getFrom(), text))
