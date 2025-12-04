# Weather monitoring system data analysis
temperatures = [22, 25, 19, 28, 31, 26, 24, 29, 27, 23]

# Analysis parameters
start_idx = 2
end_idx = 8
threshold = 25
max_temp = max(temperatures)
avg_temp = sum(temperatures) / len(temperatures)

# Count temperatures above threshold within selected range
filtered_count = sum(1 for temp in temperatures[start_idx:end_idx] if temp > threshold)

# Additional data processing
daily_variation = max_temp - min(temperatures)
above_avg = len([t for t in temperatures if t > avg_temp])

print(f"Result: {filtered_count}")