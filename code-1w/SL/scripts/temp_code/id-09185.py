import math

# Simulated sensor array diagnostics with noise filtering and status classification

def collect_sensor_readings():
    raw_readings = [
        (102, 'temp', 0.8), (155, 'pressure', 1.2), (201, 'temp', 0.9),
        (98, 'temp', 0.7), (305, 'flow', 2.1), (148, 'pressure', 1.0),
        (250, 'flow', 1.8), (105, 'temp', 1.1), (152, 'pressure', 0.9)
    ]
    return raw_readings

def apply_noise_filter(readings):
    # Filter out high-variance anomalies based on sensitivity factor
    filtered = []
    for val, sensor_type, sens in readings:
        if sensor_type == 'temp' and abs(val - 100) <= 20:
            filtered.append((val, sensor_type))
        elif sensor_type == 'pressure' and 140 <= val <= 160:
            filtered.append((val, sensor_type))
        elif sensor_type == 'flow' and val > 200:
            filtered.append((val, sensor_type))
    return filtered

def build_threshold_map():
    # Complex threshold policy using dictionary and lambda functions
    base = {'temp': 105, 'pressure': 150, 'flow': 250}
    adjustment = lambda x: 0.95 * x if x < 120 else 1.05 * x
    adj_base = {k: adjustment(v) for k, v in base.items()}
    
    # Irrelevant secondary map (distractor)
    safety_multipliers = {'temp': 1.1, 'pressure': 1.2, 'flow': 1.15}
    tolerance = {'temp': 5, 'pressure': 10, 'flow': 20}
    
    # Return only the relevant one
    return adj_base

def evaluate_stability(status_log):
    # Dead function - never called (red herring)
    stable_count = 0
    for entry in status_log:
        if entry['status'] == 'STABLE':
            stable_count += 1
    return stable_count

def aggregate_by_type(data):
    # Group sensor values by type using dictionary
    groups = {}
    for val, stype in data:
        if stype not in groups:
            groups[stype] = []
        groups[stype].append(val)
    return groups

def compute_variance(values):
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

def classify_status(variance, threshold):
    return 'CRITICAL' if variance > threshold else 'NORMAL'

def process_readings(clean_data, thresholds):
    # Core logic: compute variances and compare to adjusted thresholds
    grouped = aggregate_by_type(clean_data)
    
    # Irrelevant set operations (distractor)
    all_types = set(grouped.keys())
    required_types = set(['temp', 'pressure', 'flow'])
    missing = required_types - all_types
    redundant = all_types - required_types
    completeness_score = 100 * (1 - len(missing) / len(required_types))
    
    # Real computation path
    diagnostics = {}
    for stype, values in grouped.items():
        var = compute_variance(values)
        ref = thresholds[stype]
        # Use case conversion as minor distraction
        key = stype.upper()
        diagnostics[key] = classify_status(var, ref * 0.02)  # 2% of threshold as variance cap
    
    # Secondary distraction: character counting in status
    total_chars = sum(len(diagnostics[k]) for k in diagnostics)
    
    # Final diagnostic score: sum of adjusted variances minus red herrings
    final_components = []
    for stype, values in grouped.items():
        v = compute_variance(values)
        final_components.append(int(v * 10))
    
    # This is the real answer contributor
    base_diagnostic = sum(final_components)
    
    # Add irrelevant transformations
    temp_set = {int(x) for x in [math.sin(i) * 100 for i in range(3)]}
    offset = len(temp_set.intersection({0, 1, -1}))
    
    # Final result
    final_diagnostic = base_diagnostic - offset
    
    # Unused variables (dead code paths)
    audit_trail = []
    for t in sorted(required_types):
        audit_trail.append(f"{t}:{diagnostics[t.upper()]}")
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw sensor data
    raw_data = collect_sensor_readings()
    
    # Step 2: Apply noise filter
    cleaned = apply_noise_filter(raw_data)
    
    # Step 3: Build dynamic threshold map
    threshold_map = build_threshold_map()
    
    # Step 4: Process readings to generate final diagnostic code
    final_diagnostic = process_readings(cleaned, threshold_map)
    
    # Print result
    print(f"Result: {final_diagnostic}")