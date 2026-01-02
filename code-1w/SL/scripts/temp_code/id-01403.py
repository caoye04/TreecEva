from collections import Counter

# Simulate sensor readings over time (e.g., temperature in tenths of °C)
readings = [235, 241, 235, 248, 250, 241, 235, 241, 241, 248]

# Count frequency of each reading
frequency_count = Counter(readings)

# Track rolling average for smoothing (basic signal processing)
cumulative_avg = sum(readings) / len(readings)
smoothed_peak = max(readings) - cumulative_avg

# Identify most frequently observed value
peak_frequency = max(frequency_count.values())

# Print final result
print(f"Result: {peak_frequency}")