from collections import defaultdict

# Simulate daily transactions for multiple accounts over a week
daily_transactions = [
    [100, -50, 25, -10],      # Day 0
    [-20, 30, -5, 40],       # Day 1
    [10, -15, 60, -20],      # Day 2
    [-30, 50, -10, 5],       # Day 3
    [20, -40, 70, -25],      # Day 4
    [5, 10, -8, 30],         # Day 5
    [-5, 20, -10, 15]        # Day 6
]

account_logs = defaultdict(list)
overall_total = 0
peak_balance = 0
current_balance = 0
transfer_buffer = 0
redundant_sum = 0

for day_idx, transactions in enumerate(daily_transactions):
    day_total = sum(transactions)
    overall_total += day_total
    
    # Process each transaction in the day
    for t in transactions:
        current_balance += t
        account_logs['balance_track'].append(current_balance)
        
        # Update peak only if positive fluctuation
        if current_balance > peak_balance:
            peak_balance = max(peak_balance, current_balance)
    
    # Distractor: simulate irrelevant buffer transfer logic
    if day_idx % 2 == 0:
        transfer_buffer += day_total * 0.1
    else:
        transfer_buffer -= day_total * 0.05

    # Dead code path – never affects peak_balance
    if day_idx > 10:
        fallback_recalc = sum(account_logs['balance_track']) // (day_idx + 1)
        redundant_sum += fallback_recalc

    # Extra computation with slicing that doesn't impact main logic
    recent_trends = account_logs['balance_track'][-3:] if len(account_logs['balance_track']) >= 3 else []
    if recent_trends:
        trend_change = recent_trends[-1] - recent_trends[0]
        # Unused variable
        smoothed_value = abs(trend_change) / 3

# Final adjustment unrelated to peak_balance
final_offset = len(account_logs['balance_track']) % 7
overall_total += final_offset

print(f"Result: {peak_balance}")