from application import app
from flask import render_template, request, session,redirect, url_for
import requests

app.secret_key = "super secret key"

@app.route('/', methods=['GET','POST'])
def home():

    card1 = requests.get('http://service_2:5001/random')
    card = card1.text
    
    
    if request.method == 'POST':

        
        card1 = session['Card']
        pos = card1.index(" ")
        new = card1[0:pos]
        l1 = card1.split(" ")
        
        
        number = l1[0]
        suit = l1[2]
        details=request.form
        value=details['Value']
        
        url = "http://service_4:5003/work?Card=" + number + "&Value=" + value
        query = requests.get(url)
        second = query.text
        session['Message'] = second + "," +  l1[0] + " "+ l1[1] + " "+l1[2]
        session.pop('Card', None)
        return redirect(url_for('home'))
    if 'Message' in session:
        message = session['Message'] + "," + card
    else:
        message = "First Card "+ card
        
    session.pop('Message', None)
    session['Card'] = card
    story = []
    try:
        
        story = formalise(message)
    except:
        
        story.append(message)
    return render_template('index.html', numb= message, story = story)
@app.route('/newgame', methods=['GET','POST'])
def newGame():
    session.pop('Message',None)
    session.pop('Card',None)
    reset = requests.get("http://service_4:5003/reset")
    
    return redirect(url_for('home'))

def formalise(string):
    st1 = string.split(',')                 #splits string by , to list
    name = st1[0]
    previous =st1[1]                      #turned to ace of spades-king of....
    value_of_first_card = st1[2]              #not useful
    guessed_card = st1[3]                  #when you pick higher/lower this the card you will be guessing against
    outcome = st1[4]          #actual outcome
    result = st1[5]                #wheter right or wrong
    first_card = st1[6]
    new_card = st1[7]
    previous_list = previous.split('-')        #gets previous cards into list
    new_list = [name,'-------------------','Previous Cards']
    for i in range(len(previous_list)):
        new_list.append(previous_list[i])
    new_list.append('-------------------')
    new_list.append('You Guessed')
    new_list.append(first_card)
    new_list.append('-------------------')
    new_list.append('Drawn Card')
    new_list.append(guessed_card)
    new_list.append('-------------------')
    new_list.append(result)
    new_list.append('-------------------')
    new_list.append('New Card')
    new_list.append(new_card)
    return new_list
