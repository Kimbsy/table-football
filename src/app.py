from gpio_handler import GPIO_handler
from announcer import Announcer
import time

class App:

  """The main App class holds the references to the Sensor_handler and Announcer
  objects as well as all the scores.
  """

  def __init__(self):
    self.GPIO_handler = GPIO_handler()
    self.announcer    = Announcer()
    self.scores       = [0, 0]
    self.paused       = False

  def start(self):
    while not self.paused:
      if self.GPIO_handler.check_for_goals(self):
        self.announcer.announce(self)
        time.sleep(1)
