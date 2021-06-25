#!/bin/python3
from math import ceil

def f2(dist):
    return dist ** 1.435


dp_dict = {}

def dp(m1,m2,pos,draw_adv):
    if pos == 0:
        return (1,0)
    if pos == 10:
        return (0,0)
    if m1 == 0:
        if m2 >= 10-pos:
            return (0,0)
        return (1,0)
    if m2 == 0:
        return (1,1)

    su = m1 + m2 *1000 + pos *1000000 + draw_adv * 10000000
    if su in dp_dict:
        return dp_dict[su]
    
    can_win = 0
    winning_amt = 0
    min_losing = 1000
    for b1 in range(1,m1+1):
        can_win_b1 = 1
        loser = 0
        for b2 in range(1,m2+1):
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
            
            if res == 0:
                can_win_b1 = 0
                loser = b2
                break
        
        if can_win_b1 == 1:
            winning_amt = b1
            can_win = 1
        if can_win == 1:
            break
        if min_losing < loser:
            min_losing = loser
            winning_amt = b1
    
    dp_dict[su] = (can_win,winning_amt)
    return dp_dict[su]

def dp_bot(player,pos,first_moves,second_moves):
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
    


def calculate_bid(player,pos,first_moves,second_moves):
    dist = pos
    opp_dist = 10-pos
    if player == 2:
        first_moves, second_moves = second_moves, first_moves
        dist = 10 - pos
        opp_dist = pos
    my_money_spent  = 0
    his_money_spent = 0
    count = 0
    dc = 0
    for a,b in zip(first_moves, second_moves):
        count += 1
        if a > b:
            my_money_spent += a
            # print("i spent "+str(a))
        elif a < b:
            his_money_spent += b
        else:
            dc += 1
            if dc%2 == player%2:
                my_money_spent += a
                # print("i spent adv"+str(a))
            else:
                his_money_spent += b
            # draw_adv = 3 - player
                
    my_money_left = 100 - my_money_spent 
    his_money_left = 100 - his_money_spent
    amortized_bid = int(my_money_left / dist)
    force = [0,1,2,5,7,10,13,16,19]
    
    if my_money_left == 0:
        return 0
    
    bid = 0
    rate = 2
    minimum = 2
    coef = 0.065
    fraction = 0.45
    
    if dist == 1:
        # print(my_money_left)
        bid = my_money_left
        return bid
    elif dist == 9:
        if dc%2 == (player+1)%2:
            bid = his_money_left
        else:
            bid = his_money_left + 1
        return min(my_money_left,bid)
    else:
        # bid = ceil(min(fraction*my_money_left, coef * (rate ** dist)))
        bid = min(my_money_left,his_money_left) / f2(opp_dist) + (dc%2 != (player+1)%2)
    
    if count == 0:
        if player == 1:
            return 14
        else:
            return 15
    if count == 1:
        if dc%2 == (player+1)%2:
            return 13
        else:
            return 14

    # return min(my_money_left,max(minimum,bid))
    return max(1, min(my_money_left, int(round(bid))))


from math import ceil
import random

def calculate_bid2(player,pos,first_moves,second_moves):
    dist = pos
    if player == 2:
        first_moves, second_moves = second_moves, first_moves
        dist = 10 - pos
    my_money_spent  = 0
    his_money_spent = 0
    his_bids = 0
    draw_adv = 1
    count = 0
    dc = 0
    for a,b in zip(first_moves, second_moves):
        count += 1
        his_bids += b
        if a > b:
            my_money_spent += a
            print("i spent "+str(a))
        elif a < b:
            his_money_spent += b
        else:
            dc += 1
            if dc%2 ==1:
                print("player 1 draw adv")
            else:
                print("player 2 draw adv")
            if draw_adv == player:
                my_money_spent += a
                print("i spent "+str(a))
            else:
                his_money_spent += b
            draw_adv = 3 - player
                
    my_money_left = 100 - my_money_spent 
    his_money_left = 100- his_money_spent
    min_c = min(my_money_left,his_money_left)
    amortized_bid = int(his_money_left / (10-dist))
    print(his_money_left)
    print(dist)
    print(amortized_bid)
    print(my_money_left)
    
    if my_money_left <= 1:
        return my_money_left
    
    # bid = 0
#     rate = 2
#     minimum = 2
#     coef = 0.05
#     fraction = 0.5
    
    if dist == 1:
        return my_money_left
    elif dist == 9:
        if draw_adv == player:
            return his_money_left
        else:
            return (his_money_left + 1)
#     else:
#         bid = ceil(min(fraction*my_money_left, coef * (rate ** dist)))

#     return min(my_money_left,max(minimum,bid))
    print("here")
    bid = 0
    if count< 3:
        bid = random.randint(10,16)
    if count >=3 and count <=4:
        bid = random.randint(5,11)
    if count >4 and count <=6:
        if draw_adv == player:
            bid = int(his_bids/count) + 1
        else:
            bid = int(his_bids/count) + 2
    
    if bid != 0:
        return min(my_money_left,bid)

    print("final")
    print(my_money_left)
    
    return min(my_money_left,amortized_bid+2)
    
        

    

    

#gets the id of the player
player = int(input())

scotch_pos = int(input())         #current position of the scotch

first_moves = map(int, input().split())
second_moves = map(int, input().split())
bid = dp_bot(player,scotch_pos,first_moves,second_moves)
print(bid)