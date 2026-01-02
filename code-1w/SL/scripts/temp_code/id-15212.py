import math

def analyze_conditions(temperature, pressure, humidity):
    # Irrelevant transformation
    adjusted_temp = temperature + 273.15
    saturated_vapor_pressure = 6.11 * (humidity / 100) if humidity > 0 else 0
    
    # Distractor calculation
    dew_point = adjusted_temp - ((100 - humidity) / 5) if humidity < 80 else adjusted_temp - 4
    
    # Relevant logic: stability index
    stability_index = (pressure / 1000) * (temperature / adjusted_temp)
    return stability_index > 0.85

def compute_entropy(values):
    total = sum(values)
    entropy = 0.0
    for v in values:
        prob = v / total if total > 0 else 0
        if prob > 0:
            entropy -= prob * math.log(prob)
    return entropy

def process_metrics(data):
    baseline = 100
    threshold = 0.7
    temp_sum = 0
    valid_entries = 0
    
    # Track auxiliary state (some irrelevant)
    cumulative_product = 1
    fluctuation_count = 0
    previous = None
    
    for entry in data:
        t, p, h, readings = entry['temp'], entry['press'], entry['humid'], entry['sensors']
        
        # Irrelevant but plausible computation
        sensor_entropy = compute_entropy(readings)
        normality_factor = sensor_entropy / 10.0
        
        # Conditional expression - relevant to filtering
        is_stable = analyze_conditions(t, p, h)
        include_entry = (t > 15 and p > 950) and is_stable
        
        # Key branching logic with distractors
        if include_entry:
            temp_sum += t * (1 + h / 100)
            valid_entries += 1
            
            # Real impact: product accumulates only for valid entries
            max_sensor = max(readings) if readings else 0
            cumulative_product *= (max_sensor % 7 + 1)
            
            if previous is not None and abs(t - previous) > 5:
                fluctuation_count += 1
            previous = t
        else:
            # Dead code path (never executed due to data)
            baseline -= 5
    
    # Red herring: unused complex calculation
    complexity_metric = math.sqrt(cumulative_product) if cumulative_product > 0 else 0
    adjustment_factor = 1 + (fluctuation_count * 0.05)
    
    # Core formula - efficiency depends only on average weighted temp and valid count
    avg_weighted_temp = temp_sum / valid_entries if valid_entries > 0 else 0
    efficiency_score = baseline - (avg_weighted_temp * 0.5) + (valid_entries * 2)
    
    # Final output includes irrelevant formatting
    final_output = {
        'result': efficiency_score,
        'entries_processed': len(data),
        'distractor_metric': complexity_metric
    }
    
    return final_output

data = [
    {'temp': 20, 'press': 1013, 'humid': 60, 'sensors': [3, 5, 7, 2]},
    {'temp': 25, 'press': 1005, 'humid': 65, 'sensors': [4, 4, 6, 8]},
    {'temp': 18, 'press': 998, 'humid': 70, 'sensors': [5, 3, 5, 4]},  # Below pressure threshold
    {'temp': 30, 'press': 1020, 'humid': 50, 'sensors': [7, 6, 8, 9]}
]

result_dict = process_metrics(data)
efficiency_score = result_dict['result']
print(f"Target result: {efficiency_score}")