#RPS game

#taking 2 players-1 and 2
#if player1 is rock and player2 is paper,player2 wins
#if player1 is paper and player2 is scissor,player2 wins
#if player1 is scissor and player 2 is rock,player 2 wins

player1=input("player1's turn")
player2=input("player2's turn")
if (player1=="r" and player2=="p") or (player1=="p" and player2=="s") or ( player1=="s" and player2=="r") :
    print("player2 wins")
elif player1==player2:
    print("invalid")
else:
    print("player1 wins")
