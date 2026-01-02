def analyze_temperatures(temp_readings):
    high_threshold = 30
    low_threshold = 10
    hot_days = [t for t in temp_readings if t > high_threshold]
    cold_days = [t for t in temp_readings if t < low_threshold]
    moderate_days = [t for t in temp_readings if low_threshold <= t <= high_threshold]
    
    # Distractor: statistical analysis not used in final result
    avg_temp = sum(temp_readings) / len(temp_readings)
    temp_variance = sum((t - avg_temp) ** 2 for t in temp_readings) / len(temp_readings)
    
    return {'hot': len(hot_days), 'moderate': len(moderate_days), 'cold': len(cold_days)}


def transform_codes(event_codes):
    # Mapping codes with distraction logic
    code_map = {c: ord(c.upper()) - ord('A') + 1 for c in 'abcdefghij'}
    numeric_values = [code_map.get(e.lower(), 0) for e in event_codes]
    weighted_sum = sum(v * (i + 1) for i, v in enumerate(numeric_values))
    
    # Dead computation path
    if len(numeric_values) > 5:
        adjustment = (weighted_sum % 7) * 2.5
    else:
        adjustment = 0
    
    return numeric_values, weighted_sum  # Only weighted_sum is semi-relevant


def filter_and_aggregate(metadata_flags, readings):
    valid_flags = {'active', 'valid', 'confirmed'}
    filtered_readings = []
    flag_count = 0
    
    for i, flag in enumerate(metadata_flags):
        if flag in valid_flags and i < len(readings):
            filtered_readings.append(readings[i])
            flag_count += 1
    
    # Unused but distracting aggregation
    cumulative = 0
    running_totals = []
    for val in filtered_readings:
        cumulative += val
        running_totals.append(cumulative)
    
    return filtered_readings


def calculate_final_score(data_packet):
    raw_temps = data_packet['temperatures']
    events = data_packet['events']
    flags = data_packet['status_flags']
    
    # Step 1: Analyze temperature distribution
    temp_analysis = analyze_temperatures(raw_temps)
    
    # Step 2: Transform event codes
    _, event_bonus = transform_codes(events)
    
    # Step 3: Filter sensor readings using flags
    filtered_sensors = filter_and_aggregate(flags, raw_temps)
    
    # Step 4: Core calculation
    base_score = temp_analysis['hot'] * 3
    base_score += temp_analysis['moderate'] * 2
    base_score += temp_analysis['cold'] * 1
    
    # Step 5: Apply bonus from event codes (only component that uses event_bonus)
    scaled_bonus = int(event_bonus // 10)
    intermediate_result = base_score + scaled_bonus
    
    # Step 6: Adjustment based on filtered sensor count
    if len(filtered_sensors) >= 4:
        intermediate_result += 5
    elif len(filtered_sensors) >= 2:
        intermediate_result += 2
    else:
        intermediate_result -= 3
    
    # Step 7: Final non-linear transformation
    final_score = (intermediate_result ** 2) // (len(events) or 1)
    
    # Critical print statement
    print(f"Result: {final_score}")
    return final_score

# Main execution block
if __name__ == "__main__":
    input_data = {
        'temperatures': [8, 15, 22, 35, 29, 11, 31],
        'events': ['B', 'E', 'D', 'A'],
        'status_flags': ['active', 'inactive', 'valid', 'invalid', 'confirmed', 'unknown', 'active']
    }
    final_score = calculate_final_score(input_data)