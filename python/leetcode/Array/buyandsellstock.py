# Best time to busy and sell stock

def maxProfit(prices):
  minPrice = float("inf")
  maxProfit = 0
  
  for price in prices:
      if price < minPrice:
          minPrice = price
          
      profit = price - minPrice
      
      if profit > maxProfit:
          maxProfit = profit
          
  return maxProfit
  
result = maxProfit([7, 1, 5, 3, 6, 4])
print("PROFIT:", result)