import RPi.GPIO as GPIO

class GPIO_handler:

  """The GPIO_handler class is responsible for checking IR sensors and reset
  button inputs as well as setting LED outputs and updating the App's scores
  appropriately.

  RPi.GPIO documentation:
  http://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/
  """

  def __init__(self):

    # Define GPIO pin variables.
    self.led_1    = 8
    self.led_2    = 12
    self.sensor_1 = 10
    self.sensor_2 = 7
    self.reset    = 26

    # Set appropriate pin modes.
    GPIO.setup(self.led_1, GPIO.OUT)
    GPIO.setup(self.led_2, GPIO.OUT)
    GPIO.setup(self.sensor_1, GPIO.IN)
    GPIO.setup(self.sensor_2, GPIO.IN)
    GPIO.setup(self.reset, GPIO.IN)

  def beam_broken(self, sensor):
    return not GPIO.input(sensor)

  def reset_pressed(self):
    return not GPIO.input(self.reset)

  def check_for_goals(self, app):
    # Check sensor_1.
    if self.beam_broken(self.sensor_1):
      GPIO.output(self.led_1, True)
      app.scores[0] = app.scores[0] + 1
      return True
    else:
      GPIO.output(self.led_1, False)

    # Check sensor_2.
    if self.beam_broken(self.sensor_2):
      GPIO.output(self.led_2, True)
      app.scores[1] = app.scores[1] + 1
      return True
    else:
      GPIO.output(self.led_2, False)

    if self.reset_pressed():
      app.scores[0] = 0
      app.scores[1] = 0
      return True

    return False
