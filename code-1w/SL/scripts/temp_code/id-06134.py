from collections import defaultdict
from itertools import combinations

# Simulate sensor data aggregation and scoring for environmental monitoring
raw_readings = [12.5, 13.0, 11.8, 14.2, 13.1, 12.9, 13.3, 12.7]
weights = {'temp': 0.4, 'stability': 0.3, 'trend': 0.2, 'outlier_penalty': 0.1}

# Irrelevant preprocessing: group readings by rounded value (not used in final logic)
dummy_counter = defaultdict(int)
for val in raw_readings:
    dummy_counter[round(val)] += 1

# Extract trends and volatility
mean_temp = sum(raw_readings) / len(raw_readings)
temp_deviation = [abs(x - mean_temp) for x in raw_readings]
avg_deviation = sum(temp_deviation) / len(temp_deviation)

# Identify increasing trend segments (used later)
trend_count = 0
for i in range(len(raw_readings) - 1):
    if raw_readings[i] < raw_readings[i + 1]:
        trend_count += 1

# Simulate redundant stability metric using set operations
unique_devs = set(round(d, 1) for d in temp_deviation)
high_dev_threshold = 0.5
exceedance_count = len([d for d in temp_deviation if d > high_dev_threshold])

# Dummy combination analysis (dead code path - not used)
all_pairs = list(combinations(raw_readings, 2))
convergent_pairs = 0
for a, b in all_pairs:
    if abs(a - b) < 0.3:
        convergent_pairs += 1  # Not used

# Secondary distraction: simulate calibration offset
baseline_offset = 0.15
adjusted_readings = [r - baseline_offset for r in raw_readings]
adjusted_mean = sum(adjusted_readings) / len(adjusted_readings)

# Core scoring function
def compute_base_metrics(data):
    base = sum(data) / len(data)
    variance = sum((x - base) ** 2 for x in data) / len(data)
    return base, variance

def compute_trend_strength(data):
    increases = 0
    for i in range(1, len(data)):
        if data[i] >= data[i-1]:
            increases += 1
    return increases / (len(data) - 1) if len(data) > 1 else 0

def count_outliers(data, threshold=1.0):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return sum(1 for x in data if abs(x - mean) > threshold * std_dev)

def compute_final_score(data, w):
    # Step 1: Base temperature score
    temp_score, var = compute_base_metrics(data)
    
    # Step 2: Stability score (inverse of normalized variance)
    max_reasonable_var = 0.6
    stability_score = max(0, 1 - var / max_reasonable_var)
    
    # Step 3: Trend score
    trend_score = compute_trend_strength(data)
    
    # Step 4: Outlier penalty
    outliers = count_outliers(data, threshold=1.2)
    penalty_factor = outliers * 0.05  # Max penalty caps at 0.25 for 5+ outliers
    
    # Final weighted score
    score = (
        w['temp'] * temp_score +
        w['stability'] * stability_score * 10 +  # Scale to match temp range
        w['trend'] * trend_score * 10 +
        w['outlier_penalty'] * (1 - penalty_factor) * 10
    )
    return round(score, 4)

# Misleading intermediate calculation (semi-relevant but overridden)
initial_estimate = mean_temp * 0.8 + trend_count * 0.5

# Actual critical computation
final_score = compute_final_score(raw_readings, weights)

# Output result as required
print(f"Result: {final_score}")