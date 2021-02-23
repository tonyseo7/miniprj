import RPi.GPIO as gpio
import threading
import queue
import time
import sys
 
NUM_MSG = 10
buzzQ = queue.Queue(NUM_MSG)
cameraQ = queue.Queue(NUM_MSG)
servoQ = queue.Queue(NUM_MSG)

def systemInit():
    gpio.setmode(gpio.BCM)

def pirSensorInit():
    pirPin = 14
    outputPin = 18

    gpio.setup(pirPin, gpio.IN)
    gpio.setup(outputPin, gpio.OUT)

    return pirPin


def buzzInit():
    
    #melody=[262, 294, 330, 349, 392, 440, 494, 523]
    buzzPin = 11
    gpio.setup(buzzPin, gpio.OUT)
    pwm = gpio.PWM(buzzPin, 1.0)
    pwm.start(1.0)
    """
    for i in range(0, 8):
        pwm.ChangeFrequency(melody[i])
        time.sleep(0.5)
        #gpio.output(buzzPin, detectFlag)
    pwm.stop()
    """
    return buzzPin, pwm




def pirThread(pirPin):
    sigVal = False

    while True:
        pirInput = gpio.input(pirPin)

        if pirInput == 1:
            print("PIR SENSEOR detect thread")
            sigVal=True
            buzzQ.put(sigVal)
            cameraQ.put(sigVal)
            servoQ.put(sigVal)
        else:
            startFlag = 0

def buzzThread(buzzPin, pwm):

    melody=[262, 294, 330, 349, 392, 440, 494, 523]

    detectFlag = False

    while True:
        detectFlag = buzzQ.get()
        if detectFlag == True:
            print("BUZZ thread")
            for i in range(0, 8):
                pwm.ChangeFrequency(melody[i])
                time.sleep(0.5)
            pwm.stop()
            

def cameraThread():
    detectFlag = False
    
    while True:
        detectFlag = cameraQ.get()
        if detectFlag == True:
            print("CAMERA thread")

def servoInit():
    servoPin=18
    gpio.setup(servoPin, gpio.OUT)
    pwm = gpio.PWM(servoPin, 50)
    pwm.start(0.1)

    return servoPin, pwm



def servoThread(servoPin, pwm):
    detectFlag = False

    while True:
        detectFlag = servoQ.get()
        if detectFlag == True:
            print("SERVO 90")
            pwm.ChangeDutyCycle(12.5)
            time.sleep(1.0)
        else:
            pwm.ChangeDutyCycle(0.1)
            time.sleep(1.0)




def main():
    systemInit()

    pirPin = pirSensorInit()
    buzzPin, buzz_pwm = buzzInit()
    servoPin, servo_pwm = servoInit()
    thread_pir = threading.Thread(target=pirThread,args=(pirPin,))
    thread_buzz = threading.Thread(target=buzzThread, args=(buzzPin, buzz_pwm))
    thread_camera = threading.Thread(target=cameraThread)
    thread_servo = threading.Thread(target=servoThread, args=(servoPin, servo_pwm))


    #t1 = time.time()
    thread_pir.start()
    thread_buzz.start()
    thread_camera.start()
    thread_servo.start()
    
    #t2 = time.time()

    thread_pir.join()
    thread_buzz.join()
    thread_camera.join()
    thread_servo.join()
    #psTime = t2-t1
    #print("Time:%f"%psTime)

if __name__ == "__main__":
    main()
