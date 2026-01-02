from collections import defaultdict
import math

# Simulated sensor data ingestion (realistic domain: environmental monitoring)
sensor_readings = [
    [0.5, 1.2, 3.7, 2.1, 0.9],
    [1.3, 0.8, 2.5, 4.0, 1.7],
    [2.0, 3.1, 1.4, 0.6, 3.3],
    [1.8, 2.7, 3.9, 2.2, 1.1]
]

# Irrelevant calibration matrix (distractor - not used in final computation)
calibration_matrix = [
    [1.01, 0.99, 1.02, 0.98, 1.00],
    [0.97, 1.03, 0.96, 1.04, 0.95],
    [1.05, 0.94, 1.06, 0.93, 1.07],
    [0.92, 1.08, 0.91, 1.09, 0.90]
]

# Misleading preprocessing function (dead code path)
def legacy_normalize(data):
    max_val = max(max(row) for row in data)
    return [[val / max_val for val in row] for row in data]

# Unused transformation (red herring)
legacy_normalized = legacy_normalize(sensor_readings)

# Real preprocessing: transpose and extract peaks
transposed = list(zip(*sensor_readings))  # Convert to column-wise per sensor

# Extract peak values per sensor (column)
peak_values = [max(column) for column in transposed]

# Compute rolling averages (slicing operation - required feature)
rolling_avg = []
for i in range(len(peak_values) - 1):
    rolling_avg.append((peak_values[i] + peak_values[i+1]) / 2)

# Add dummy padding (irrelevant)
padded_rolling = [0.0] + rolling_avg + [0.0]

# Threshold map based on adaptive baselines (used later)
thresh_base = sum(peak_values) / len(peak_values)
threshold_map = {
    'low': thresh_base * 0.7,
    'high': thresh_base * 1.3,
    'critical': thresh_base * 1.8
}

# Simulate data corruption flags (distractor)
corruption_flags = defaultdict(bool)
for i, p in enumerate(peak_values):
    corruption_flags[i] = (p > 4.0)  # Never true in this dataset

# Processed data structure (key relevant data)
processed_data = {
    'peaks': peak_values,
    'baseline': thresh_base,
    'stats': {
        'mean_peak': thresh_base,
        'variance': sum((x - thresh_base)**2 for x in peak_values) / len(peak_values),
        'entropy': -sum((x / sum(peak_values)) * math.log(x / sum(peak_values)) for x in peak_values if x > 0)
    }
}

# Decoy analysis function (never called)
def quick_diagnostic(data):
    return sum(data['peaks']) % 7

# Actual analysis logic
# Uses bit manipulation to encode state (required paradigm)
def diagnose_state(value, thresholds):
    flag = 0
    if value < thresholds['low']:
        flag |= 1  # Below normal
    if value > thresholds['high']:
        flag |= 2  # Elevated
    if value > thresholds['critical']:
        flag |= 4  # Critical
    if value == thresholds['high']:
        flag |= 8  # Exact high (never happens)
    return flag

# Complex conditional analysis with short-circuiting and nesting
def analyze_signal(data, thresholds):
    peaks = data['peaks']
    baseline = data['baseline']
    total_score = 0
    
    for i, p in enumerate(peaks):
        # Multiple nested conditions (3 levels deep)
        if p > baseline:
            if i % 2 == 0:
                # Even-indexed sensors use XOR-based weighting
                weight = i ^ 3
                if weight == 0:
                    weight = 1
                contribution = (p / baseline) * weight
                
                # Bit shift for scaling (paradigm inclusion)
                scaled = int(contribution * 10) >> 1
                total_score += scaled
            else:
                # Odd-indexed: use logarithmic adjustment
                log_adj = math.log(p + 1) * 2
                total_score -= int(log_adj)
        else:
            # Below baseline: minor addition
            total_score += 1
            
        # Short-circuit logic with OR (paradigm inclusion)
        status_flag = diagnose_state(p, thresholds)
        if status_flag & 2 or status_flag & 4:  # Elevated or critical
            total_score += 5
        
    # Final transformation using slicing (last 3 elements of peaks)
    tail_peaks = peaks[-3:]
    tail_correction = sum(tail_peaks) / 3 * 1.5
    
    # Distractor: unused dictionary update
    data['stats']['phantom_metric'] = 999
    
    # Final result (this is the answer)
    final = int(total_score + tail_correction)
    
    return final

# Key execution point
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")