#Creating Rock,Paper,Scissor Using Python
print("Welcome To Rock Paper Scissor Game")
#Create Variable For Two Player
Times_Game=int(input("Enter Number Of Times Did You Want To Play With Each Other:"))
for a in range(1,Times_Game):
    Player1=int(input("Enter 1 For Rock\nEnter 2 For Paper\nEnter 3 For Scissor"))
    Player2=int(input("Enter 1 For Rock\nEnter 2 For Paper\nEnter 3 For Scissor"))
    if (Player1==1 and Player2==1):
        print("Both Are Same")
    elif (Player1==1 and Player2==2):
        print("Congratulations Player 2 Won Against Player1")
    elif (Player1==1 and Player2==3):
        print("Congratulations Player 1 Won Against Player2")
    elif (Player1==2 and Player2==2):
        print("Both Are Same")
    elif (Player1==2 and Player2==1):
        print("Congratulations Player 1 Won Against Player2")
    elif (Player1==2 and Player2==3):
        print("Congratulations Player 2 Won Against Player1")
    elif (Player1==3 and Player2==1):
        print("Congratulations Player 2 Won Against Player1")
    elif (Player1==3 and Player2==3):
        print("Both Are Same")
    elif (Player1==3 and Player2==2):
        print("Congratulations Player 1 Won Against Player2")