import subprocess

class Announcer:
  """Announcer class is responsible for deciding what to say based on the App's
  scores.

  It has the ability to execute bash commands through the subprocess module.
  """

  def __init__(self):
    self.teams = ['team 1', 'team 2']

  def announce_goal(self, app):
    phrase = self.create_phrase(app.scores)
    self.output(phrase)

  def declare_winner(self, app):
    scores     = app.scores
    winner_idx = int(scores[1] > scores[0])

    score_phrase  = self.create_phrase(app.scores)
    winner_phrase = self.teams[winner_idx] + ' wins'

    self.output(score_phrase)
    self.output(winner_phrase)

  def announce_reset(self):
    self.output('game reset')

  def output(self, phrase):
    # self.speak(phrase)
    self.echo(phrase)

  def speak(self, phrase):
    subprocess.call(['espeak', phrase])

  def echo(self, phrase):
    subprocess.call(['echo', phrase])

  def create_phrase(self, scores):
    phrase = ''

    # Check if the scores are equal.
    if (scores[0] == scores[1]):
      phrase = phrase + str(scores[0]) + ' all'
      return phrase

    # Determine which team is in the lead.
    leader_idx = int(scores[1] > scores[0])

    # Construct 'X Y to TEAM' phrase.
    phrase = phrase + self.parse_score(scores, leader_idx) + ' ' + self.parse_score(scores, not leader_idx)
    phrase = phrase + ' to ' + self.teams[leader_idx]

    return phrase

  def parse_score(self, scores, idx):
    idx = int(idx)

    if scores[idx] == 0:
      score = 'nill'
    else:
      score = str(scores[idx])

    return score
