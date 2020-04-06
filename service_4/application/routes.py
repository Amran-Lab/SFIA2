from application import app
from flask import render_template, request
from random import randrange
from .pointclass import player
import requests

player1 = player('Greg')
number = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
@app.route('/work', methods=['GET'])
def home():
    
    
        
    picked = player1.getPicked()
    f_card = request.args.get('Card')
    #picked.append(f_card)
    while len(picked) < 52:
        card = requests.get('http://service_2:5001/random')
        if card.text not in picked:
            player1.addPicked(card.text)
            break
        else:
            pass
    
    
    pos = card.text.find(" ")
    new = card.text[0:pos]
    value_1 = number.index(f_card)
    value_2 = number.index(new)
    #value_1 = 1
    #value_2 = 2
    if value_2 > value_1:
        result = "Higher"
    elif value_2 < value_1:
        result = "Lower"
    else:
        result = "Same"


    value_get = request.args.get('Value')
    if result == 'Same':
        flag = True
    elif value_get == result:
        flag = True
    else:
        flag = False



    points = requests.get('http://service_3:5002/random')
    point = points.text

    if flag:
        bring = "You Guessed Correctly +" + point
    else:
        bring = "Sorry You Guessed Wrong -" + point

        
    
    
    
           
    

    # list1 = player.getPicked
    
    #return player1.name + " " + str(picked) + " first card " + f_card + " -- new card " + card.text + " -- The anser was " + result + " " +bring
    return player1.name +"," + str('-'.join(picked)) + "," + f_card + "," + card.text + "," + result + "," +bring

@app.route('/reset', methods=['GET'])
def resetPlayer():
    
    player1.emptyPicked()
    