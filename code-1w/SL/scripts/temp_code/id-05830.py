from itertools import compress, count

# Simulated sensor data with timestamps and readings
timestamps = list(range(100, 200, 2))
raw_readings = [t * 0.75 + (-1)**t * 3 for t in timestamps]
quality_flags = [(r > 90 or r < 30) for r in raw_readings]

# Data filtering based on quality and range
filtered_times = [t for t, flag in zip(timestamps, quality_flags) if not flag]
filtered_readings = [r for r, flag in zip(raw_readings, quality_flags) if not flag]

# Misleading secondary processing (distractor)
decoy_stats = []
counter = count(1)
for i in range(len(filtered_readings)):
    val = filtered_readings[i] * next(counter)
    decoy_stats.append(val ** 0.5 if val > 0 else 0)

decoys_summed = sum(decoy_stats[::3])  # Irrelevant aggregation

# Actual signal analysis: detect rising trends
window_size = 4
trend_changes = 0
prev_avg = sum(filtered_readings[:window_size]) / window_size

for i in range(1, len(filtered_readings) - window_size + 1):
    current_avg = sum(filtered_readings[i:i+window_size]) / window_size
    if current_avg > prev_avg and current_avg > 50:
        trend_changes += 1
    prev_avg = current_avg

# Bonus logic based on pattern detection
def predict_next_peak(data, trends):
    base = sum(data[-10:]) / 10
    adjustment = trends * 1.5
    return base + adjustment

predicted_peak = predict_next_peak(filtered_readings, trend_changes)

# Validate entries above threshold
threshold = 65.0
valid_entries = [v for v in filtered_readings if v > threshold]

# Secondary decoy structure (dead path)
if len(valid_entries) > 100:
    scaled_vals = [v * 1.2 for v in valid_entries]
else:
    dummy_calc = len(filtered_readings) * 0.1  # Unused computation

# Bonus factor from predicted peak (only this matters)
bonus_factor = int(predicted_peak // 10)

# Core scoring logic
entry_points = len(valid_entries) * 2
bonus_points = bonus_factor * 3
penalty = 0

for val in valid_entries:
    if val < 70:
        penalty += 1
    elif val > 85:
        penalty -= 1  # Reward

final_score = process_results(entry_points, bonus_points, penalty)

# Redefine function to finalize score
def process_results(entries, bonus, pen):
    temp = entries + bonus - abs(pen)
    if temp < 0:
        return 0
    return int(temp * 1.1)  # Final scaling

# Recompute final score using correct function
final_score = process_results(entry_points, bonus_points, penalty)

print(f"Result: {final_score}")