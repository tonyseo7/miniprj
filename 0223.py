import RPi.GPIO as gpio
import time

buzz_pin = 18
pir_pin = 18

gpio.setmode(gpio.BCM)
gpio.setup(pir_pin,gpio.IN)
#gpio.setup(buzz_pin,gpio.OUT)
#pwm = gpio.PWM(buzz_pin, 1)
#pwm.start(50.0)

pir_input = 0

try:
    while True:
        pir_input = gpio.input(pir_pin)
      
        print("input:%d"%pir_input)
        #pwm.ChangeFrequency(1.0)
        if pir_input == 1:
            print("pir detect")
           # pwm.ChangeFrequency(50.0)
           # time.sleep(2.0)
            pir_input = 0



except KeyboardInterrupt:
    pass

gpio.cleanup()


