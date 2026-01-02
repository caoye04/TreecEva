import math

# Simulated sensor fusion system for environmental monitoring
raw_readings = [14.2, 18.5, 22.1, 19.3, 25.6, 30.1, 28.7, 24.5, 20.3, 17.8]

def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) * 100 for x in data]

def filter_outliers(data, factor=1.5):
    # Irrelevant filtering function - not actually used in final computation
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    lower, upper = q1 - factor * iqr, q3 + factor * iqr
    return [x for x in data if lower <= x <= upper]

def transform_scale(value):
    # Unused transformation - red herring
    return round(math.log(value + 1) * 10, 2) if value > 0 else 0

def rolling_average(data, window=3):
    # Distractor: looks important but unused
    result = []
    for i in range(len(data) - window + 1):
        result.append(sum(data[i:i+window]) / window)
    return result

def generate_checksum(data):
    # Decoy function: computes something that looks diagnostic
    checksum = 0
    for i, val in enumerate(data):
        checksum += int(val) ^ (i + 1)
    return checksum % 1000

# Dead code path - never called
class DataBuffer:
    def __init__(self, size):
        self.buffer = [0] * size
        self.index = 0
    
    def push(self, val):
        self.buffer[self.index % len(self.buffer)] = val
        self.index += 1

# Key processing steps interwoven with distractions
def process_sequence(seq):
    temp_results = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            # Apply square root to even indices, then scale
            transformed = math.sqrt(val) * 2.5
        else:
            # Apply ceiling and shift
            transformed = math.ceil(val / 2) * 1.8
        temp_results.append(round(transformed, 3))
    
    # Slicing operation - core element
    sliced_part = temp_results[1:-1:2]  # Take every other from index 1 to -1
    
    # Add irrelevant modification
    offset_correction = sum(sliced_part) / len(sliced_part) if sliced_part else 0
    adjusted = [x + offset_correction * 0.1 for x in temp_results]
    
    return adjusted

# Set operations as required - core logic uses intersection
baseline_set = {10, 15, 20, 25, 30, 35}
threshold_set = {18, 20, 22, 24, 25, 28, 30}
critical_band = baseline_set & threshold_set  # Intersection: {20, 25, 30}

# Unused set operations - distractors
expanded_threshold = threshold_set | {32, 34}
deviations = threshold_set - baseline_set

# Main analysis function with early returns and multiple concepts
def analyze_readings(readings, alert_levels):
    if not readings:
        return -1
    
    magnitude = sum(1 for x in readings if x > 20)
    if magnitude < 3:
        return 0
    
    # First real computation branch
    normalized = normalize(readings)
    processed = process_sequence(normalized)
    
    # Compute secondary metric - looks important
    avg_normalized = sum(normalized) / len(normalized)
    fluctuation_index = max(normalized) - min(normalized)
    
    # Red herring: this block modifies a variable but it's not used later
    diagnostic_flag = 1
    if fluctuation_index > 50:
        diagnostic_flag = 2
        temp_score = avg_normalized * 0.85
        if temp_score > 60:
            diagnostic_flag = 3
    
    # Core logic begins here - depends on set intersection result
    base_multiplier = len(critical_band)  # = 3
    adjustment_factor = 0
    for i, val in enumerate(processed):
        if i in critical_band:  # Only indices 20,25,30 - but i only goes to ~10
            adjustment_factor += val * 0.1
        elif i % 4 == 0 and i > 0:
            adjustment_factor += val * 0.05
    
    # This is the actual answer path
    signal_strength = sum(processed) / 10.0  # ~6.7ish
    
    # Final calculation combines multiple hidden paths
    final_score = signal_strength * base_multiplier
    
    # Integer division and rounding - key step
    rough_estimate = int(final_score // 1)  # Truncate
    
    # Early return decoy - this condition is false
    if rough_estimate in deviations:
        return rough_estimate * 2
    
    # Actual return
    convergence_metric = round(final_score + adjustment_factor, 4)
    return convergence_metric

# Execution flow with distraction variables
buffer_sim = DataBuffer(5)
for val in raw_readings[:5]:
    buffer_sim.push(val)

# Irrelevant checksum
checksum_diagnostic = generate_checksum(raw_readings)

# Main processing pipeline
normalized_data = normalize(raw_readings)  # Used
processed_data = process_sequence(normalized_data)  # Used

# Key execution point
final_diagnostic = analyze_readings(processed_data, threshold_set)

print(f"Result: {final_diagnostic}")