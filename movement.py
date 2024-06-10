import RPi.GPIO as GPIO
from time import sleep

# Configuração dos pinos GPIO
GPIO.setmode(GPIO.BCM)
MOTOR_PIN1 = 17
MOTOR_PIN2 = 18
GPIO.setup(MOTOR_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_PIN2, GPIO.OUT)

def move_forward():
    GPIO.output(MOTOR_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)

def stop():
    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)

# Simulação de movimento
try:
    while True:
        # Move para frente por 2 segundos
        move_forward()
        sleep(2)
        stop()
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()