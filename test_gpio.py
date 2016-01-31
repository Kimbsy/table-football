import RPi.GPIO as GPIO
import time

# Define gpio pin variables
led_1 = 8
led_2 = 12
sensor_1 = 10
sensor_2 = 7
reset = 26

# Variables for scores
score_1 = 0
score_2 = 0

GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(sensor_1, GPIO.IN)
GPIO.setup(sensor_2, GPIO.IN)
GPIO.setup(reset, GPIO.IN)

def beam_broken(sensor):
  return not GPIO.input(sensor)

def print_scores():
  print(str(score_1) + ' - ' + str(score_2))

def check_for_goals():
  global score_1
  global score_2

  if beam_broken(sensor_1):
    GPIO.output(led_1, True)
    score_1 = score_1 + 1
    print_scores()
    time.sleep(1)
  else:
    GPIO.output(led_1, False)

  if beam_broken(sensor_2):
    GPIO.output(led_2, True)
    score_2 = score_2 + 1
    print_scores()
    time.sleep(1)
  else:
    GPIO.output(led_2, False)

  if not GPIO.input(reset):
    score_1 = 0
    score_2 = 0
    print_scores()
    time.sleep(1)


# Loop continuously
while (True):
  check_for_goals()

