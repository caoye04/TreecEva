from itertools import zip_longest

# Simulate sensor readings from three monitoring stations over 4 time intervals
station_a = [87, 92, 85, 90]
station_b = [88, 90, 83]
station_c = [85, 88, 89, 87, 86]  # Extra reading (noise)

# Align readings using zip_longest, fill missing with previous valid value
filled_data = []
for a, b, c in zip_longest(station_a, station_b, station_c, fillvalue=None):
    last_valid = lambda x, prev: x if x is not None else prev
    row = []
    prev = 0
    for val in [a, b, c]:
        if val is not None:
            prev = val
        row.append(prev)
    filled_data.append(row)

# Compute average efficiency per time interval
interval_averages = [sum(interval)/len(interval) for interval in filled_data]

# Calculate rolling 2-interval efficiency using sliding window
rolling_efficiencies = []
for i in range(len(interval_averages) - 1):
    window_avg = (interval_averages[i] + interval_averages[i+1]) / 2
    rolling_efficiencies.append(round(window_avg, 2))

# Determine peak efficiency across rolling windows
peak_efficiency = max(rolling_efficiencies)

# Print result
print(f"Result: {peak_efficiency}")