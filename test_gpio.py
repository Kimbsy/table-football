import RPi.GPIO as GPIO
import time

# Define gpio pin variables
led = 12
reset = 8
sensor_1 = 10

# Variables for scores
score_1 = 0
score_2 = 0

GPIO.setup(led, GPIO.OUT)
GPIO.setup(sensor_1, GPIO.IN)

def beam_broken(sensor):
  return not GPIO.input(sensor)

def print_scores():
  print(str(score_1) + ' - ' + str(score_2))

def check_for_goals():
  global score_1
  global score_2

  if beam_broken(sensor_1):
    GPIO.output(led, True)
    score_1 = score_1 + 1
    print_scores()
    time.sleep(1)
  else:
    GPIO.output(led, False)

#  if beam_broken(sensor_2):

# Loop continuously
while (True):
  check_for_goals()

