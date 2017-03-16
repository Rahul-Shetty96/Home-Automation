# Imports
import webiopi
import time

 pin = {r1_l:15, r2_f:24, r3_1l:16, r3_2l:21, r4_l:3, r4_t:17 ,r5_l:10, r5_f:11, p:0, l:0, d:0};

# Enable debug output
webiopi.setDebug()

# Retrieve GPIO lib
GPIO = webiopi.GPIO

def setup():
    GPIO.setFunction(15,GPIO.OUT);
    GPIO.setFunction(24,GPIO.OUT);
    GPIO.setFunction(16,GPIO.OUT);
    GPIO.setFunction(21,GPIO.OUT);
    GPIO.setFunction(3,GPIO.OUT);
    GPIO.setFunction(17,GPIO.IN);
    GPIO.setFunction(10,GPIO.OUT);
    GPIO.setFunction(11,GPIO.OUT);
    #GPIO.setFunction(3,GPIO.OUT);
    #GPIO.setFunction(17,GPIO.IN);
    #GPIO.setFunction(10,GPIO.OUT);

@webiopi.macro
def ONOFF(id,stat):
	st=int(stat)
	if st == 0:
	GPIO.digitalWrite(pin[id],1);
	else:
	GPIO.digitalWrite(pin[id],0);
	
