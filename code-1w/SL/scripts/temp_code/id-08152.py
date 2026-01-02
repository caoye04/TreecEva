from collections import defaultdict
from itertools import cycle

# Simulate sensor data processing with noise filtering and thresholding
def main():
    raw_readings = [124, 135, 128, 140, 99, 133, 138, 127, 141, 101]
    calibration_offsets = [3, -2, 1, 0, -1, 2, -3, 0, 1, -2]
    
    # Apply calibration (relevant)
    calibrated = [raw_readings[i] + calibration_offsets[i] for i in range(len(raw_readings))]
    
    # Noise detection (distractor: computed but not used later)
    high_fluctuations = []
    for i in range(1, len(calibrated)):
        if abs(calibrated[i] - calibrated[i-1]) > 10:
            high_fluctuations.append(i)
    
    # Normalize around mean (relevant)
    mean_val = sum(calibrated) / len(calibrated)
    normalized = [x - mean_val for x in calibrated]
    
    # Scale to percentage range (relevant)
    max_dev = max(normalized, key=abs)
    scaled_values = [round(50 + (v / max_dev) * 50) for v in normalized]
    
    # Threshold bands (semi-relevant setup)
    thresholds = defaultdict(list)
    for val in scaled_values:
        if val < 40:
            thresholds['low'].append(val)
        elif val > 60:
            thresholds['high'].append(val)
        else:
            thresholds['normal'].append(val)
    
    # Distractor: elaborate but unused frequency analysis
    freq_counter = defaultdict(int)
    pattern_cycle = cycle(['A', 'B', 'C'])
    for idx, val in enumerate(scaled_values):
        bucket = next(pattern_cycle)
        freq_counter[f'{bucket}_{val // 10}'] += 1
    
    # Dead code path - never executed (distractor)
    def legacy_adjust(x):
        return x * 1.1 if x < 45 else x * 0.9
    
    # Key processing function
    final_score = process_results(scaled_values, thresholds)
    print(f"Result: {final_score}")

# Process results based on balance of high/low deviations
def process_results(values, thresh):
    high_count = len(thresh['high'])
    low_count = len(thresh['low'])
    normal_count = len(thresh['normal'])
    
    # Compute imbalance score (core logic)
    imbalance = abs(high_count - low_count)
    
    # Base adjustment from median of highs
    median_high = sorted(thresh['high'])[(len(thresh['high'])-1)//2] if thresh['high'] else 0
    
    # Dummy bitwise manipulation (looks important, minimal real impact)
    flag = (high_count ^ low_count) & 1
    tweak = median_high >> 3 if flag else 5
    
    # Final score computation (answer determined here)
    base_score = 100 - (imbalance * 4)
    final_score = base_score + tweak - normal_count
    
    # Additional red herring: XOR-based checksum (not used)
    checksum = 0
    for v in values:
        checksum ^= (v + 7) % 17
    
    return final_score

if __name__ == '__main__':
    main()