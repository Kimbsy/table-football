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
      # Wait for a goal to be scored.
      if self.GPIO_handler.check_for_goals(self):

        # Check if a team has won.
        if max(self.scores) >= 3:
          self.announcer.declare_winner(self)
          self.reset_scores(False)
        else:
          self.announcer.announce_goal(self)
          # wait a second.
          time.sleep(1)

  def reset_scores(self, announce):
    self.scores = [0, 0]
    if announce:
      self.announcer.announce_reset()
    time.sleep(1)
