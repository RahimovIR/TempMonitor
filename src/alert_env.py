import subprocess
import time, io, tty

HighTempLevel = 70
LowTempLevel  = 30
DigiTemp = "/usr/bin/digitemp_DS9097"
Gnokii = "/usr/bin/gnokii"


def GetTemp(IdSensor = 0):
    parametr = ' -t %d -q -o "%%.2C" -c /home/nimda/.digitemprc' % (IdSensor)
    command = DigiTemp + parametr
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        out = process.communicate()[0]
        return float(out)
    except ValueError:
        return -100

def SendSMS(num, text):
    command =  '/bin/echo "' + text + '" | ' + Gnokii + ' --sendsms ' + num
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        return process.returncode
    except ValueError:
        return -100

def GetSMS():
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
