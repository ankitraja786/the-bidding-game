import random
from math import ceil
#ALL IMPORT STATEMENTS HERE

def f2(dist):
    return dist ** 1.435

dp_dict = {}

def dp(m1,m2,pos,draw_adv):
    if pos == 0:
        return (2,0)
    if pos == 10:
        return (0,0)
    if m1 == 0:
        if m2 >= 10-pos:
            return (0,0)
        return (1,0)
    if m2 == 0:
        if m1>=pos:
            return (2,1)
        return (1,1)

    su = m1 + m2 *1000 + pos *1000000 + draw_adv * 10000000
    if su in dp_dict:
        return dp_dict[su]
    
    state = 0
    winning_amt = 0
    # min_losing = 1000
    min_win_or_draw = 1000
    for b1 in range(1,m1+1):
        # can_win_b1 = 1
        zero_c = 0
        one_c = 0
        two_c = 0
        tc = 0
        loser = 0
        for b2 in range(1,m2+1):
            tc += 1
            res = 0
            if b1<b2:
                res = dp(m1,m2-b2,pos+1,draw_adv)[0]
            elif b1>b2:
                res = dp(m1-b1,m2,pos-1,draw_adv)[0]
            else:
                if draw_adv == 0:
                    res = dp(m1-b1,m2,pos-1,1)[0]
                else:
                    res = dp(m1,m2-b2,pos+1,0)[0]
            
            # if res == 0:
            #     can_win_b1 = 0
            #     loser = b2
            #     break
            if res == 0:
                zero_c += 1
            elif res == 1:
                one_c += 1
            else:
                two_c += 1
        
        # if can_win_b1 == 1:
        #     winning_amt = b1
        #     can_win = 1
        # if can_win == 1:
        #     break
        # if min_losing < loser:
        #     min_losing = loser
        #     winning_amt = b1
        if two_c == tc:
            dp_dict[su] = (2,b1)
            return dp_dict[su]
        if two_c+one_c == tc:
            if b1<min_win_or_draw:
                min_win_or_draw = b1
                state = 1
            
    if state == 0:
        amt = min(m1,m2)/f2(10-pos) + (draw_adv)
        amt = int(round(amt))
        dp_dict[su] = (0,amt)
        return dp_dict[su]
    
    dp_dict[su] = (1,min_win_or_draw)
    return dp_dict[su]
        
    # dp_dict[su] = (can_win,winning_amt)
    # return dp_dict[su]

def calculate_bid_player1(player,pos,first_moves,second_moves):
    draw_adv = 0
    m1, m2 = 100,100
    for a,b in zip(first_moves, second_moves):
        if a<b:
            m2 -= b
        elif a>b:
            m1 -= a
        else:
            if draw_adv == 0:
                m1 -= a
            else:
                m2 -= b
            draw_adv = 1 - draw_adv

    if player == 1:
        a,b = dp(m1,m2,pos,draw_adv)
        # print("can win "+ str(a))
        return b
    else:
        a,b = dp(m2,m1,10-pos,1-draw_adv)
        # print("can win"+str(a))
        return b
        

def calculate_bid_player2(player,pos,first_moves,second_moves):        
    #PLAYER 2 BOT HERE
    # import random

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
while pos!=0 or pos!=10:
	bid1=calculate_bid_player1(play1,pos,first_moves,second_moves)
	bid2=calculate_bid_player2(play2,pos,first_moves,second_moves)
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
	print("Player2 Bid : ",second_moves[i],"\tPlayer2 Balance : ",player2)
	print("Position : ",pos)
	print("")

	if pos==0:
		print("PLAYER 1 WINS")
		break
	if pos==10:
		print("PLAYER 2 WINS")
		break
	if (player2>0 and second_moves[i]<=0) or second_moves[i]<0 or (second_moves[i]>player2+second_moves[i]):
		print("PLAYER 2 has made a wrong bet")
		print("PLAYER 1 WINS")
		break
	if (player1>0 and first_moves[i]<=0) or first_moves[i]<0 or (first_moves[i]>player1+first_moves[i]):
		print("PLAYER 1 has made a wrong bet")
		print("PLAYER 2 WINS")
		break
	if player1==0 and player2==0:
		print("Draw")
		break