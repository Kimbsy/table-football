import RPi.GPIO as GPIO
import time

led = 12
sensor_1 = 10

GPIO.setup(led, GPIO.OUT)
GPIO.setup(sensor_1, GPIO.IN)

# Loop continuously
while (True):

  # True indicates a beam break
  if GPIO.input(sensor_1):
    GPIO.output(led, False)
  else:
    GPIO.output(led, True)
