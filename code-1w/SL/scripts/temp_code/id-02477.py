from itertools import compress, cycle
import math

# Simulated sensor array data (temperature readings in Celsius)
sensor_ids = [101, 102, 103, 104, 105, 106, 107, 108]
raw_readings = [23.5, 19.0, -1.2, 25.8, 30.1, -2.5, 27.3, 22.0]
operational_flags = [True, True, False, True, True, False, True, True]

def adjust_for_drift(value, sensor_id):
    # Simulate hardware-specific calibration
    if sensor_id % 2 == 0:
        return value + 0.3
    else:
        return value - 0.1

def classify_temperature(temp):
    if temp < 0:
        return 'FROZEN'
    elif temp < 20:
        return 'COOL'
    elif temp < 25:
        return 'WARM'
    else:
        return 'HOT'

# Irrelevant transformation chain (distractor)
shifted_cycle = list(zip(raw_readings, cycle([0.1, -0.1])))
decoy_mapped = [x[0] + x[1] for x in shifted_cycle]
decoy_filtered = [x for x in decoy_mapped if x > 20]

def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Dead function - looks important but unused in main logic
def legacy_normalization(arr):
    min_val, max_val = min(arr), max(arr)
    return [(x - min_val) / (max_val - min_val) for x in arr]

# Misleading intermediate calculation
aggregate_score = sum(abs(x) for x in raw_readings) / len(raw_readings)
pseudo_entropy = math.log(aggregate_score + 1) * 100

# Core processing begins here
adjusted_readings = [
    adjust_for_drift(val, sid) 
    for val, sid in zip(raw_readings, sensor_ids)
]

# Mask out non-operational sensors and invalid readings
valid_readings_mask = [
    flag and val > -2.0 
    for flag, val in zip(operational_flags, adjusted_readings)
]

filtered_data = list(compress(adjusted_readings, valid_readings_mask))

# Decoy statistical summary
mean_raw = sum(raw_readings) / len(raw_readings)
std_dev_raw = (sum((x - mean_raw) ** 2 for x in raw_readings) / len(raw_readings)) ** 0.5
outlier_boundary = mean_raw + 2 * std_dev_raw  # Not actually used

# Create dynamic threshold function using lambda
base_threshold = 24.0
elevation_factor = 1.1
threshold_func = lambda x: base_threshold * elevation_factor if classify_temperature(x) == 'HOT' else base_threshold * 0.9

# Secondary decoy structure
classification_summary = {
    cat: len([r for r in adjusted_readings if classify_temperature(r) == cat])
    for cat in ['FROZEN', 'COOL', 'WARM', 'HOT']
}

def process_readings(data, threshold_strategy):
    # Apply complex filtering based on dynamic thresholds
    hot_zone = []
    warm_zone = []
    
    for reading in data:
        effective_threshold = threshold_strategy(reading)
        if reading >= effective_threshold:
            hot_zone.append(reading)
        elif reading >= 20.0:
            warm_zone.append(reading)
    
    # Complex aggregation with bit manipulation (irrelevant to final result but looks critical)
    hot_count_encoded = len(hot_zone) << 2
    warm_count_encoded = len(warm_zone) ^ 5
    
    # Red herring: entropy-like calculation
    if hot_zone:
        total_weight = sum(math.log(x + 10) for x in hot_zone)
        decoy_index = total_weight / len(hot_zone)
    
    # Actual determinant of final result
    primary_metric = sum(hot_zone) if hot_zone else sum(warm_zone) / 2 if warm_zone else 0
    
    # Additional distraction: mock machine learning weight
    ml_sim_weight = 0.85
    confidence_adjustment = len(hot_zone) * 0.1
    
    # Final diagnostic is only dependent on primary_metric, others are distractions
    final_diagnostic = int(primary_metric * 10)  # Critical deterministic output
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_func)
print(f"Result: {final_diagnostic}")