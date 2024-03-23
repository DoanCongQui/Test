from Motor import Motor
import RPi.GPIO as GPIO
from time import sleep

motor = Motor(17, 27, 22, 23, 24, 25)

motor.chay(speed=0.5, t=10)

        # Chay max 
#  motor.chay(speed=1, t=20)

motor.trai(speed=0.5, t=3)
#  motor.phai(speed=0.5, t=10)

#  motor.trai_tt(speed=0.5, t=10)
#  motor.phai_tt(speed=0.5, t=10)


try:
    # Rẽ trái trong 2 giây, sau đó trở lại vị trí ban đầu
    motor.trai_tt(speed=0.5, t=2)
    print("Turned left for 2 seconds.")

    sleep(2)  # Chờ 2 giây

    # Rẽ phải trong 2 giây, sau đó trở lại vị trí ban đầu
    motor.phai_tt(speed=0.5, t=2)
    print("Turned right for 2 seconds.")

finally:
    GPIO.cleanup()  # Dọn dẹp GPIO khi kết thúc chương trình
