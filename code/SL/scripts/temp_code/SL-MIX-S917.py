import math
from itertools import combinations

def tokenize_prices(raw_data):
    tokens = []
    for i in range(0, len(raw_data), 2):
        price_chunk = raw_data[i:i+2]
        if len(price_chunk) == 2:
            token_value = int(price_chunk[0]) * 10 + int(price_chunk[1])
            tokens.append(token_value)
    return tokens

def compute_log_returns(prices):
    log_returns = []
    for i in range(1, len(prices)):
        if prices[i-1] > 0 and prices[i] > 0:
            log_return = math.log(prices[i] / prices[i-1])
            log_returns.append(log_return)
    return log_returns

def adjust_volatility(returns, adjustment_factor=1.5):
    squared_returns = [r**2 for r in returns]
    avg_squared = sum(squared_returns) / len(squared_returns) if squared_returns else 0
    base_volatility = math.sqrt(avg_squared)
    return base_volatility * adjustment_factor

# Encoded market data representing stock prices
market_feed = "123456789012345"

# Tokenize the market data into price points
price_tokens = tokenize_prices(market_feed)

# Compute logarithmic returns between consecutive prices
log_returns_series = compute_log_returns(price_tokens)

# Calculate adjusted volatility with a scaling factor
adjusted_volatility = adjust_volatility(log_returns_series, 2.0)

print(f"Result: {round(adjusted_volatility, 4)}")