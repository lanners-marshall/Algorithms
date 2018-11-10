#!/usr/bin/python

import argparse

def find_max_profit(prices):

  best_diff = 0

  for i in prices:
    for index, j in enumerate(prices):
      if i - j > best_diff:
        
        if index < prices.index(i):
          best_diff = i - j
  
  if best_diff == 0:
    best_diff = max(prices[1:]) - max(prices)
         
  return best_diff


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))