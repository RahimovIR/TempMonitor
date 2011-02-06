#!/usr/bin/python

import ConfigParser, xmpp, os, datetime

def LoadConfig():
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    login = config.get('connect', 'login')
    password = config.get('connect', 'password')
    user_no_pass = config.get('permission', 'user_no_pass')
    return {'login':login, 'password':password, 'user_no_pass':user_no_pass}

def Message(conn, mess):
    global bot
    text = mess.getBody()

    if ( text  == None ):
        return
    command = text.split(' ')
    command = command[0]

    if command in bot.plugins['public_commands']:
        RunPlugin(command, bot, mess)
        return
    user = mess.getFrom()
    user = str(user).split('/')
    user = user[0]

    if user not in bot.config['user_no_pass']:
        text = "wrong command. Try 'help'"
        bot.send(xmpp.Message(mess.getFrom(), text))
        return

    if command in bot.plugins['commands']:
        RunPlugin(command, bot, mess)
    else:
        text = "wromg command. try 'help'"
        bot.send(xmpp.Message(mess.getFrom(), text))

def LoadPlugins():
    commands = []
    public_commands = []
    for fname in os.listdir('plugins/'):
        if fname.endswith('.py'):
            plugin_name = fname[:-3]
            if plugin_name != '__init__':
                plugins = __import__('plugins.'+plugin_name)
                plugin = getattr(plugins, plugin_name)
                if plugin.init():
                    commands.append(plugin_name)
                else:
                    public_commands.append(plugin_name)
    return {'plugins':plugins, 'commands':commands, 'public_commands':public_commands}

def RunPlugin(command, bot, mess):
    plugin = getattr(bot.plugins['plugins'], command)
    plugin.run(bot, mess)

def SetStatus(bot, status):
    bot.statusTime = datetime.datetime.now()
    bot.status.setStatus(status + ' ' + bot.statusTime.strftime('%X'))
    bot.send(bot.status)


config = LoadConfig()
jid = xmpp.JID(config['login'])
bot = xmpp.Client(jid.getDomain(), debug=[])
bot.config = config

bot.plugins = LoadPlugins()
bot.status = xmpp.Presence()

bot.connect()
bot.auth(jid.getNode(), bot.config['password'])

bot.RegisterHandler('message', Message)
bot.sendInitPresence()

SetStatus(bot, "online")

bot.online = 1
while bot.online:
    bot.Process(1)
    now = datetime.datetime.now()
    if (now - bot.statusTime > datetime.timedelta(seconds = 5)) :
        SetStatus(bot, "online")

bot.disconnect()
