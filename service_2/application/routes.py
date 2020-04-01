from application import app
from flask import render_template, request
from random import randrange
import requests
import csv

suit = ['Diamonds','Clubs','Spades','Heart']
number = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
cards = []
for i in suit:
        for j in number:
            str1 = j + ' of ' + i
            cards.append(str1)
            
@app.route('/random', methods=['GET'])
def home():
    


    numb = randrange(0,52)
    card = cards[numb]
    return card