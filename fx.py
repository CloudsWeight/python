'''
OANDA API/Streaming currency rates


Author: N. Sepe / 
The MIT License (MIT)

Copyright (c) 2024 Clouds Weight

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import requests
import json 
from accts import accts
from secret import SECRET 
import argparse


class OandaApp():
	def __init__(self, token=None, account=None):
		self.BASE_URL ='https://api-fxtrade.oanda.com'
		if account is not None:
			self.account = {
					'URL':f'{self.BASE_URL}/v3/accounts', # Accounts Endpoint
					'acctId': account,
					'current':f'{account}'
					}
		self.account = {
					'URL':f'{self.BASE_URL}/v3/accounts', # Accounts Endpoint
					'acctId': accts,
					'current':f'{accts[0]}'
						}
		#if token is None:
			#self.token = SECRET
		self.token = token
		self.HEADER = { # Headers and Auth
					'Authorization': 'Bearer {}'.format(SECRET),
				} 
		self.ENDPOINT = { 
						'instruments':f'{self.BASE_URL}/v3/instruments/',
						'candles': f'{self.BASE_URL}/candles?',
						}
		self.instruments = {
					# CURRENCY PAIRS
					'URL':f'{self.BASE_URL}/v3/instruments/', 
					'current':'USD_JPY',
					'eurusd':'EUR_USD', 
					'usdjpy':'USD_JPY', 
					'usdchf':'USD_CHF', 
					}
		self.count = {
						'URL':'count=',
						'current':'3' # [default=500, maximum=5000] dont use with "FROM and TO"
						}
		self.candles = {'URL':'/candles?',
						'granularity':{
						'current':'&granularity=H4',
						'5s':'&granularity=S5',
						'5m':'&granularity=M5',
						'15m':'&granularity=M15',
						'1h':'&granularity=H1', 
						'4h':'&granularity=H4',
						'd':'&granularity=D',
						'w':'&granularity=W',
						'M':'&granularity=M',
						 },
					}
		self.current_url = (
			 f"{self.instruments['URL']}{self.instruments['current']}"
			 f"{self.candles['URL']}"
			 f"{self.count['URL']}{self.count['current']}"
			 f"{self.candles['granularity']['current']}"
			 				) # As Above So Below
	# Example:	https://api-fxtrade.oanda.com/v3/instruments/EUR_USD/candles?count=6&price=M&granularity=S5
	######################## methods, man
	def query_accounts(self, url=None, header=None):
		if header is None:
			header = self.HEADER
		if url is None:
			url = f"{self.account['URL']}"
		r = requests.get(url=url, headers=header)
		print(f"{r.status_code}, /n {r.content}")

	def query_account(self, url=None, header=None):
		if header is None:
			header = self.HEADER
		if url is None:
			url = f"{self.account['URL']}/{self.account['current']}"
			print(url)
		r = requests.get(url=url, headers=header)
		print(f"{r.status_code}")

	def query_rate(self, url=None, header=None):
		if header is None:
			header = self.HEADER
		if url is None:
			url = self.current_url
		#print(f"\nURL: {self.current_url}")
		r = requests.get(url=url, headers=header)
		#print(r.status_code)
		#print(r.content)
		return(r.content)

	def deserialize(self, bin_data=None):
		if json is None:
			print("must provide binary data")
		else:
			json_string = bin_data.decode('utf-8')
			json_data = json.loads(json_string)
			#print(json.dumps(json_data, indent=2))
		return json_data

	def update_current_url(self):
		self.current_url = (
					 f"{self.instruments['URL']}{self.instruments['current']}"
					 f"{self.candles['URL']}"
					 f"{self.count['URL']}{self.count['current']}"
					 f"{self.candles['granularity']['current']}"
					 )

	def set_rate(self, rate=None):
		if rate is None:
			print("No rate set no change made")
		rate = rate.lower()
		self.instruments['current'] = self.instruments[rate]
		print(f"new rate {self.instruments['current']}\n ")     
		self.update_current_url()

class Candlesticks():
	def __init__(self):
		self.fig, self.ax = plt.subplots()
		self.ohlc_data = []

	def fetch_data(self, data=None):
		if data is None:
			print("Failed to fetch_data")
		self.ohlc_data =[]
		print(data['candles'])
		#for candle in data['candles']:
		#	if 'mid' in candle:
		#		self.ohlc_data.append([[candle['time'], candle['mid']['o'], candle['mid']['h'],candle['mid']['l'],candle['mid']['c']]])
		return data
			 	
		

################## Enter the dragon
if __name__ == '__main__':
	app = OandaApp()
	rate_data = app.query_rate()
	print(json.dumps(app.deserialize(rate_data), indent=2))
	
	
