#
#	Alex Donnan
#	IFT458 - 
#

import urllib.request
import json

api_key = 'ALVKRT756BLLGZ2H'
api_url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='

def main():
	user_input = ''
	while (user_input != 'quit'):
		user_input = input('Enter a stock symbol or quit: ')
		if (user_input != 'quit'):
			stock_result = getStockData(user_input)
			stock_json = json.loads(stock_result)
			if 'Global Quote' in stock_json:
				print(stock_result)
				print('The current price of ' + stock_json['Global Quote']['01. symbol'] + ' is: ' + stock_json['Global Quote']['05. price'])
			if 'Error Message' in stock_json:
				print('Please enter a vaild stock symbol')


def getStockData(symbol):
	modified_url = api_url + symbol + '&apikey=' + api_key
	connection = urllib.request.urlopen(modified_url)
	responseString = connection.read().decode()

	return responseString

main()