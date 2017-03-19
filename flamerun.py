import RPi.GPIO as GPIO
import smtplib
import urllib2
import cookielib
from getpass import getpass
import sys
import os
from stat import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(27,GPIO.IN)

def ring_buzzer():
	GPIO.digitalWrite(27,1)
	time.sleep(0.5)
	GPIO.digitalWrite(27,0)


def send_mail():
	c = "Fire has been detected in your house"
	mail = smtplib.SMTP('smtp.gmail.com',587)
	mail.ehlo()
	mail.starttls()
	mail.login('','')
	mail.sendmail('ravi.yadav@ves.ac.in','ravi.yadav@ves.ac.in',c)
	mail.close()

def send_msg():
	message = "Fire has been detected in your house"
	number = "7507827367"

	if __name__ == "__main__":  
	    username = "9657583510"
	    passwd = "rajiv9230"

	    message = "+".join(message.split(' '))

 #logging into the sms site
	    url ='http://site24.way2sms.com/Login1.action?'
	    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

	 #For cookies

	    cj= cookielib.CookieJar()
	    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	 #Adding header details
	    opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
	    try:
	        usock =opener.open(url, data)
	    except IOError:
	        print "error"
	        #return()

	    jession_id =str(cj).split('~')[1].split(' ')[0]
	    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
	    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
	    opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
	    try:
	        sms_sent_page = opener.open(send_sms_url,send_sms_data)
	    except IOError:
	        print "error"
	        #return()


while True:
	if GPIO.input(17): #pin change kaer
		print("Flame Detected")
		send_mail()
		send_msg()
		#ring_buzzer()
		time.sleep(30)
	else:
		print("Not Detected")
		time.sleep(3)
