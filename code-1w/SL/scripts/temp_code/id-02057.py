from collections import defaultdict

# Simulate sensor readings over time
time_series_data = [23.5, 24.1, 23.8, 24.0, 23.6]

# Basic statistical analysis using defaultdict for frequency counting
freq_counter = defaultdict(int)
for val in time_series_data:
    freq_counter[round(val)] += 1

# Determine modal temperature (most frequent rounded value)
mode_temp = max(freq_counter, key=lambda x: freq_counter[x])

# Compute average temperature
avg_temp = sum(time_series_data) / len(time_series_data)

# Assess thermal stability based on variance threshold
variance = sum((x - avg_temp) ** 2 for x in time_series_data) / len(time_series_data)
is_stable = variance < 0.1

# Score computation using conditional expression
temperature_score = 95 if mode_temp == 24 else 85
fallback_score = 70
result = temperature_score if is_stable else fallback_score

print(f"Result: {result}")