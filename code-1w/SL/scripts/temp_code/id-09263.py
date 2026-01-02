from collections import defaultdict

# Simulate hourly server load distribution over a day
time_slots = [f"hour_{i}" for i in range(24)]
base_loads = [120, 135, 150, 160, 180, 200, 220, 240, 300, 320, 310, 290, 280, 275, 285, 295, 305, 315, 300, 250, 200, 170, 140, 130]

load_distribution = defaultdict(int)
for hour, load in zip(time_slots, base_loads):
    load_distribution[hour] = load

# Apply dynamic scaling factor during peak business hours (9-11 and 13-15)
business_hours = ['hour_9', 'hour_10', 'hour_11', 'hour_13', 'hour_14']
scale_factor = 1.1
for slot in business_hours:
    load_distribution[slot] = int(load_distribution[slot] * scale_factor)

# Calculate average off-peak load (non-business hours)
off_peak_hours = [h for h in time_slots if h not in business_hours]
total_off_peak = sum(load_distribution[h] for h in off_peak_hours)
avg_off_peak = total_off_peak / len(off_peak_hours)

# Identify maximum observed load
peak_load = max(load_distribution.values())

# Print result for evaluation
print(f"Result: {peak_load}")