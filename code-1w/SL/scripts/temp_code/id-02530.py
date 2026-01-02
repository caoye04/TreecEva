from collections import defaultdict

# Simulate daily transactions across multiple accounts over a week
daily_transactions = [
    [100, -50, 200, -30],      # Day 0
    [-150, 500, -100, -40],    # Day 1
    [300, -200, 50, -60],      # Day 2
    [200, -180, 120, -80],     # Day 3
    [500, -400, 300, -150],    # Day 4
    [-100, 200, -90, 300],     # Day 5
    [400, -350, 100, -120]     # Day 6
]

account_stats = defaultdict(int)
buffer_cache = []
running_total = 0
temp_offset = 0

# Accumulate raw totals for performance baseline (irrelevant to final result)
for day_idx in range(len(daily_transactions)):
    temp_sum = sum(daily_transactions[day_idx])
    running_total += temp_sum
    buffer_cache.append(temp_sum * 0.1)  # Distractor: scaled and unused

# Track peak balance during reconstruction of account flow
base_reserve = 1000
recovery_point = None
peak_balance = base_reserve
consecutive_positive = 0
rollback_value = 0

for day_idx in range(len(daily_transactions)):
    current_balance = base_reserve
    
    # Process each transaction in the day
    for txn in daily_transactions[day_idx]:
        current_balance += txn
        account_stats['adjustments'] += 1  # Semi-relevant tracking
        
        # Update peak only at positive thresholds (distractor condition)
        if current_balance > peak_balance and current_balance > 1100:
            peak_balance = current_balance
    
    # Key logic: update peak regardless of threshold at end of each day
    peak_balance = max(peak_balance, current_balance)

    # Distractor: simulate recovery logic (never used)
    if current_balance < 900 and recovery_point is None:
        recovery_point = day_idx
        rollback_value = current_balance
    
    # Another distractor: modify temp_offset with irrelevant pattern
    temp_offset += len(daily_transactions[day_idx]) // 2

# Additional red herring computations
snapshot_log = daily_transactions[1:6:2]  # Sliced but unused
avg_adjustment = account_stats['adjustments'] / 7 if account_stats['adjustments'] else 0

# Final adjustment based on initial reserve and peak
final_metric = peak_balance - base_reserve + temp_offset

# Output the target variable as required
print(f"Target result: {peak_balance}")