from application import app
from flask import render_template, request
from random import randrange
import requests
import csv


            
@app.route('/random', methods=['GET'])
def home():
    


    numb = randrange(1,6)
    points = numb
    return str(points)