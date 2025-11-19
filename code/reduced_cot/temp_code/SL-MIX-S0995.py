import heapq
from collections import defaultdict

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate) ** time

currency_rates = {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.0}
initial_capital = 10000
transaction_queue = [
    (-500, 'USD', 0.02),   # Priority, currency, interest_rate
    (-1200, 'EUR', 0.015),
    (-800, 'GBP', 0.018),
    (-2000, 'JPY', 0.012)
]

# Convert to max heap by negating priorities
heapq.heapify(transaction_queue)

portfolio = defaultdict(float)
portfolio['USD'] = initial_capital

# Lambda to filter significant transactions
is_significant = lambda amount: abs(amount) > 600

processing_steps = 0
while transaction_queue and processing_steps < 3:
    neg_amount, currency, rate = heapq.heappop(transaction_queue)
    amount = -neg_amount
    
    # Short-circuit evaluation
    if is_significant(amount) and currency in currency_rates:
        converted_amount = amount / currency_rates[currency]
        portfolio[currency] += calculate_compound_interest(converted_amount, rate, 2)
    elif currency in currency_rates:  # Only process if currency is valid
        converted_amount = amount / currency_rates[currency]
        portfolio[currency] += converted_amount
    
    processing_steps += 1

# Merge portfolios using dictionary comprehension
base_values = {k: v*0.95 for k, v in portfolio.items() if v > 0}
bonus_values = {k: v*0.05 for k, v in portfolio.items() if v > 1000}

# Divide and conquer approach to merge
for k in bonus_values:
    base_values[k] = base_values.get(k, 0) + bonus_values[k]

final_portfolio_value = sum(base_values.values())
print(f"Result: {int(final_portfolio_value)}")