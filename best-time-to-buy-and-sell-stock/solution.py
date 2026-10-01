def max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


# Test Case 1 - Typical case
prices = [7, 1, 5, 3, 6, 4]
print("Test Case 1:", max_profit(prices))

# Test Case 2 - Edge case
prices = [7, 6, 4, 3, 1]
print("Test Case 2:", max_profit(prices))