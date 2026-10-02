# Best Time to Buy and Sell Stock

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Problem

Given an array of stock prices, choose one day to buy a stock and a later day to sell it to get the maximum possible profit.

If no profit can be made, return 0.

## Approach

I keep track of the minimum price seen so far.

For each price:
- Check whether it is lower than the current minimum price.
- Calculate the profit by subtracting the minimum price from the current price.
- Update the maximum profit if the current profit is higher.
- The stock must be bought before it is sold.

## Time Complexity

O(n)

## Space Complexity

O(1)

## Test Cases

### Test Case 1 - Typical Case

Input:
```text
prices = [7, 1, 5, 3, 6, 4]
```

Output:
```text
5
```

### Test Case 2 - Edge Case

Input:
```text
prices = [7, 6, 4, 3, 1]
```

Output:
```text
0
```

## Notes / Edge Cases

- The buying day must come before the selling day.
- If prices continuously decrease, no profit can be made.
- In that case, the answer is 0.

## Learning Notes

I learned how to find the maximum profit by keeping track of the minimum price and calculating the profit for each day.