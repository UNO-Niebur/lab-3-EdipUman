#RPS.py
#Name:Edip Uman
#Date:2/8/2026
#Assignment:Lab 03
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  playAgain = "Y"
  while playAgain == "Y": 
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.
    computer = random.choice (["R","P", "S"])
    print("R=Rock,P=Paper,S=Scissors")
    player = input("Make your choice, R,P,S")
    if computer == "R" :
      print("Computer decides to battle using Rock")
    elif computer == "P" :
      print("Computer decides to slam using Paper")
    elif computer == "S" :
      print("Computer decides to slice with Scissors")
    if player == "R" :
      print("Player decides to smash using Rock")
    elif player == "P" :
      print("Player decides to cut using Paper")
    elif player == "S" :
      print("Player decides to chop with Scissors")
    if player == "R" and computer == "R":
      print("Tie")
      ties = ties + 1
    if player == "P" and computer == "P":
      print("Tie")
      ties = ties + 1
    if player == "S" and computer == "S":
      print("Tie")
      ties = ties + 1
    if player == "R" and computer == "P":
      print("Computer Wins")
      losses = losses + 1
    if player == "P" and computer == "S":
      print("Computer Wins")
      losses = losses + 1
    if player == "S" and computer == "R":
      print("Computer Wins")
      losses = losses + 1
    if player == "R" and computer == "S":
      print("Player Wins")
      wins = wins + 1
    if player == "P" and computer == "R":
      print("Player Wins")
      wins = wins + 1
    if player == "S" and computer == "P":
      print("Player Wins")
      wins = wins + 1
  
    playAgain = input("Play Again? (Y/N): ")
  
  
  
    
  #In the end, print the stats
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
