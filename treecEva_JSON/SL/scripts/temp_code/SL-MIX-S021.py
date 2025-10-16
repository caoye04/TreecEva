from statistics import median

daily_gains = [120, -50, 300, 0, -20, 150, 75]
sorted_gains = sorted(daily_gains)
median_gain = median(sorted_gains)

print(f"Result: {median_gain}")