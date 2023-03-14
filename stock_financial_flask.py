''' 
Flask course from Udemy.

 There are 5 most important HTTP words:
 POST : Add data
 GET : Retrieve Data
 DELETE : Remove Data
 PATCH : Update Data
 PUT : Replace Data

Data Formats: HTML and JSON

Goal of this code:
Make a webpage where the user can choose the company and receive the data related to its financial statement
(Specially the revenue and profit)
'''

from flask import Flask
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/')
def test():
    return 'Welcome Here you can receive informatoins about TSLA'

@app.route('/price', methods=['GET'])

def get_API():
    url = 'https://www.alphavantage.co/query'
    params = {'function': 'TIME_SERIES_DAILY_ADJUSTED', 
            'symbol': 'TSLA',
            'apikey': 'TE1E1KD330UYLRHQ'}  
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    new_price = df.iloc[0]['4. close']
    return 'Price: ' + str(new_price)
    

if __name__ == '__main__':
    app.run(port=8080)

