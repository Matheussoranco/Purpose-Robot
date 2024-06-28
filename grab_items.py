import RPi.GPIO as GPIO
from time import sleep

SERVO_PIN = 22
GPIO.setup(SERVO_PIN, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz

servo.start(0)

def grab_item():
    servo.ChangeDutyCycle(7)  # Ângulo para pegar
    sleep(1)

def release_item():
    servo.ChangeDutyCycle(12)  # Ângulo para soltar
    sleep(1)

# Simulação de pegar e soltar
try:
    while True:
        grab_item()
        sleep(2)
        release_item()
        sleep(2)
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
