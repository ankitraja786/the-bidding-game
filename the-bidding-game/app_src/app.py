from flask import Flask,flash,render_template,request,session
from math import ceil

app = Flask(__name__)
app.config["SECRET_KEY"] = "zkmbdsedrqdsamdlsdmfsldsmkdd"

def f2(dist):
    return dist ** 1.435


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


# @app.route('/handle_data', methods=['POST'])
# def handle_data():
#     bid = request.form['bid']
#     print("here")
#     print(bid)
#     # your code
#     # return a response

def restart_game():
    session['player1_bids'] = []
    session['player2_bids'] = []
    session['bottle_pos'] = 5
    session['draw_counts'] = 0
    session['player1_money'] = 100
    session['player2_money'] = 100
    session['duration'] = 0
    session.modified = True

def first_time_start():
    if "player1_bids" not in session:
        session["player1_bids"] = []
    if "player2_bids" not in session:
        session["player2_bids"] = []
    if "bottle_pos" not in session:
        session["bottle_pos"] = 5
    if "draw_counts" not in session:
        session["draw_counts"] = 0
    if "player1_money" not in session:
        session["player1_money"] = 100
    if "player2_money" not in session:
        session["player2_money"] = 100
    if "duration" not in session:
        session["duration"] = 0


def find_min_and_max_p1(p1_bal):
    if p1_bal== 0:
        return 0, 0
    else:
        return 1, p1_bal

def calculate_bots_bid():
    return 13

def update_session_vars(player1_bid,player2_bid):
    session['duration'] += 1
    session['player1_bids'].append(player1_bid)
    session['player2_bids'].append(player2_bid)
    deduct_1 = True
    if player1_bid > player2_bid:
        deduct_1 = True
    elif player1_bid < player2_bid:
        deduct_1 = False
    else:
        if session['draw_counts']%2 == 0:
            deduct_1 = True
        else:
            deduct_1 = False
        session['draw_counts'] += 1
    
    if deduct_1:
        session['player1_money'] -= player1_bid
        session['bottle_pos'] -= 1
    else:
        session['player2_money'] -= player2_bid
        session['bottle_pos'] += 1

    session.modified = True

def calculate_bots_bid():
    return calculate_bid(2,session['bottle_pos'],session['player1_bids'],session['player2_bids'])





@app.route('/', methods= ["GET", "POST"])
def homepage():
    flash("flash test!!!!")
    first_time_start()
    if request.method == 'POST':
        if request.form.get('start_button') == 'Restart':
            restart_game()
            return render_template('index.html',duration=0,p1_bal=100,p2_bal=100,new_pos = 5, min_bid = 1, max_bid = 100)
        player1_bid = request.form.get('bid')
        if player1_bid:
            player1_bid = int(player1_bid)
            bid2 = calculate_bots_bid()
            update_session_vars(player1_bid,bid2)
            new_pos = session['bottle_pos']
            p1_bal = session['player1_money']
            p2_bal = session['player2_money']
            mini, maxi = find_min_and_max_p1(p1_bal)
            duration = session['duration']
            message = ""
            if new_pos == 0:
                message += "Player 1 Won!!"
                # restart_game()
                # return render_template('index.html',message=message,duration=0,p1_bal=100,p2_bal=100,new_pos = 5, min_bid = 1, max_bid = 100)
                #player1 won restart render

            if new_pos == 10:
                message += "Player 2 Won"
                # restart_game()
                # return render_template('index.html',message=message,duration=0,p1_bal=100,p2_bal=100,new_pos = 5, min_bid = 1, max_bid = 100)
                #player2 won restart render

            return render_template('index.html',message=message,duration=duration,p1_bal=p1_bal,p2_bal=p2_bal,new_pos = new_pos,bid1=player1_bid,bid2=bid2,min_bid = mini, max_bid = maxi)
        else:
            flash('Only non-zero bids are allowed.')
            return render_template('index.html')

    return render_template('index.html',duration=0,p1_bal=100,p2_bal=100,new_pos = 5, min_bid = 1, max_bid = 100)



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
