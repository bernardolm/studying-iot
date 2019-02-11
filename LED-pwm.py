import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,100)     #Configura para 100 Hz
pwm.start(0)             #Inicia com DC=0%

while(1):
    for dc in range(0,100,1):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.1)
