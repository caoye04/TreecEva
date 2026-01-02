from itertools import compress

# Sensor data validation and scoring
raw_readings = [105, 92, 110, 87, 96, 113, 89]
validity_flags = [x > 90 for x in raw_readings]
filtered_readings = list(compress(raw_readings, validity_flags))

# Apply temperature compensation
adjusted_readings = [r * 0.98 for r in filtered_readings]

# Calculate rolling averages over 2-point windows
rolling_averages = [(adjusted_readings[i] + adjusted_readings[i+1]) / 2 for i in range(len(adjusted_readings)-1)]

# Adjust totals with bonus for consistency
adjusted_totals = [avg + (1.5 if abs(adjusted_readings[i] - adjusted_readings[i+1]) < 5 else 0) for i, avg in enumerate(rolling_averages)]

# Determine final performance score
final_score = max(adjusted_totals)

# Irrelevant tracking variable (minimal distraction)
count_valid = len(filtered_readings)

print(f"Result: {final_score}")