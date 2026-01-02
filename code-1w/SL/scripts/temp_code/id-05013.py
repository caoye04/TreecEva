from collections import Counter

# Simulate hourly customer demand log from a retail store
entries = [
    'morning', 'morning', 'morning', 'morning',
    'lunch', 'lunch', 'lunch',
    'afternoon', 'afternoon',
    'dinner', 'dinner', 'dinner', 'dinner', 'dinner',
    'late_night'
]

demand_log = [hour for hour in entries if len(hour) > 5]

demand_counter = Counter(demand_log)

# Track peak demand across periods
peak_demand = max(demand_counter.values()) if demand_log else 0

# Irrelevant utility variable (minor distraction)
total_periods = len(set(demand_log))

Result: peak_demand