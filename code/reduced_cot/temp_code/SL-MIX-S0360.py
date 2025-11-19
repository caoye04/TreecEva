def calculate_max_profit(prices, fee):
    n = len(prices)
    if n <= 1:
        return 0
    
    # hold[i] represents max profit when holding stock at day i
    # sold[i] represents max profit when not holding stock at day i
    hold = [0] * n
    sold = [0] * n
    
    hold[0] = -prices[0]
    sold[0] = 0
    
    for i in range(1, n):
        # Either keep holding or buy today
        hold[i] = max(hold[i-1], sold[i-1] - prices[i])
        # Either keep not holding or sell today (with fee)
        sold[i] = max(sold[i-1], hold[i-1] + prices[i] - fee)
    
    return sold[n-1]

# Stock prices over 7 days
stock_prices = [10, 15, 8, 12, 9, 14, 7]
transaction_fee = 2

max_profit = calculate_max_profit(stock_prices, transaction_fee)
print(f'Result: {max_profit}')