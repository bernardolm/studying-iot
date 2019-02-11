import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
for i in range(1,10):
	print "LED on {0}".format(i)
	GPIO.output(18,GPIO.HIGH)
	time.sleep(1)

	print "LED off {0}".format(i)
	GPIO.output(18,GPIO.LOW)
	time.sleep(1)
GPIO.cleanup()

