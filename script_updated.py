# Imports
import webiopi
import time
import subprocess
import psutil

pin = {'r1_l':15, 'r2_f':24, 'r3_l':16, 'r4_l':3, 'r4_t':17 ,'r5_l':10, 'r5_f':11, 'p':22, 'l':21, 'd':18};
pirid = 0
flameid = 0
# Enable debug output
webiopi.setDebug()

# Retrieve GPIO lib
GPIO = webiopi.GPIO
#continue
def setup():
    GPIO.setFunction(15,GPIO.OUT);
    GPIO.setFunction(24,GPIO.OUT);
    GPIO.setFunction(16,GPIO.OUT);
    GPIO.setFunction(3,GPIO.OUT);
    GPIO.setFunction(17,GPIO.IN);
    GPIO.setFunction(10,GPIO.OUT);
    GPIO.setFunction(11,GPIO.OUT);
    GPIO.setFunction(22,GPIO.IN);
    GPIO.setFunction(21,GPIO.OUT);
    GPIO.setFunction(18,GPIO.OUT);
    GPIO.setFunction(23,GPIO.OUT);

@webiopi.macro
def ONOFF(id,stat):

    st = int(stat)
    
#code of pir sensor
    global pirid
    if pin[id] == 22:
        if st == 0:
            pir = subprocess.Popen(['python','pirrun.py'])
            pirid = pir.pid
        else:
            if pirid != 0:
                pir1 = psutil.Process(pirid)
                pir1.kill()
                pirid = 0
    return

#code for flame sensor
    global flameid
    if pin[id] == 17:
        if st == 0:
            flame = subprocess.Popen(['python','flamerun.py'])
            flameid = flame.pid
        else:
            if flameid != 0:
                flame1 = psutil.Process(flameid)
                flame1.kill()
                flameid = 0
    return

#code for door
    if pin[id] == 18:
        GPIO.digitalWrite(18,0)
        GPIO.digitalWrite(23,0)
        if st==0:
            GPIO.digitalWrite(23,0)
            GPIO.digitalWrite(18,1)
        else:
            GPIO.digitalWrite(18,0)
            GPIO.digitalWrite(23,1)
    time.sleep(1)
    return



#code for light and fan
	if st == 0:
	GPIO.digitalWrite(pin[id],1);
	else:
	GPIO.digitalWrite(pin[id],0);
