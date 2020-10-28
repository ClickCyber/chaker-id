from flask import Flask
import algo 

apps = Flask('Apps')

@apps.route('/')
def index():
    return 'Working'

@apps.route('/id/<card_id>')
def echo(card_id):
    if algo.id_chaker(card_id) == True:
        return {card_id:'True'}
    else:
        return {card_id:'False'}

apps.run(debug=True)
