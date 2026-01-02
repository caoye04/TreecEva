from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic analysis
def fetch_raw_readings():
    return [
        (101, 23.1, 'temp'), (102, 45.6, 'pressure'), (103, 23.1, 'temp'),
        (104, 12.8, 'humidity'), (105, 45.6, 'pressure'), (106, 18.3, 'temp'),
        (107, 12.8, 'humidity'), (108, 23.1, 'temp'), (109, 33.9, 'flow')
    ]

def validate_sensor(id_val, reading):
    # Complex validation logic with bit manipulation for error flags
    flag = 0
    if id_val & 1:
        flag ^= 1
    if id_val > 105:
        flag |= 4
    if reading < 20.0:
        flag |= 2
    return flag == 0 or (flag & 2)  # Allow low readings only

def filter_and_classify(raw):
    grouped = defaultdict(list)
    stats = {'valid': 0, 'invalid': 0, 'redundant': 0}
    seen_values = set()
    
    for sid, val, stype in raw:
        key = (stype, val)
        if key in seen_values:
            stats['redundant'] += 1
            continue
            
        if not validate_sensor(sid, val):
            stats['invalid'] += 1
            continue
            
        grouped[stype].append(val)
        seen_values.add(key)
        stats['valid'] += 1
    
    # Distractor: unused transformation
    inverse_map = {v: k for k, v in grouped.items() if len(v) > 1}
    temp_avg = sum(grouped['temp']) / len(grouped['temp']) if grouped['temp'] else 0
    
    # Irrelevant aggregation
    pressure_mode = max(Counter(grouped['pressure']).items(), key=lambda x: x[1])[0] if grouped['pressure'] else None
    
    return dict(grouped), stats, temp_avg

def compute_baseline(readings_dict):
    base = {}
    for typ, vals in readings_dict.items():n        if typ == 'temp':
            base[typ] = round(sum(vals) / len(vals), 2)
        elif typ == 'pressure':
            base[typ] = max(vals) - min(vals)
        else:
            base[typ] = len(vals) * 1.5
    return base

def generate_threshold_map(baseline):
    # Create dynamic thresholds based on baseline with artificial complexity
    tmap = defaultdict(lambda: (0.0, 100.0))
    for k, v in baseline.items():
        if isinstance(v, float):
            tmap[k] = (v * 0.8, v * 1.2)
        else:
            tmap[k] = (v - 5, v + 10)
    # Add decoy entries
    tmap['phantom_sensor'] = (-999, -998)
    tmap['aux_power'] = (0, 40)
    return dict(tmap)

def enhance_resolution(data):
    # Dummy high-res transformation
    enhanced = {}
    for k, v in data.items():
        enhanced[f"{k}_hr"] = [round(x * 1.01, 3) for x in v]
    return enhanced

def detect_anomalies(hr_data, thresholds):
    anomalies = []
    for k, vals in hr_data.items():
        clean_key = k.replace('_hr', '')
        low_t, high_t = thresholds.get(clean_key, (0, float('inf')))
        for v in vals:
            if not (low_t <= v <= high_t):
                anomalies.append((clean_key, v))
    return anomalies

def recursive_integrity_check(data_list, index=0, acc_checksum=0):
    # Simple recursion to add interference
    if index >= len(data_list):
        return acc_checksum * 1.05
    val = data_list[index]
    new_sum = acc_checksum + (val * index)
    return recursive_integrity_check(data_list, index + 1, new_sum)

def finalize_report(anomaly_list, raw_stats):
    score = 100 - len(anomaly_list) * 5
    score -= raw_stats['invalid'] * 3
    score = max(score, 10)
    return round(score, 1)

def analyze_readings(processed, threshold_map):
    # Core analysis function with critical computation
    flat_vals = [v for sublist in processed.values() for v in sublist]
    sorted_vals = sorted(flat_vals)
    n = len(sorted_vals)
    median = (sorted_vals[n//2] + sorted_vals[(n-1)//2]) / 2
    
    # Key calculation path
    base_weight = sum(flat_vals) / (median + 1)
    
    # Dead code branch - never executed due to condition
    emergency_override = False
    if base_weight < 0:
        critical_chain = [base_weight]
        for i in range(5):
            critical_chain.append(critical_chain[-1] * 1.5 - 2)
        base_weight = sum(critical_chain)
    
    # Decoy statistical computations
    variance_proxy = sum((x - base_weight / 10) ** 2 for x in flat_vals[:3])
    entropy_approx = len(set(flat_vals)) / len(flat_vals) if flat_vals else 0
    
    # Critical statement: final diagnostic depends on filtered data and thresholds
    valid_range_items = 0
    for k, v_list in processed.items():
        low, high = threshold_map.get(k, (0, 0))
        for v in v_list:
            if low <= v <= high:
                valid_range_items += 1
    
    adjustment_factor = 0.95 if valid_range_items > 5 else 1.05
    
    # Final deterministic result
    final_diagnostic = int((base_weight * adjustment_factor * 100) % 973) + 42
    
    # Unused complex structure
    report_summary = {
        'items_processed': len(flat_vals),
        'median_value': median,
        'range_compliance': valid_range_items,
        'adjustment': adjustment_factor,
        'raw_score': base_weight,
        'diagnostic_code': f"DX{final_diagnostic:04d}"
    }
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    raw_data = fetch_raw_readings()
    
    # Irrelevant preprocessing step
    sorted_by_id = sorted(raw_data, key=lambda x: x[0])
    filtered_data, validation_stats, average_temp = filter_and_classify(raw_data)
    
    # Multiple distraction transformations
    baseline_refs = compute_baseline(filtered_data)
    threshold_map = generate_threshold_map(baseline_refs)
    high_res_data = enhance_resolution(filtered_data)
    anomaly_list = detect_anomalies(high_res_data, threshold_map)
    
    # Recursive check with unused result
    temp_array = [int(x * 10) for x in filtered_data.get('temp', [])]
    checksum_result = recursive_integrity_check(temp_array) if temp_array else 0
    
    # Final reporting steps
    compliance_score = finalize_report(anomaly_list, validation_stats)
    processed_data = filtered_data  # Alias for clarity
    
    # Key execution point
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    print(f"Result: {final_diagnostic}")