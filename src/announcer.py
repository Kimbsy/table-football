class Announcer:
  """Announcer class is responsible for deciding what to say based on the App's
  scores.
  """

  def announce(self, app):
    print(str(app.scores[0]) + ' - ' + str(app.scores[1]))
