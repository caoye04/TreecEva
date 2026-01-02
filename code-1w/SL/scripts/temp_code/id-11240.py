from collections import defaultdict

# Simulate daily transactions for a retail account over a week
daily_transactions = [
    [150, -75, 200, -50],       # Monday
    [100, -30, -45, 300],       # Tuesday
    [-80, 250, -120],            # Wednesday
    [400, -200, -60, -40],      # Thursday
    [120, -90, 500, -300]       # Friday
]

day_profit_map = defaultdict(float)
current_balance = 1000.0
peak_balance = current_balance
threshold_met = False

for i, transactions in enumerate(daily_transactions):
    day_profit = sum(transactions)
    day_profit_map[f'Day{i+1}'] = day_profit
    
    current_balance += day_profit
    
    if current_balance > 1500 and not threshold_met:
        threshold_met = True
    
    peak_balance = max(peak_balance, current_balance)

# Irrelevant utility: count total transaction days with net gain
total_positive_days = sum(1 for profit in day_profit_map.values() if profit > 0)

Result: peak_balance