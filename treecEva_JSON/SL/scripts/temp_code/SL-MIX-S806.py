import heapq

def calculate_volatility_score(open_price, close_price, volume):
    price_change = abs(close_price - open_price)
    return price_change * (volume // 1000)

# Market data: (open_price, close_price, volume)
market_events = [
    (100.5, 105.2, 15000),
    (98.3, 97.8, 12000),
    (102.0, 101.5, 18000),
    (99.8, 103.4, 21000)
]

# Priority queue to store transactions: (-urgency_score, adjustment_value)
transaction_queue = []
initial_portfolio_value = 50000

for event in market_events:
    open_price, close_price, volume = event
    urgency_score = calculate_volatility_score(open_price, close_price, volume)
    adjustment_value = (close_price - open_price) * (volume // 100)
    heapq.heappush(transaction_queue, (-urgency_score, adjustment_value))

processed_adjustments = []
while transaction_queue:
    _, adjustment = heapq.heappop(transaction_queue)
    processed_adjustments.append(adjustment)

# Dynamic programming approach to find optimal subset of adjustments
n = len(processed_adjustments)
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(dp[i-1], dp[i-1] + processed_adjustments[i-1])

final_portfolio_value = initial_portfolio_value + dp[n]
print(f"Result: {final_portfolio_value}")