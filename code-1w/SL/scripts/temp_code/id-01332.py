import math

# Simulated system telemetry data
telemetry_stream = [142, 89, 201, 77, 133, 95, 104, 66, 188, 73]
data_log = [{'value': x, 'status': 'active' if x > 80 else 'idle', 'flagged': x % 13 == 0} for x in telemetry_stream]

# Irrelevant helper function (decoy)
def analyze_health(records):
    return sum(1 for r in records if r['value'] > 100)

# Unused transformation (dead code path)
transformed = [math.log(x['value']) for x in data_log if x['flagged']]

# Misleading intermediate calculation (red herring)
aggregate_score = sum(item['value'] for item in data_log) / len(data_log)

# Auxiliary constants with plausible but unused role
CALIBRATION_FACTOR = 0.917
REFERENCE_BASE = 85

# Bit manipulation distraction
def shift_diagnostic(val):
    shifted = val << 2
    masked = shifted & 0xFF
    return masked ^ 0xAA

# Unused diagnostic map (irrelevant structure)
diagnostic_map = {idx: shift_diagnostic(entry['value']) for idx, entry in enumerate(data_log)}

# Core logic buried among distractions
def evaluate_stability(value, base=REFERENCE_BASE):
    deviation = abs(value - base)
    return math.exp(-deviation / 100)

# Conditional expression and filtering mixed with noise
def filter_critical(entries):
    return [e for e in entries if e['value'] > 90 or e['flagged']]

# Key processing function with embedded logic chain
def process_metrics(log_entries, threshold):
    # Step 1: Filter active high-value entries
    filtered = [entry for entry in log_entries if entry['status'] == 'active']
    
    # Step 2: Apply dynamic thresholding
    qualified = [f for f in filtered if f['value'] > threshold]
    
    # Step 3: Compute stability weights using exponential decay model
    weights = [evaluate_stability(item['value']) for item in qualified]
    
    # Step 4: Aggregate weighted efficiency
    total_weight = sum(weights)
    total_value = sum(item['value'] * w for item, w in zip(qualified, weights))
    
    # Step 5: Normalize efficiency
    if total_weight == 0:
        efficiency = 0.0
    else:
        efficiency = total_value / total_weight
    
    # Step 6: Adjust with conditional offset (conditional expression)
    adjustment = 1.05 if len(qualified) >= 4 else 0.95
    adjusted_efficiency = efficiency * adjustment
    
    # Step 7: Calculate redundancy index (distractor computation)
    redundant_count = sum(1 for e in log_entries if e['value'] < 85)
    redundancy_index = redundant_count / len(log_entries)
    
    # Step 8: Final efficiency ratio incorporating robustness factor
    robust_entries = sum(1 for q in qualified if q['value'] > 100)
    robustness_factor = 1 + (robust_entries / len(qualified)) if qualified else 1
    efficiency_ratio = adjusted_efficiency * robustness_factor
    
    # Irrelevant final check (misleading branch)
    if redundancy_index > 0.3:
        efficiency_ratio *= 0.85  # This will not trigger
    
    # Critical point: efficiency_ratio is now finalized
    return efficiency_ratio

# Threshold setting (relevant)
threshold = 88

# Execution point of interest
final_output = process_metrics(data_log, threshold)

# Output the target variable
print(f"Result: {final_output}")