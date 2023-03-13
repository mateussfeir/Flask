''' 
Flask course from Udemy.

 There are 5 most important HTTP words:
 POST : Add data
 GET : Retrieve Data
 DELETE : Remove Data
 PATCH : Update Data
 PUT : Replace Data

Data Formats: HTML and JSON

'''

from flask import Flask
import requests

app = Flask(__name__)
my_list = ['1', '2']

@app.route('/')
def test():
    return 'This works'

@app.route('/getticker', methods=['GET'])

def get_API():
    url = 'https://www.alphavantage.co/query'
    params = {'function': 'INCOME_STATEMENT',
            'symbol': 'TSLA',
            'apikey': 'TE1E1KD330UYLRHQ'}
    response = requests.get(url, params=params)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run()
