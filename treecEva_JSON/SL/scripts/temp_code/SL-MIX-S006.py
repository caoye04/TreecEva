# Daily closing prices
prices = [100, 103, 101, 105, 108, 106, 110, 112]

# Step 1: Calculate daily returns
returns = []
for i in range(1, len(prices)):
    daily_return = prices[i] - prices[i-1]
    returns.append(daily_return)

# Step 2: Find longest positive streak
max_positive_streak = 0
current_streak = 0
for ret in returns:
    if ret > 0:
        current_streak += 1
        if current_streak > max_positive_streak:
            max_positive_streak = current_streak
    else:
        current_streak = 0

# Step 3: Calculate momentum score
positive_returns = [r for r in returns if r > 0]
if positive_returns:
    avg_positive = sum(positive_returns) / len(positive_returns)
    momentum_score = int(max_positive_streak * avg_positive * 10)
else:
    momentum_score = 0

# Step 4: Generate trading signal
if momentum_score > 50:
    trading_signal = 2  # Strong buy
elif momentum_score > 25:
    trading_signal = 1  # Buy
else:
    trading_signal = 0  # Hold

print(f"Result: {trading_signal}")