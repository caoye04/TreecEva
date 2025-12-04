def fibonacci(n):
    # Helper function that calculates Fibonacci numbers
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def analyze_trend(data):
    # Analyze trend direction (not used in final calculation)
    uptrends = 0
    downtrends = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            uptrends += 1
        else:
            downtrends += 1
    return uptrends - downtrends

def calculate_profit(prices, investment):
    # Calculate profit based on price differences
    buy_price = prices[0]
    sell_price = prices[-1]
    
    # Calculate market volatility (not used in final calculation)
    volatility = sum(abs(prices[i] - prices[i-1]) for i in range(1, len(prices)))
    
    # Calculate transaction fees based on position in Fibonacci sequence
    fee_multiplier = fibonacci(4) / 10  # 3/10 or 0.3
    transaction_fee = investment * fee_multiplier / 100
    
    # Calculate profit percentage
    profit_percentage = ((sell_price - buy_price) / buy_price) * 100
    
    # Potential alternative strategy (distraction)
    alternative_profit = 0
    for i in range(len(prices) - 1):
        daily_change = prices[i+1] - prices[i]
        alternative_profit += daily_change
    
    # Calculate actual profit
    shares_bought = investment / buy_price
    gross_profit = shares_bought * (sell_price - buy_price)
    net_profit = gross_profit - transaction_fee
    
    return round(net_profit, 2)

# Historical price data
price_history = [105.42, 107.89, 106.33, 108.76, 110.42, 112.30, 115.75, 114.82, 116.43, 118.90, 
                120.15, 119.80, 121.35, 124.75, 123.42, 125.30, 127.45, 129.80]

# Initial parameters
initial_investment = 5000
trading_days = len(price_history)

# Market sentiment analysis (distraction)
market_mood = "bullish" if analyze_trend(price_history) > 0 else "bearish"
sentiment_score = len([p for p in price_history if p > price_history[0]])

# Calculate moving averages (distraction)
short_ma = sum(price_history[10:15]) / 5
long_ma = sum(price_history[5:15]) / 10

# Execute the trade and calculate profit
final_profit = calculate_profit(price_history[5:15], initial_investment)

print(f"Result: {final_profit}")