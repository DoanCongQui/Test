import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
    def __init__(self, EnaA, In1A, In2A, EnaB, In1B, In2B):
    # def __init__(self, EnaA, In1A, In2A):
        # Dong co banh sau 
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A

        # Dong co banh truoc 
        self.EnaB = EnaB
        self.In1B = In1B
        self.In2B = In2B

        GPIO.setup(self.EnaA, GPIO.OUT)
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)
        GPIO.setup(self.EnaB, GPIO.OUT)
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)

        self.pwmA = GPIO.PWM(self.EnaA, 100)
        self.pwmB = GPIO.PWM(self.EnaB, 100)
        self.pwmA.start(0)
        self.pwmB.start(0)

    # Ham chay toi
    def chay(self, speed=0.5, t=0):
        GPIO.output(self.In1A, GPIO.LOW)
        GPIO.output(self.In2A, GPIO.HIGH)
        self.pwmA.ChangeDutyCycle(speed * 100)

        # Dung dong co
        sleep(t)
        self.pwmA.ChangeDutyCycle(0)

    # Ham chay lui
    def lui(self, speed=0.5, t=0):
        GPIO.output(self.In1A, GPIO.HIGH)
        GPIO.output(self.In2A, GPIO.LOW)
        self.pwmA.ChangeDutyCycle(speed * 100)

        # Dung dong co
        sleep(t)
        self.pwmA.ChangeDutyCycle(0)

    # Ham re trai
    def trai(self, speed=0.5):
        GPIO.output(self.In1B, GPIO.HIGH)
        GPIO.output(self.In2B, GPIO.LOW)
        self.pwmB.ChangeDutyCycle(speed * 100)

    # Ham re phai
    def phai(self, speed=0.5):
        GPIO.output(self.In1B, GPIO.LOW)
        GPIO.output(self.In2B, GPIO.HIGH)
        self.pwmB.ChangeDutyCycle(speed * 100)



    # Demo mo cu dong cua 
    def trai_tt(self, speed=0.5, t=2):
        GPIO.output(self.In1B, GPIO.HIGH)
        GPIO.output(self.In2B, GPIO.LOW)
        
        for i in range(0, int(speed*100), 5):
            self.pwmB.ChangeDutyCycle(i)
            sleep(t / (speed*100))

        # Dung dong co
        sleep(t)
        self.pwmB.ChangeDutyCycle(0)

    def phai_tt(self, speed=0.5, t=2):
        GPIO.output(self.In1B, GPIO.LOW)
        GPIO.output(self.In2B, GPIO.HIGH)
        
        for i in range(0, int(speed*100), 5):
            self.pwmB.ChangeDutyCycle(i)
            sleep(t / (speed*100))

        # Dung dong co
        sleep(t)
        self.pwmB.ChangeDutyCycle(0)
