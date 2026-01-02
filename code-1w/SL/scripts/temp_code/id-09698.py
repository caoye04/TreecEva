import math

# Simulated sensor array data processing for environmental monitoring system
def collect_readings():
    raw_values = [3.2, 5.7, 1.4, 8.9, 2.5, 7.1, 4.3, 6.8]
    timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800, 1623456805, 1623456810, 1623456815]
    statuses = ['OK', 'ERROR', 'OK', 'OK', 'WARNING', 'OK', 'OK', 'ERROR']
    
    # Irrelevant transformation: convert timestamps to strings and back
    str_timestamps = [str(ts) for ts in timestamps]
    recovered_timestamps = [int(st) for st in str_timestamps]
    time_offset = sum(recovered_timestamps) - sum(timestamps)  # Always zero, distractor

    readings = []
    for i in range(len(raw_values)):
        reading_dict = {
            'id': i,
            'value': raw_values[i],
            'status': statuses[i],
            'valid': statuses[i] == 'OK',
            'magnitude_class': int(math.log10(raw_values[i]) + 1) if raw_values[i] > 0 else 0
        }
        readings.append(reading_dict)
    
    return readings

# Legacy function (dead code path) - not used but looks important
def legacy_calibrate(data_list):
    calibrated = []
    for item in data_list:
        adj_value = item['value'] * 0.95 + 0.3
        calibrated.append({**item, 'value': adj_value})
    return calibrated

# Misleading intermediate diagnostic function
def compute_health_score(dataset):
    score = 0
    for entry in dataset:
        if entry['status'] == 'OK':
            score += 10
        elif entry['status'] == 'WARNING':
            score += 5
        else:
            score -= 20
        
        # Bit manipulation red herring
        binary_id = bin(entry['id'])[2:]
        parity = sum([int(b) for b in binary_id]) % 2
        score += parity * 2
    
    normalized_score = round(score / len(dataset), 2)
    return normalized_score  # Never used in final calculation

# Auxiliary function with string distraction
def categorize_magnitude(value):
    category_map = {1: 'LOW', 2: 'MEDIUM', 3: 'HIGH'}
    mag = int(math.log10(value) + 1) if value > 0 else 0
    cat_str = category_map.get(mag, 'UNKNOWN')
    
    # Use string methods meaningfully but distractingly
    reversed_cat = cat_str.lower()[::-1]
    title_case_reversed = reversed_cat.title()
    
    # Return only the original category (distraction above)
    return cat_str

# Core processing pipeline
def filter_invalid_readings(readings):
    valid_entries = [r for r in readings if r['valid']]
    error_count = len([r for r in readings if not r['valid']])
    
    # Extra computation: checksum of valid ids (not used later)
    id_checksum = sum([r['id'] * (r['id'] + 1) // 2 for r in valid_entries]) % 1000
    
    # Sort by value descending
    sorted_entries = sorted(valid_entries, key=lambda x: x['value'], reverse=True)
    
    return sorted_entries

# Central accumulation logic
def accumulate_trend(data):
    trend_accumulator = 0.0
    weight_sequence = [0.8, 1.1, 1.3, 0.9, 1.0, 1.2]  # Weight per position
    
    for idx, entry in enumerate(data):
        base_contribution = entry['value'] * 0.5
        if idx < len(weight_sequence):
            weighted_contribution = base_contribution * weight_sequence[idx]
        else:
            weighted_contribution = base_contribution * 1.0
        
        # Apply logical condition mask
        is_medium = categorize_magnitude(entry['value']) == 'MEDIUM'
        is_high = categorize_magnitude(entry['value']) == 'HIGH'
        
        if is_high and not is_medium:
            trend_accumulator += weighted_contribution * 1.25
        elif is_medium:
            trend_accumulator += weighted_contribution * 0.85
        else:
            trend_accumulator += weighted_contribution
    
    return round(trend_accumulator, 4)

# Final diagnostic processor
def process_readings(data):
    # Summation with conditional inclusion
    total_impact = 0
    for item in data:
        magnitude_factor = item['magnitude_class']
        impact = item['value'] * magnitude_factor
        total_impact += impact
    
    # Secondary adjustment based on pattern recognition
    values_only = [d['value'] for d in data]
    above_median = [v for v in values_only if v > sum(values_only)/len(values_only)]
    bonus_multiplier = 1 + (len(above_median) * 0.05)
    
    # Apply adjustment
    adjusted_impact = total_impact * bonus_multiplier
    
    # Decoy bitwise operation
    shifted_impact = int(adjusted_impact) >> 1  # Unused
    xor_mask = 255
    masked_impact = int(adjusted_impact) ^ xor_mask  # Unused
    
    # Final non-linear transformation
    final_score = math.sqrt(adjusted_impact) * math.log(adjusted_impact + 10)
    
    return round(final_score, 4)

# Main execution sequence
data_stream = collect_readings()
health_metric = compute_health_score(data_stream)  # Computed but unused
filtered_data = filter_invalid_readings(data_stream)
trend_index = accumulate_trend(filtered_data)  # Intermediate result
final_diagnostic = process_readings(filtered_data)

# Output target result
print(f"Result: {final_diagnostic}")