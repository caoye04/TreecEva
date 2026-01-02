from itertools import combinations

def preprocess_entries(raw_data):
    processed = []
    for item in raw_data:
        name, value_str = item.split(':')
        cleaned_value = float(value_str.strip().upper().replace('X', '0'))
        processed.append((name.strip(), cleaned_value))
    return processed

def validate_range(value, min_val=0, max_val=100):
    return min(max(value, min_val), max_val)

def calculate_final_score(entries, limits):
    scores = []
    temp_offsets = [0.5, -0.3, 0.7]
    cumulative_shift = 0

    for idx, (label, val) in enumerate(entries):
        capped = validate_range(val)
        if 'temp' in label.lower():
            capped += temp_offsets[idx % len(temp_offsets)]
        
        category_multiplier = 1.0
        if any(c.isupper() for c in label):
            category_multiplier = 1.2
        
        adjusted = capped * category_multiplier
        
        # Irrelevant combination tracking (distractor)
        _ = list(combinations([adjusted], 1))  
        
        scores.append(adjusted)

    # Secondary logic path that doesn't affect outcome (dead branch)
    debug_mode = False
    if debug_mode:
        print("Debug info:", scores)

    base_avg = sum(scores) / len(scores)
    
    # Apply threshold filtering
    thresholded = [s for s in scores if s >= limits['passing']]
    
    # Unused transformation (distractor)
    normalized = [round((x - min(thresholded)) / (max(thresholded) - min(thresholded)) * 100) 
                 for x in thresholded] if len(thresholded) > 1 else [50]

    final_score = int(round(base_avg + len(thresholded) * 0.5))
    
    # Extra computation with no impact
    checksum = sum(f'{final_score}'[i] == f'{final_score}'[-i-1] for i in range(len(f'{final_score}')))
    
    return final_score

# Main execution
raw_input = [
    "SensorA: 89.4", "TEMP_B: 92X1", "sensor_c: 76.8",
    "MonitorD: 85.0", "TEMP_E: 88X5"
]

data = preprocess_entries(raw_input)
thresholds = {'passing': 80}

intermediate_total = sum(int(x[1]) for x in data)  # Red herring variable

final_score = calculate_final_score(data, thresholds)
print(f"Result: {final_score}")