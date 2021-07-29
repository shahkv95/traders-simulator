################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

# Author - Kush Shah

import urllib.request
import time
import json
import random

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

def getDataPoint(quote):
	""" Produce all of the needed values to generate a datapoint """
	""" ------------- Update this function ------------- """
	stock = quote['stock']
	bid_price = float(quote['top_bid']['price'])
	bid_size = float(quote['top_bid']['size'])
	ask_price = float(quote['top_ask']['price'])
	ask_size = float(quote['top_ask']['size'])
	# Weighted average is considered for calculating the average price
	price = ((bid_price * bid_size) + (ask_price * ask_size)) / (bid_size + ask_size)
	return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
	""" Get ratio of price_a and price_b """
	""" ------------- Update this function ------------- """
	""" Also create some unit tests for this function in client_test.py """
	if(price_b!=0):
		ratio = round((price_a / price_b),2)
		return ratio

def getDataPoint_calculatePriceBidGreaterThanAsk(quote):
	""" Return the bid_price if greater than the ask price """
	bid_price = float(quote['top_bid']['price'])
	ask_price = float(quote['top_ask']['price'])
	if bid_price > ask_price:
		return bid_price
	return

# Main
if __name__ == "__main__":

	# Query the price once every N seconds.
	for _ in iter(range(N)):
		quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

		""" ----------- Update to get the ratio --------------- """
		stock_name_and_price = {}
		for quote in quotes:
			stock, bid_price, ask_price, price = getDataPoint(quote)
			stock_name_and_price[stock] = price
			print ("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

		print ("Ratio %s" % getRatio(stock_name_and_price['ABC'], stock_name_and_price['DEF']))
