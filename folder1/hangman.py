class Hangman:
  '''
  Fields:
     secret_word (Str)
     in_progress_word (Str)
     guessed_letter_hits (listof Str)
     guessed_letter_misses (listof Str)
     
     Requires: 
        in_progress_word and secret_word correspond to a valid Hangman pair
        guessed_letter_hits and guessed_letter_misses 
             contain only capital letters
        len(guessed_letter_misses) <= Hangman.max_strikes
  '''  
  max_strikes = 6
  max_word = 1000
  enter_game_number = \
  "Please enter a valid game number between 1 and {0}: ".format(max_word)
  invalid_game_number = "Error, the number entered was not valid."
  letter_prompt = "Please enter a letter: "
  not_a_letter = "The character {0} is not a letter."
  already_guessed_letter = \
  "You have already guessed the letter {0}. Please enter another letter."
  not_in_word = "The letter {0} is not in the word."
  not_last_guess = \
  "Watch out! You only have {0} more guesses left before your man is hung!"
  play_again = "Do you want to play again? (Y for yes, N for no)."
  invalid_play_again_response = "Error, invalid response."
  game_over = "Game over. The correct word was {0}."
  congratulations = "You win! The correct word was {0}."
  
  def __init__(self, word_number):
    self.secret_word = self.get_word(word_number)
    self.in_progress_word = ""
    for i in range(len(self.secret_word)):
      if self.secret_word[i].isspace():
        self.in_progress_word += " "
      else:
        self.in_progress_word += "_"
    self.guessed_letter_hits = []
    self.guessed_letter_misses = []
    
  
  def __repr__(self):
    '''
    Returns a string representation of self
  
    __repr__: Hangman -> Str
    '''
    fin = open("hangman_board.txt")
    L = fin.readlines()
    fin.close()
    start = len(self.guessed_letter_misses)
    board_length = 15
    return "".join(L[start*board_length:start*board_length+board_length])
  
  def __eq__(self, other):
    if other == self.secret_word:
      return True
    else:
      return False
    pass
  
  def get_word(self, n):
    '''
    Returns a secret word corresponding to entry n in a list.
  
    get_word: Nat -> Str
    Requires: 1 <= n <= Hangman.max_word
    '''
    fin = open("words.txt")
    L = fin.readlines()
    fin.close()
    return L[n].strip()
    
  def update_board(self, guess):
    gameover = False
    if guess not in self.secret_word.upper():
      self.guessed_letter_misses.append(guess)
      self.guessed_letter_misses.sort()
      print(self.not_in_word.format(guess))
      if len(self.guessed_letter_misses) == self.max_strikes:
        print(self.__repr__())
        print(self.in_progress_word)
        print(self.game_over.format(self.secret_word))
        gameover = True
      else:
        num_guess = self.max_strikes - len(self.guessed_letter_misses)
        print(self.not_last_guess.format(num_guess))
        print(self.__repr__())
        print(self.in_progress_word)
    else:
      flag = False
      for i in range(len(self.secret_word)):
        temp = self.secret_word[i].capitalize()
        if guess == temp:
          self.in_progress_word = self.in_progress_word[:i] + self.secret_word[i] + self.in_progress_word[i+1:]
          if not flag:
            self.guessed_letter_hits.append(guess)
            self.guessed_letter_hits.sort()
      print(self.__repr__())
      print(self.in_progress_word)
      if self.__eq__(self.in_progress_word):
        print(self.congratulations.format(self.secret_word))
        gameover = True
    return gameover



def play_game():
  word_number = int(input(Hangman.enter_game_number))
  while word_number < 1 or word_number > Hangman.max_word:
    word_number = int(input(Hangman.enter_game_number))
  hm = Hangman(word_number)
  print(hm.__repr__())
  print(hm.in_progress_word)
  flag = True
  while(flag):
    letter = input(hm.letter_prompt)
    if letter.isalpha() and len(letter) == 1:
      temp = []
      temp.extend(hm.guessed_letter_hits)
      temp.extend(hm.guessed_letter_misses)
      if letter.capitalize() in temp:
        print(hm.already_guessed_letter.format(letter.capitalize()))
      else:
        result = hm.update_board(letter.capitalize())
        if result:
          y = input(hm.play_again)
          if y.capitalize() == 'Y':
            play_game()
          elif y.capitalize() == 'N':
            flag = False
          else:
            print(hm.invalid_play_again_response)    
    else:
      print(hm.not_a_letter.format(letter))
      
  return None

play_game()