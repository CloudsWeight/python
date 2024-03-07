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
from secret import SECRET as SECRET
#                                                                                                                              
#                                                                                   :                                          
#           .                             ,;                                       t#,     L.                     ,;           
#          ;W          j.               f#i                                       ;##W.    EW:        ,ft       f#i            
#         f#E GEEEEEEELEW,            .E#t             ..           ..       :   :#L:WE    E##;       t#E     .E#t  f.     ;WE.
#       .E#f  ,;;L#K;;.E##j          i#W,             ;W,          ,W,     .Et  .KG  ,#D   E###t      t#E    i#W,   E#,   i#G  
#      iWW;      t#E   E###D.       L#D.             j##,         t##,    ,W#t  EE    ;#f  E#fE#f     t#E   L#D.    E#t  f#f   
#     L##Lffi    t#E   E#jG#W;    :K#Wfff;          G###,        L###,   j###t f#.     t#i E#t D#G    t#E :K#Wfff;  E#t G#i    
#    tLLG##L     t#E   E#t t##f   i##WLLLLt       :E####,      .E#j##,  G#fE#t :#G     GK  E#t  f#E.  t#E i##WLLLLt E#jEW,     
#      ,W#i      t#E   E#t  :K#E:  .E#L          ;W#DG##,     ;WW; ##,:K#i E#t  ;#L   LW.  E#t   t#K: t#E  .E#L     E##E.      
#     j#E.       t#E   E#KDDDD###i   f#E:       j###DW##,    j#E.  ##f#W,  E#t   t#f f#:   E#t    ;#W,t#E    f#E:   E#G        
#   .D#j         t#E   E#f,t#Wi,,,    ,WW;     G##i,,G##,  .D#L    ###K:   E#t    f#D#;    E#t     :K#D#E     ,WW;  E#t        
#  ,WK,          t#E   E#t  ;#W:       .D#;  :K#K:   L##, :K#t     ##D.    E#t     G#t     E#t      .E##E      .D#; E#t        
#  EG.            fE   DWi   ,KK:        tt ;##D.    L##, ...      #G      ..       t      ..         G#E        tt EE.        
#  ,               :                        ,,,      .,,           j                                   fE           t          
#                                                                                                       ,                      
# curl -H "Authorization: Bearer 12345678900987654321-abc34135acde13f13530" https://api-fxtrade.oanda.com/v3/accounts
#
# dictionary of constants to call to build queries
const = {}
const['token']='' # API Toke 
const['headers']={ # Headers and Auth
					'Authorization': 'Bearer {}'.format(SECRET),
				} 
const['URL']='https://api-fxtrade.oanda.com' # BASE URL
const['accounts']='/v3/accounts' # Accounts Endpoint
const['accountId']=[ # Account Ids
					'1',
					'2',
					]
# Example of a built URL:
#                   "https://api-fxtrade.oanda.com/v3/instruments/EUR_USD/candles?count=6&price=M&granularity=S5"										
const['instruments']={  # CURRENCY PAIRS
					'eurusd':'EUR_USD', 
					'usdjpy':'USD_JPY',
					}
# OANDA GRANULARITY VALUES BELOW
# S5	5 second candlesticks, minute alignment
# S10	10 second candlesticks, minute alignment
# S15	15 second candlesticks, minute alignment
# S30	30 second candlesticks, minute alignment
# M1	1 minute candlesticks, minute alignment
# M2	2 minute candlesticks, hour alignment
# M4	4 minute candlesticks, hour alignment
# M5	5 minute candlesticks, hour alignment
# M10	10 minute candlesticks, hour alignment
# M15	15 minute candlesticks, hour alignment
# M30	30 minute candlesticks, hour alignment
# H1	1 hour candlesticks, hour alignment
# H2	2 hour candlesticks, day alignment
# H3	3 hour candlesticks, day alignment
# H4	4 hour candlesticks, day alignment
# H6	6 hour candlesticks, day alignment
# H8	8 hour candlesticks, day alignment
# H12	12 hour candlesticks, day alignment
# D	1 day candlesticks, day alignment
# W	1 week candlesticks, aligned to start of week
# M	1 month candlesticks, aligned to first day of the month
const['candles']={
					'granularity':{
						'5s':'S5',
						'5m':'M5',
						'15m':'M15',
						'1h':'H1', 
						'4h':'H4',
						'd':'D',
						'w':'W',
						'M':'M',
						 },
					'count': 1000, # [default=500, maximum=5000] dont use with FROM and TO

					} 
const['default_granularity']=const["candles"]["granularity"]["15m"]
const['default_count']=const['candles']['count']
# The RFC 3339 Date Time format for FROM and TO parameters 
# second header section
#headers = {'Authorization': 'Bearer %s' % const['token']}
# build query based off the defined constants 
const['built_URL']=const['URL']+const['accounts']
#
def build_url(url=const['built_URL'], headers=const['headers']):
	print(f"{url}\n{const['headers']}")
	r = requests.get(url=url, headers=headers)
	print(r.status_code)
	print(r.content)

#	
def check_const():
	for keys in const:
		print(f"{keys}: {const[keys]} \n") 
#
def query_url(url=const['built_URL']):
	if url == '':
		print("need data feed me grrrURL")
		return


if __name__ == "__main__":
	build_url()
