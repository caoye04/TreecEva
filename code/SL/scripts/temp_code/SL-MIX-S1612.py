temperatures = [22.5, 24.0, 23.1, 25.3, 24.8]

# Quality check using short-circuit evaluation
valid_readings = all(-50 <= temp <= 70 for temp in temperatures)

# Calculate average if all readings are valid
avg_temp = sum(temperatures) / len(temperatures) if valid_readings else 0

print(f"Result: {avg_temp}")