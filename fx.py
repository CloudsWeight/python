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
#import argparse

class OandaApp():
	def __init__(self, token='', account=''):
		self.BASE_URL ='https://api-fxtrade.oanda.com'
		self.account = {
					'URL':f'{self.BASE_URL}/v3/accounts', # Accounts Endpoint
					'acctId': accts,
					'current':f'{accts[0]}'
						}
		self.token = SECRET
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
						'current':'&granularity=H1',
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
			 				)
# Expected Built URL: https://api-fxtrade.oanda.com/v3/instruments/EUR_USD/candles?count=6&price=M&granularity=S5
						
		self.query_url = f"{self.instruments['URL']}{self.instruments['current']}"

	def query_accounts(self, url=None, header=None):
		if header is None:
			header = self.HEADER
		if url is None:
			url = f"{self.account['URL']}{self.account['current']}"
		
		r = requests.get(url=url, headers=header)
		print(f"{r.status_code}, /n {r.content}")

	def query_rate(self, url=None, header=None):

		if header is None:
			header = self.HEADER
		if url is None:
			url = self.current_url
		print(self.current_url)
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
			print(json_data)

#                                                   

if __name__ == '__main__':
	app = OandaApp()
	raw_data = app.query_rate()
	app.deserialize(raw_data)

