from collections import defaultdict

# Simulate sensor readings over time
sensor_data = [70, 75, 79, 81, 82, 85, 86, 84, 80]

# Track frequency of high temperatures
temp_freq = defaultdict(int)
for temp in sensor_data:
    if temp >= 80:
        temp_freq[temp] += 1

# Lambda to check if critical threshold has been frequently exceeded
exceeds_critical = lambda x: x > 83
frequent_high = sum(1 for t in temp_freq if exceeds_critical(t))

# Determine if sustained high temperature is detected
sustained_alert = len(temp_freq) > 4

# Irrelevant distraction: count even frequencies (not used in final logic)
even_counts = sum(1 for cnt in temp_freq.values() if cnt % 2 == 0)

# Main decision function
def temperature_filter(value):
    if value >= 85 and frequent_high >= 2:
        return 1
    elif sustained_alert:
        return 2
    else:
        return 0

final_check = temperature_filter(85)
threshold_alert = final_check + 1

print(f"Result: {threshold_alert}")