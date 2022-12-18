import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

GIPHY_API_KEY = 'G56kYSMdcysRxLwAdvwcUSNjpFp0M0au'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    response = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={query}&limit=4')
    data = response.json()
    gifs = data['data']
    return render_template('home.html', gifs=gifs, query=query)

if __name__ == '__main__':
    app.run()
