import math

# Simulated sensor data and calibration values
data_stream = [3.2, 4.8, 5.1, 6.7, 2.9, 7.3, 8.0, 1.4, 9.2, 6.5]
baseline = 5.0
noise_floor = 1.5
calibration_factor = 0.9

# Irrelevant auxiliary metrics (distractors)
signal_quality_score = 0.0
stability_index = 0.0
redundant_accumulator = 0.0

def analyze_stability(window):
    return sum(x ** 0.5 for x in window if x > 3) / len(window)

# Misleading pre-processing step (not used in final logic)
preliminary_normalization = [calibration_factor * (x - baseline) for x in data_stream]

# Actual relevant filtering based on dynamic threshold
filtered_data = [x for x in data_stream if abs(x - baseline) > noise_floor]

# Lambda function for adaptive thresholding (used)
threshold_func = lambda val: math.log(val) if val > 4 else 0.5

# Secondary distractor: complex but unused signal refinement
refined_candidates = []
for val in data_stream:
    if val > baseline:
        adjusted = val * (1 + 0.1 * math.sin(val))
        refined_candidates.append(round(adjusted, 2))

# Helper function with conditional expression (core logic)
def process_signals(signals, threshold_strategy):
    result = 0.0
    temp_log = []
    for s in signals:
        # Conditional expression usage
        contribution = s * 0.8 if s > 6 else s * 0.6
        dynamic_weight = threshold_strategy(s)
        
        # Interdependent computation
        weighted_val = contribution * (dynamic_weight + 1)
        temp_log.append(weighted_val)
        
        # Accumulate only final output
        result += weighted_val
    
    # Red herring: unused intermediate statistic
    avg_temp = sum(temp_log) / len(temp_log) if temp_log else 0
    stability_index = avg_temp * 0.1  # Distractor assignment
    
    return round(result, 4)

# Unused recursive diagnostic (dead code path - interference)
def diagnose_anomalies(seq, idx=0):
    if idx >= len(seq):
        return 0
    if seq[idx] < 0:
        return 1 + diagnose_anomalies(seq, idx + 1)
    return diagnose_anomalies(seq, idx + 1)

# Core execution point
final_output = process_signals(filtered_data, threshold_func)

# Print result as required
print(f"Target result: {final_output}")