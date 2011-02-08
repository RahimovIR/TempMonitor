import subprocess, os
import time, io, tty
import ConfigParser
import common


def readConfig():
    config = ConfigParser.RawConfigParser()
    config.read('alert_env.cfg')

    HighTempLevel = config.getint('AlertLevel', 'HighTempLevel')
    LowTempLevel  = config.getint('AlertLevel', 'LowTempLevel')
    DigiTemp = config.get('Programs','DigiTemp')
    Gnokii   = config.get('Programs','Gnokii')
    SendSMSDelta = config.getboolean('SendSMS','Delta')
    SendSMSTemp = config.getboolean('SendSMS','Temp')

    if HighTempLevel == None: HighTempLevel = 70
    if LowTempLevel == None: LowTempLevel  = 30
    if DigiTemp == None: DigiTemp = "/usr/bin/digitemp_DS9097"
    if Gnokii == None: Gnokii = "/usr/bin/gnokii"
    if SendSMSTemp == None: SendSMSTemp = True
    if SendSMSDelta == None: SendSMSDelta = True

def writeConfig():
    config = ConfigParser.RawConfigParser()

    config.add_section('AlertLevel')
    config.set('AlertLevel', 'HighTempLevel', str(HighTempLevel))
    config.set('AlertLevel', 'LowTempLevel', str(LowTempLevel))

    config.add_section('Programs')
    config.set('Programs', 'DigiTemp', DigiTemp)
    config.set('Programs', 'Gnokii', Gnokii)

    config.add_section('SendSMS')
    config.set('SendSMS', 'Delta', str(SendSMSDelta))
    config.set('SendSMS', 'Temp', str(SendSMSTemp))

    # Writing our configuration file to 'alert_env.cfg'
    with open('alert_env.cfg', 'wb') as configfile:
        config.write(configfile)


HighTempLevel = 70
LowTempLevel  = 30
DigiTemp = "/usr/bin/digitemp_DS9097"
Gnokii = "/usr/bin/gnokii"
SendSMSTemp = True
SendSMSDelta = True

testhost = ('ilyas-HP-2140',)
hostname = os.uname()[1]
testsms = """
1. Inbox Message (Unread)
Date/time: 03/02/2011 11:03:49 +0500
Sender: +79199230235 Msg Center: +79126313431
Text:
endelta
"""

readConfig()
writeConfig()

def GetTemp(IdSensor = 0):
    b = common.base(host = 'localhost', base='heating', user='tempuser', password='password')
    return b.getTempFromBase()

def GetMinMaxInDay():
    b = common.base(host = 'localhost', base='heating', user='tempuser', password='password')
    return b.getMinMaxInDay()

def GetShortDlt(dlt):
    return ':'.join(str(dlt).split(':')[:-1])


def SendSMS(num, text):
    command =  '/bin/echo "' + text + '" | ' + Gnokii + ' --sendsms ' + num
    if hostname in testhost:
        print command
        return 0
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        return process.returncode
    except ValueError:
        return -100

def GetSMS():
    if hostname in testhost:
        return testsms
    commands = Gnokii + ' --getsms ME '
    commands_delsms = Gnokii + ' --deletesms ME '
    count = 1
    sms_exist = True
    while (sms_exist):
        process = subprocess.Popen(commands + str(count), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait()
        outs, errors = process.communicate()
        if errors.find('failed') == -1:
            process = subprocess.Popen(commands_delsms + str(count), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            process.wait()
            return outs
        count += 1
        if count > 10:
            return None


def GetBalance():
    def writeToPort(s):
      p.write(s+'\r\n')
      time.sleep(0.1)

    p = io.open('/dev/ttyUSB1', 'w+b', 0)
    tty.setraw(p)
    writeToPort('AT+CPBS="SM"')
    writeToPort('AT+CPMS="SM","SM",""')
    writeToPort('AT+ZSNT=0,0,2')
    writeToPort('AT+CUSD=1,*100#,15')

    for ln in p:
      if ln.startswith('+CUSD'):
        result = ln[10:ln.rfind('"')].decode('hex').decode('utf-16-be')
        break

    p.close()
    return result

if __name__ == "__main__":
    print GetSMS()
