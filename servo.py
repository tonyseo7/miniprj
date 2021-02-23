import RPi.GPIO as gpio
import time

pin=11

gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

pwm = gpio.PWM(pin, 50)
pwm.start(3.0)

for cnt in range(0,3):
    pwm.ChangeDutyCycle(3.0)
    time.sleep(1.0)
    pwm.ChangeDutyCycle(12.5)
    time.sleep(1.0)

pwm.ChangeDutyCycle(1.0)


pwm.stop()
gpio.cleanup()
