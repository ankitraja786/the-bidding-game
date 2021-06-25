import random
from math import ceil

def botp(player,pos,first_moves,second_moves):

    bank = 100

    win = True
    first_wins = []
    for a, b in zip(first_moves, second_moves):
        if a == b:
            if win:
                first_wins.append(a)
            else:
                first_wins.append(0)
            win = not win
        elif a > b:
            first_wins.append(a)
        else:
            first_wins.append(0)
    fw = win

    win = False
    second_wins = []
    for a, b in zip(second_moves, first_moves):
        if a == b:
            if win:
                second_wins.append(a)
            else:
                second_wins.append(0)
            win = not win
        elif a > b:
            second_wins.append(a)
        else:
            second_wins.append(0)
    sw = win

    win = fw if player == 1 else sw
    tw = 0 if win else 1
  
    # money = []
    # money.append(bank - sum(x) for x in first_wins)
    # money.append(bank - sum(x) for x in second_wins)

    # my_money = money[player - 1]
    # their_money = money[player % 2]
    if player == 1:
      my_money = bank - sum(first_wins)
      their_money = bank - sum(second_wins)
    else:
      their_money = bank - sum(first_wins)
      my_money = bank - sum(second_wins)

    if my_money == 0:
        return 0
    # print(my_money)
    f = min(my_money, their_money)

    maxp = 9 if player == 1 else 1
    maxp0 = 10 if player == 1 else 0

    if maxp + pos == 10:
        return max(1, my_money)
    elif maxp == pos:
        return max(1, min(my_money, their_money + tw))

    pf = 0.9
    dist = abs(maxp0 - pos)
    fact = [(1 / (i ** pf)) for i in range(1, dist + 1)]
    coeff = sum(fact)
    mu = f / (coeff * (dist ** pf))
    mu += tw

    if len(first_moves) == 0:
        if player == 1:
            return 13
        else:
            return 14
    if len(first_moves) == 1:
        if win:
            return 12
        else:
            return 13

    return max(1, min(my_money, int(round(mu))))







#THE SIMULATOR CODE
player1=100
player2=100
first_moves=[]
second_moves=[]
pos=5
draw123=0
play1=1
play2=2
print("You want to go first or second?")
pid = int(input())
if pid == 1:
    while pos!=0 or pos!=10:
        # bid1=calculate_bid_player1(play1,pos,first_moves,second_moves)
        # bid2=calculate_bid_player2(play2,pos,first_moves,second_moves)
        print("Enter your bid?")
        bid1 = int(input())
        bid2=botp(2,pos,first_moves,second_moves)
        if bid1 > player1: 
            print("PLAYER 1 has made a wrong bet")
            print("PLAYER 2 BOT WINS")
            break
        if bid2 > player2: 
            print("PLAYER 2 BOT has made a wrong bet")
            print("PLAYER 1 WINS")
            break
        first_moves.append(int(bid1))
        second_moves.append(int(bid2))
        i=len(first_moves)-1
        if first_moves[i]>second_moves[i]:
            player1-=first_moves[i]
            pos-=1
        elif first_moves[i]<second_moves[i]:
            player2-=second_moves[i]
            pos+=1
        else:
            if draw123%2==0:
                player1-=first_moves[i]
                pos-=1
            else:
                player2-=second_moves[i]
                pos+=1
            draw123+=1
        print("Player1 Bid : ",first_moves[i],"\tPlayer1 Balance : ",player1)
        print("Player2 BOT Bid : ",second_moves[i],"\tPlayer2 BOT Balance : ",player2)
        print("Position : ",pos)
        print("")

        if pos==0:
            print("PLAYER 1 WINS")
            break
        if pos==10:
            print("PLAYER 2 BOT WINS")
            break
        if (player2>0 and second_moves[i]<=0) or second_moves[i]<0 or (second_moves[i]>player2+second_moves[i]):
            print("PLAYER 2 BOT has made a wrong bet")
            print("PLAYER 1 WINS")
            break
        if (player1>0 and first_moves[i]<=0) or first_moves[i]<0 or (first_moves[i]>player1+first_moves[i]):
            print("PLAYER 1 has made a wrong bet")
            print("PLAYER 2 BOT WINS")
            break
        if player1==0 and player2==0:
            print("Draw")
            break
elif pid == 2:
    while pos!=0 or pos!=10:
        # bid1=calculate_bid_player1(play1,pos,first_moves,second_moves)
        # bid2=calculate_bid_player2(play2,pos,first_moves,second_moves)
        print("Enter your bid?")
        bid2= int(input())
        bid1 = botp(1,pos,first_moves,second_moves)
        if bid1 > player1: 
            print("PLAYER 1 BOT has made a wrong bet")
            print("PLAYER 2 WINS")
            break
        if bid2 > player2: 
            print("PLAYER 2 has made a wrong bet")
            print("PLAYER 1 BOT WINS")
            break
        first_moves.append(int(bid1))
        second_moves.append(int(bid2))
        i=len(first_moves)-1
        if first_moves[i]>second_moves[i]:
            player1-=first_moves[i]
            pos-=1
        elif first_moves[i]<second_moves[i]:
            player2-=second_moves[i]
            pos+=1
        else:
            if draw123%2==0:
                player1-=first_moves[i]
                pos-=1
            else:
                player2-=second_moves[i]
                pos+=1
            draw123+=1
        print("Player1 BOT Bid : ",first_moves[i],"\tPlayer1 BOT Balance : ",player1)
        print("Player2 Bid : ",second_moves[i],"\tPlayer2 Balance : ",player2)
        print("Position : ",pos)
        print("")

        if pos==0:
            print("PLAYER 1 BOT WINS")
            break
        if pos==10:
            print("PLAYER 2 WINS")
            break
        if (player2>0 and second_moves[i]<=0) or second_moves[i]<0 or (second_moves[i]>player2+second_moves[i]):
            print("PLAYER 2 has made a wrong bet")
            print("PLAYER 1 BOT WINS")
            break
        if (player1>0 and first_moves[i]<=0) or first_moves[i]<0 or (first_moves[i]>player1+first_moves[i]):
            print("PLAYER 1 BOT has made a wrong bet")
            print("PLAYER 2 WINS")
            break
        if player1==0 and player2==0:
            print("Draw")
            break