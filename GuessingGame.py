class GuessingGame:

  isSolved = False
  feedbk = ""

  def __init__(self, answer):
    self.answer = answer
  
  def guess(self, user_guess):

    if (user_guess > self.answer):
      self.feedbk = "high"
    elif (user_guess < self.answer):
      self.feedbk = "low"
    else:
      self.feedbk = "correct"

    print(self.feedbk)

  def solved(self):
    if (self.feedbk == "correct"):
      self.isSolved = True
    
    return self.isSolved
