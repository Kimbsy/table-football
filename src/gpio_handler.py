import RPi.GPIO as GPIO
import time

class GPIO_handler:

  """The GPIO_handler class is responsible for checking IR sensors and reset
  button inputs as well as setting LED outputs and updating the App's scores
  appropriately.
  """

  def __init__(self):

    # Define GPIO pin variables
    led_1 = 8
    led_2 = 12
    sensor_1 = 10
    sensor_2 = 7
    reset = 26

    # Set appropriate pin modes
    GPIO.setup(led_1, GPIO.OUT)
    GPIO.setup(led_2, GPIO.OUT)
    GPIO.setup(sensor_1, GPIO.IN)
    GPIO.setup(sensor_2, GPIO.IN)
    GPIO.setup(reset, GPIO.IN)

  def beam_broken(sensor):
    return not GPIO.input(sensor)

  def check_for_goals(app):
    if self.beam_broken(sensor_1):
      GPIO.output(led_1, True)
      app.scores[0] = app.scores[0] + 1
    else:
      GPIO.output(led_1, False)

    if self.beam_broken(sensor_2):
      GPIO.output(led_2, True)
      app.scores[1] = app.scores[1] + 1
    else:
      GPIO.output(led_2, False)

    if not GPIO.input(reset):
      app.scores[0] = 0
      app.scores[1] = 0
