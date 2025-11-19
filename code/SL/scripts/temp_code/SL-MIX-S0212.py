from functools import reduce
from collections import defaultdict

# Daily market signals for portfolio adjustments
daily_signals = [3, -1, 4, -2, 5, -3, 2]

# Initialize adjustment tracking
adjustment_history = defaultdict(int)
total_impact = 0
final_adjustment_score = 0

# Process each signal with dynamic programming approach
for idx, signal in enumerate(daily_signals):
    # Greedy adjustment based on previous day's impact
    if idx > 0 and adjustment_history[idx-1] > 0:
        adjustment = signal * 2 if signal > 0 else signal
    else:
        adjustment = signal
    
    # Apply short-circuit logic for risk management
    is_high_risk_day = signal < 0 and (idx > 0 and daily_signals[idx-1] > 0)
    adjusted_signal = adjustment if not is_high_risk_day else adjustment // 2
    
    # Update history and accumulate impact
    adjustment_history[idx] = adjusted_signal
    total_impact += adjusted_signal

# Calculate final adjustment score using functional reduction
final_adjustment_score = reduce(lambda acc, val: acc + (val if val > 0 else -val * 2), adjustment_history.values(), 0)

# Apply final risk adjustment using logical operations
if total_impact > 10 and not (len(daily_signals) % 2 == 0 or total_impact < 15):
    final_adjustment_score *= 2

print(f"Result: {final_adjustment_score}")