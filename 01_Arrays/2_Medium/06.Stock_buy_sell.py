"""
QUESTION:-

You are given an array prices where prices[i] is the price of a stock
on the ith day.

Choose one day to buy and a different future day to sell.

Return the maximum profit that can be achieved.

If no profit is possible, return 0.

Example 1:
Input:
prices = [7, 1, 5, 3, 6, 4]

Output:
5

Explanation:
Buy at price 1 and sell at price 6.
Profit = 6 - 1 = 5.

Example 2:
Input:
prices = [7, 6, 4, 3, 1]

Output:
0
"""

"""
APPROACH:-

-> Maintain the minimum price seen so far.
-> For every current price, calculate the profit:
      current_price - minimum_price
-> Update the maximum profit.
-> Update the minimum price.

The important observation is that we only need the cheapest buying price
from all previous days.

This is the optimal solution for LeetCode 121.
"""

# CODE:-

def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0

    minimum_price = prices[0]
    best_profit = 0

    for price in prices[1:]:
        best_profit = max(best_profit, price - minimum_price)
        minimum_price = min(minimum_price, price)

    return best_profit


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
