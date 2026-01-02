from collections import defaultdict, Counter
import math

# Simulated sensor data processing with red herrings and distractions
def load_sensor_metadata():
    # Irrelevant metadata loading (distractor)
    return {
        'sensor_01': {'calibration': 'alpha', 'active': True},
        'sensor_02': {'calibration': 'beta', 'active': False}
    }

def legacy_checksum(data):
    # Outdated function not used in main logic (dead code path)
    return sum(d % 7 for d in data) * 3

def preprocess_frame(frame):
    # Unused preprocessing (distractor)
    return [x for x in frame if x > 0]

def generate_frequency_map(data):
    # Creates a frequency map but only partially relevant
    freq = defaultdict(int)
    for item in data:
        freq[item] += 1
    return freq

def filter_outliers(sequence, limit=50):
    # Filters values above limit, but limit is misleadingly set
    return [x for x in sequence if x < limit]

def shift_cipher(values, key=3):
    # Bit manipulation red herring
    return [(v << 1) ^ key for v in values]

def compute_rolling_average(data, window=3):
    # Looks important but not used in final result
    averages = []
    for i in range(len(data) - window + 1):
        avg = sum(data[i:i+window]) / window
        averages.append(round(avg, 2))
    return averages

def transform_sequence(raw):
    # Core transformation: reverse, slice every second, then apply operation
    reversed_raw = raw[::-1]
    sliced = reversed_raw[::2]  # Take every second element from reversed
    powered = [x ** 2 for x in sliced]  # Square each
    return powered

def analyze_pattern(data, cutoff):
    # Main analysis: count how many exceed cutoff, then apply formula
    count_above = len([x for x in data if x > cutoff])
    total = sum(data)
    # Real computation path
    if count_above > 0:
        base_metric = total / count_above
        adjustment = math.log2(count_above + 1)
        result = int(base_metric - adjustment)
    else:
        result = -1
    return result

# --- Main execution with distractions ---
if __name__ == "__main__":
    # Load real data
    raw_readings = [12, 7, 23, 8, 19, 4, 16, 27, 3, 11]
    
    # Distractor variables (irrelevant computations)
    calibration_data = load_sensor_metadata()
    checksum_value = legacy_checksum(raw_readings)  # Dead end
    filtered_chunk = filter_outliers(raw_readings, limit=15)  # Partial use, misleading
    shifted_data = shift_cipher(filtered_chunk, key=5)  # Complete red herring
    rolling_avgs = compute_rolling_average(shifted_data, window=2)  # Unused
    
    # Real processing begins here
    processed_signal = preprocess_frame(raw_readings)  # Unused return
    freq_map = generate_frequency_map(raw_readings)  # Collected but unused
    
    # Key transformation
    transformed_data = transform_sequence(raw_readings)
    
    # Multiple threshold attempts (only last one matters)
    test_threshold = 100
    temp_diagnostic = analyze_pattern(transformed_data, test_threshold)
    test_threshold = 50
    temp_diagnostic = analyze_pattern(transformed_data, test_threshold)
    
    # Final correct execution point
    threshold = 20
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Print final answer as required
    print(f"Result: {final_diagnostic}")