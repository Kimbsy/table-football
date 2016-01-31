from gpio_handler import GPIO_handler
from announcer import Announcer

class App:

  """The main App class holds the references to the Sensor_handler and Announcer
  objects as well as all the scores.
  """

  def __init__(self):
    self.GPIO_handler = new GPIO_handler()
    self.announcer    = new Announcer()
    self.scores       = [0, 0]
    self.paused       = False

  def start(self):
    while not self.paused:
      if self.GPIO_handler.check_for_goals(self)
        announcer.announce(self)
