import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 21.9, 20.4, 27.3, 28.0, 26.1]
humidity_readings = [45, 48, 52, 58, 61, 44, 39, 63, 66, 57]
pressure_readings = [1013, 1015, 1012, 1008, 1005, 1018, 1020, 1003, 998, 1007]

# Irrelevant auxiliary data (distractor)
sound_levels = [32, 35, 40, 45, 50, 38, 36, 42, 48, 55]  # Decoy sensor data
vibration_patterns = [[1,2],[3,4],[5,6],[7,8]]  # Unused structure

# Data transformation functions
def normalize(values):
    min_val, max_val = min(values), max(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

def rolling_average(values, window=3):
    smoothed = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        smoothed.append(sum(values[start:i+1]) / (i - start + 1))
    return smoothed

# Irrelevant function (dead code path)
def calculate_entropy(data):
    total = sum(data)
    if total == 0:
        return 0
    return -sum((x/total) * math.log2(x/total) for x in data if x > 0)

# Core processing pipeline
def filter_outliers(values, factor=1.5):
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    low_bound = q1 - factor * iqr
    high_bound = q3 + factor * iqr
    return [v for v in values if low_bound <= v <= high_bound]

# Complex slicing and combination logic
def extract_critical_windows(readings):
    n = len(readings)
    # Multiple slicing operations with overlapping regions
    window_a = readings[:n//2]                     # First half
    window_b = readings[n//4:3*n//4]              # Middle half
    window_c = readings[-n//3:]                    # Last third
    window_d = readings[1::2]                     # Odd indices
    
    # Combine using non-trivial weights (only window_b and window_d are actually used later)
    combined_score = (
        sum(window_a) * 0.1 + 
        sum(window_b) * 0.4 + 
        sum(window_c) * 0.2 + 
        sum(window_d) * 0.3
    )
    return round(combined_score, 3)

# Misleading intermediate diagnostic (red herring)
def compute_stability_index(temp, hum):
    norm_temp = normalize(temp)
    norm_hum = normalize(hum)
    diffs = [abs(norm_temp[i] - norm_hum[i]) for i in range(len(norm_temp))]
    return sum(diffs) / len(diffs)

# Real processing steps disguised among distractors
def preprocess_sensors(temp, hum, pres):
    # Apply filtering only to temperature (key fact)
    cleaned_temp = filter_outliers(temp)
    
    # Normalize all relevant signals
    norm_temp = normalize(cleaned_temp)
    norm_pres = normalize(pres)
    
    # Construct processed data with metadata
    metadata = {
        'source': 'ARRAY-7B',
        'calibration_offset': 0.07,
        'version': '2.1.3'
    }
    
    # Create composite structure with slices
    time_slices = [
        norm_temp[:3],
        norm_temp[3:6], 
        norm_temp[6:]
    ]
    
    return {
        'temp_data': norm_temp,
        'pressure_data': norm_pres,
        'time_blocks': time_slices,
        'raw_count': len(temp),
        'cleaned_count': len(cleaned_temp),
        'meta': metadata
    }

# Threshold logic with bit manipulation red herring
def generate_threshold_map():
    base_threshold = 0.45
    
    # Bit manipulation distraction (unused)
    flag_mask = 0b1101 ^ 0b1011 & 0b1110
    debug_flag = (flag_mask << 2) | 0b10
    
    # Actual thresholds
    return {
        'critical_level': base_threshold,
        'recovery_bias': 0.1,
        'window_penalty': 0.05
    }

# Main analysis function (uses only specific parts of input)
def analyze_readings(data, thresholds):
    temp_seq = data['temp_data']
    blocks = data['time_blocks']
    
    # Use slicing to extract evaluation segments
    early_phase = blocks[0]
    mid_phase = blocks[1]
    late_phase = blocks[2]
    
    # Scoring logic with conditional accumulation
    score = 0.0
    if len(early_phase) > 0 and sum(early_phase) / len(early_phase) > thresholds['critical_level']:
        score += 1.5
    
    # Mid phase requires sustained elevation
    if all(x > thresholds['critical_level'] for x in mid_phase):
        score += 2.0
    
    # Late phase decay check
    if len(late_phase) >= 2 and late_phase[-1] < late_phase[0]:
        score += 0.8
    
    # Additional penalty based on window size inconsistency
    sizes = [len(b) for b in blocks]
    if max(sizes) - min(sizes) > 1:
        score -= thresholds['window_penalty']
    
    # Diagnostic classification
    if score >= 3.0:
        diagnosis = 5  # Critical
    elif score >= 2.0:
        diagnosis = 3  # Elevated
    elif score >= 1.0:
        diagnosis = 2  # Normal
    else:
        diagnosis = 1  # Low
    
    # Final computation involving combinatorics distraction
    adjustment_factor = 1
    for i in range(1, min(4, len(blocks))):
        adjustment_factor *= i  # Actually just computes 3! at most
    
    # But we don't use factorial — instead, final result is diagnosis squared plus score
    final_value = diagnosis ** 2 + score - 0.5  # Offset adjustment
    
    # Red herring: entropy calculation never used
    def local_entropy(seq):
        total = sum(seq)
        return -sum((x/total)*math.log2(x/total) for x in seq if x > 0)
    
    return int(round(final_value))

# Execution flow with decoy calls
if __name__ == "__main__":
    # Irrelevant preprocessing (distractor)
    normalized_humidity = normalize(humidity_readings)
    avg_pressure = rolling_average(pressure_readings, 2)
    stability = compute_stability_index(temperature_readings, humidity_readings)
    
    # Actual critical path
    processed_data = preprocess_sensors(temperature_readings, humidity_readings, pressure_readings)
    threshold_map = generate_threshold_map()
    
    # Key statement
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")