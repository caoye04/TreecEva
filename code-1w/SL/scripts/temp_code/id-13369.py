from collections import defaultdict, Counter
import math

# Simulated sensor network data processing with diagnostic analysis
def collect_sensor_readings():
    raw_readings = [
        (0.88, 'temp', 'A1'), (1.02, 'pressure', 'B3'), (0.75, 'temp', 'A2'),
        (2.15, 'vibration', 'C1'), (0.93, 'temp', 'A1'), (1.88, 'vibration', 'C3'),
        (0.69, 'temp', 'A2'), (1.08, 'pressure', 'B1'), (2.03, 'vibration', 'C2')
    ]
    return raw_readings

def filter_outliers(data, factor=1.5):
    # Irrelevant outlier filtering (not used in final path)
    values = [x[0] for x in data]
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [item for item in data if lower_bound <= item[0] <= upper_bound]

def transform_units(readings):
    # Convert vibration readings from mm/s to g (conversion factor ~0.102)
    converted = []
    for value, sensor_type, sensor_id in readings:
        if sensor_type == 'vibration':
            value = round(value * 0.102, 4)  # mm/s to g
        converted.append((value, sensor_type, sensor_id))
    return converted

def aggregate_by_location(readings):
    location_data = defaultdict(list)
    for value, s_type, s_id in readings:
        location = s_id[0]  # A, B, or C
        location_data[location].append((value, s_type))
    return location_data

def compute_baseline_stats(data_dict):
    # Compute mean and variance per location (distractor)
    stats = {}
    for loc, records in data_dict.items():
        vals = [r[0] for r in records]
        mean = sum(vals) / len(vals)
        variance = sum((v - mean)**2 for v in vals) / len(vals)
        stats[loc] = {'mean': mean, 'variance': variance}
    return stats

def generate_compatibility_matrix(loc_data):
    # Generate fake compatibility scores between sensors (red herring)
    matrix = defaultdict(lambda: defaultdict(float))
    locations = list(loc_data.keys())
    for i, l1 in enumerate(locations):
        for j, l2 in enumerate(locations):
            score = (i + 1) * (j + 1) * 0.77
            matrix[l1][l2] = round(score, 3)
    return matrix

def calculate_entropy(readings):
    # Calculate entropy of sensor type distribution (unused but plausible)
    types = [t for _, t, _ in readings]
    counts = Counter(types)
    total = len(types)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def normalize_readings(aggregated):
    # Normalize readings per sensor type within each location
    normalized = defaultdict(list)
    type_extremes = defaultdict(lambda: {'min': float('inf'), 'max': float('-inf')})
    
    # First pass: find min/max per type
    for loc, records in aggregated.items():
        for val, typ in records:
            if val < type_extremes[typ]['min']:
                type_extremes[typ]['min'] = val
            if val > type_extremes[typ]['max']:
                type_extremes[typ]['max'] = val
    
    # Second pass: normalize
    for loc, records in aggregated.items():
        for val, typ in records:
            mn = type_extremes[typ]['min']
            mx = type_extremes[typ]['max']
            if mx > mn:
                norm_val = (val - mn) / (mx - mn)
            else:
                norm_val = 0.0
            normalized[loc].append((round(norm_val, 4), typ))
    
    return normalized

def derive_health_index(norm_data):
    # Compute health index based on normalized values (distractor function)
    indices = {}
    for loc, readings in norm_data.items():
        total_score = sum(val for val, _ in readings)
        indices[loc] = round(total_score / len(readings), 3) if readings else 0.0
    return indices

def build_diagnostic_profile(normalized):
    # Core relevant function: builds profile used in final analysis
    profile = defaultdict(lambda: defaultdict(list))
    for location, data in normalized.items():
        for norm_value, s_type in data:
            profile[s_type][location].append(norm_value)
    return profile

def analyze_readings(profile, thresholds):
    # Final diagnostic logic: counts how many readings exceed per-type/location thresholds
    alerts = 0
    for s_type, loc_data in profile.items():
        for location, values in loc_data.items():
            thresh = thresholds.get(s_type, {}).get(location, 0.8)
            alerts += sum(1 for v in values if v >= thresh)
    
    # Secondary adjustment based on global patterns
    all_vals = [v for lt in profile.values() for lv in lt.values() for v in lv]
    global_avg = sum(all_vals) / len(all_vals) if all_vals else 0
    
    if global_avg > 0.6:
        alerts = int(alerts * 1.25)  # 25% increase if overall activity high
    
    # Tertiary correction: apply diminishing returns
    final_score = alerts - int(math.sqrt(alerts)) if alerts > 0 else 0
    return final_score

def main():
    # Step 1: Collect raw data
    raw_data = collect_sensor_readings()
    
    # Step 2: Transform units (relevant)
    unit_converted = transform_units(raw_data)
    
    # Step 3: Aggregate by physical location (A, B, C)
    location_grouped = aggregate_by_location(unit_converted)
    
    # Step 4: Compute baseline statistics (distractor)
    stats_summary = compute_baseline_stats(location_grouped)
    
    # Step 5: Generate fake compatibility matrix (dead code path)
    compat_matrix = generate_compatibility_matrix(location_grouped)
    
    # Step 6: Calculate entropy of sensor distribution (irrelevant metric)
    entropy_metric = calculate_entropy(raw_data)
    
    # Step 7: Normalize readings per type (RELEVANT preprocessing)
    normalized_readings = normalize_readings(location_grouped)
    
    # Step 8: Derive health index (distractor result)
    health_index = derive_health_index(normalized_readings)
    
    # Step 9: Build diagnostic profile structure (critical)
    diagnostic_profile = build_diagnostic_profile(normalized_readings)
    
    # Step 10: Define dynamic thresholds (simulates adaptive system)
    threshold_map = {
        'temp': {'A': 0.65, 'B': 0.7, 'C': 0.75},
        'pressure': {'A': 0.6, 'B': 0.68, 'C': 0.72},
        'vibration': {'A': 0.55, 'B': 0.62, 'C': 0.69}
    }
    
    # Step 11: Perform final analysis (key statement)
    final_diagnostic = analyze_readings(diagnostic_profile, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")
    
    # Unused but plausible intermediate outputs
    debug_info = {
        'stats': stats_summary,
        'compat': compat_matrix,
        'entropy': entropy_metric,
        'health': health_index
    }
    
    return final_diagnostic

if __name__ == "__main__":
    main()