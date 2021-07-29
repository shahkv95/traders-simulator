import unittest
from client3 import getDataPoint, getDataPoint_calculatePriceBidGreaterThanAsk, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      test_stock = quote['stock']
      test_top_bid_price = quote['top_bid']['price']
      test_top_bid_size = quote['top_bid']['size']
      test_top_ask_price = quote['top_ask']['price']
      test_top_ask_size = quote['top_ask']['size']
      test_average = ((test_top_bid_price * test_top_bid_size) + (test_top_ask_price * test_top_ask_size))/(test_top_bid_size + test_top_ask_size)
      self.assertEqual(getDataPoint(quote), (test_stock, test_top_bid_price, test_top_ask_price,test_average))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      test_bid_price = float(quote['top_bid']['price'])
      test_ask_price = float(quote['top_ask']['price'])
      
      if (test_bid_price > test_ask_price):
        test_bid_price_greater_than_ask_price = test_bid_price 
        self.assertEqual(getDataPoint_calculatePriceBidGreaterThanAsk(quote),test_bid_price_greater_than_ask_price)

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_numerator_zero(self):
    """" When only numerator is zero """
    test_price_a = 0
    test_price_b = 1
    self.assertEqual(getRatio(test_price_a,test_price_b), 0)

  def test_getRatio_num_deno_non_zero(self):
    """ When both numerator and denominator are non-zero """
    test_price_a = 20
    test_price_b = 3
    self.assertEqual(getRatio(test_price_a, test_price_b), 6.67)

  def test_getRatio_denominator_zero(self):
    """" When only denominator is zero """
    test_price_a = 1
    test_price_b = 0
    self.assertIsNone(getRatio(test_price_a,test_price_b))

  def test_getRatio_num_deno_zero(self):
    """ When both numerator and denominator are zero """
    test_price_a = 0
    test_price_b = 0
    self.assertIsNone(getRatio(test_price_a, test_price_b))

if __name__ == '__main__':
    unittest.main()
