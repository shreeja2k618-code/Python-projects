player1=input("guess rock, scissor and paper for player 1:")
player2=input("guess rock, scissor and paper for player 2:")
if player1==player2:
  print("tie")
elif player1=="rock" and player2=="scissor":
    print("player 1 wins")
elif player1=="rock" and player2=="paper":
    print("player 2 wins")
elif player1=="paper" and player2=="scissor":
    print("player 2 wins")
elif player1=="scissor" and player2=="rock":
    print("player 2 wins")
elif player1=="paper" and player2=="rock":
    print("player 1 wins")
elif player1=="scissor" and player2=="paper":
    print("player 1 wins")