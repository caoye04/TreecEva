from itertools import cycle

# Simulate daily work metrics over a 5-day week
daily_hours = [8.5, 7.2, 9.0, 6.5, 10.0]
errors_per_day = [1, 0, 2, 1, 3]
context_switches = [15, 18, 12, 20, 25]  # Distraction metric (semi-relevant)

# Derived productivity score with diminishing returns
productivity = sum(h ** 0.8 - 0.5 * e for h, e in zip(daily_hours, errors_per_day))

# Calculate fatigue as a function of long hours and context switches
fatigue = sum(1.2 ** max(0, h - 8) for h in daily_hours) + 0.05 * sum(context_switches)

# Risk factor based on error trend and overtime
error_trend = sum(1 for i in range(1, len(errors_per_day)) if errors_per_day[i] > errors_per_day[i-1])
overtime_days = sum(1 for h in daily_hours if h > 9)
risk_factor = error_trend * 2 + overtime_days * 1.5

# Irrelevant distraction: simulate screen lock events
lock_events = [len(str(int(h * 100))) for h in daily_hours]
phantom_metric = sum(lock_events) % 7  # Unused but plausible

# Helper function to assess performance with threshold logic
def evaluate_performance(prod, risk):
    base_score = prod * 10
    penalty = 0
    
    # Nested logic with short-circuiting
    if risk >= 5 or (risk >= 3 and prod < 35):
        penalty += 15
    elif risk >= 2:
        penalty += 5
    
    # Bonus for high productivity unless high risk
    if prod > 40 and not (risk >= 4):
        bonus = 10
    else:
        bonus = 0
    
    # Additional adjustment using itertools (moderate use)
    adjustments = [0.8, 1.0, 1.1]
    adj_cycle = cycle(adjustments)
    final_multiplier = sum(next(adj_cycle) for _ in range(len(daily_hours))) / len(daily_hours)
    
    return int((base_score - penalty + bonus) * final_multiplier)

# Misleading intermediate calculation (dead-end)
temporary_rank = "".join([chr(65 + min(int(h), 9)) for h in daily_hours])  # Creates string like 'IIIAJ'

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Result: {final_score}")