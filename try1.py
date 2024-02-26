import RPi.GPIO as GPIO
import time

# Define GPIO pin numbers
in1 = 17
in2 = 18
in3 = 22
in4 = 23
enA = 24
enB = 25

# Set up GPIO mode and configure pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enA, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)

# Create PWM objects
pwm_motor_a = GPIO.PWM(enA, 1000)
pwm_motor_b = GPIO.PWM(enB, 1000)

# Start PWM with 0% duty cycle (stopped)
pwm_motor_a.start(0)
pwm_motor_b.start(0)

def forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    pwm_motor_a.ChangeDutyCycle(80)
    pwm_motor_b.ChangeDutyCycle(80)

def backward():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    pwm_motor_a.ChangeDutyCycle(80)
    pwm_motor_b.ChangeDutyCycle(80)

def right():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    pwm_motor_a.ChangeDutyCycle(250)
    pwm_motor_b.ChangeDutyCycle(250)

def left():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    pwm_motor_a.ChangeDutyCycle(250)
    pwm_motor_b.ChangeDutyCycle(250)

def stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    pwm_motor_a.ChangeDutyCycle(0)
    pwm_motor_b.ChangeDutyCycle(0)

try:
    while True:
        left_sensor = GPIO.input(0)  # Replace with the actual pin numbers you are using
        right_sensor = GPIO.input(1)  # Replace with the actual pin numbers you are using

        if right_sensor == 0 and left_sensor == 0:
            forward()
        elif right_sensor == 0 and left_sensor == 1:
            right()
        elif right_sensor == 1 and left_sensor == 0:
            left()
        elif right_sensor == 1 and left_sensor == 1:
            stop()

except KeyboardInterrupt:
    stop()
    GPIO.cleanup()
