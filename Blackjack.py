# BlackJack Extra Credit--Joseph Moreau
#Current Verison 4.0, Updated if anything other then a 1 or 2 entered for another card, gives an input error to contuine instead of crashing the code. added time and clear functions, added pyfiglet for a banner from docker lab. Also fixed game not ending if player gets 21 4-8-23
##Verison 3.0 Fixed the crash on the comparing the codes causing it to freeze and crash. under the while not is_game_over field.  3-31-23
#Verison 2.0 cleaned up the code. changed asked for another card y and n to 1 and 2 to stop spamming it. Added card Appending removing cards from the deck after put into a users hand. Need to clean up the terminal 3-24-23

#imports
import random
import os
import time
import pyfiglet

#defs

#Create a image when starting a new game. Docker lab, neat extra feature to try out
banner = pyfiglet.figlet_format("BlackJack!")


def clear():
  time.sleep(1)
  os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return a score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  elif 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw "
  elif computer_score == 0:
    return "Lost, opponent has Blackjack, maybe next time"
  elif user_score == 0:
    return "Congrats you have Blackjack!"
  elif user_score > 21:
    return "You went over. You lost "
  elif computer_score > 21:
    return "Opponent went over. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lost"

def play_game():
  clear()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21 or user_score == 21:
      is_game_over = True
    else:
      user_should_deal = input("Type '1' to get another card, type '2' to pass: ")
      if user_should_deal == "1":
        user_cards.append(deal_card())
      elif user_should_deal == "2":
        is_game_over = True
      else:
        print("Invalid input. Please input a '1' or a '2' to continue.")
        continue

      while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

      if computer_score != 0:
        while computer_score < user_score and computer_score < 21:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

  print(f"  Your final hand: {user_cards}, final score: {user_score}")
  print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


#replay
while input(f"{banner} Would you like to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  play_game()
