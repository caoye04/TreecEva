from collections import Counter

# Environmental temperature monitoring over a week
temp_readings = [23, 25, 25, 27, 26, 28, 28, 29, 27, 30, 31, 29, 26]

temp_counter = Counter(temp_readings)
dominant_temp = temp_counter.most_common(1)[0][1]  # Frequency of most common temperature

temp_peaks = [t for t in temp_readings if t > 27]
avg_temp = sum(temp_readings) / len(temp_readings)
baseline_ref = sum(1 for t in temp_readings if t < 26)

# Key computational step
threshold_score = min(avg_temp, temp_peaks[-1]) >> 1

# Irrelevant string processing (minor distraction)
diagnostic_log = "System: TempMonitor v1.0"
status_flag = diagnostic_log.split(':')[0].lower() == "system"

print(f"Result: {threshold_score}")