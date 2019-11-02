from GuessingGame import GuessingGame
from random import randint

def main():
  isSolved = False
  lives = 0
  game = GuessingGame(randint(1,10))

  while (not isSolved):
    user_guess = input("Guess a number between 1-10: ")
    game.guess(user_guess)
    isSolved = game.solved()
    lives += 1

    if (lives == 3):
      print("Game Over")
      isSolved = True



if __name__ == '__main__':
  main()