from collections import defaultdict, Counter
import math

# Simulated sensor array data from environmental monitoring system
def fetch_sensor_data():
    raw_readings = [
        (1, 'TEMP', 23.5), (2, 'HUMID', 65.2), (3, 'CO2', 410),
        (4, 'TEMP', 24.1), (5, 'HUMID', 63.8), (6, 'CO2', 425),
        (7, 'TEMP', 22.9), (8, 'HUMID', 67.3), (9, 'CO2', 395)
    ]
    return raw_readings

# Irrelevant utility: computes geometric mean (not used in final path)
def geometric_mean(values):
    product = 1
    for v in values:
        if v > 0:
            product *= v
    return product ** (1 / len(values)) if values else 0

# Distraction function: analyzes pressure (but no pressure data exists)
def analyze_pressure(readings):
    pressure_data = [v for sid, stype, v in readings if stype == 'PRESS']
    return sum(pressure_data) * 0.01 if pressure_data else -999

# Core transformation: groups and aggregates valid sensor types
def process_readings(raw_readings):
    grouped = defaultdict(list)
    type_count = Counter()
    
    for sensor_id, s_type, value in raw_readings:
        if s_type in ['TEMP', 'HUMID', 'CO2']:
            grouped[s_type].append(value)
            type_count[s_type] += 1
    
    # Dead code branch — type_count is never checked again
    if type_count['TEMP'] > 10:
        grouped['TEMP'].append(999)  # Never reached

    processed = {}
    for t in grouped:
        values = grouped[t]
        avg = sum(values) / len(values)
        variance = sum((x - avg) ** 2 for x in values) / len(values)
        processed[t] = {'mean': avg, 'variance': variance}
    
    # Red herring computation
    entropy = 0
    total = sum(type_count.values())
    for count in type_count.values():
        if count > 0:
            p = count / total
            entropy -= p * math.log2(p)
    
    processed['ENTROPY_DIAGNOSTIC'] = entropy  # Distractor field
    return processed

# Threshold logic with misleading branching
def build_threshold_map():
    thresholds = defaultdict(dict)
    thresholds['TEMP']['min'] = 18.0
    thresholds['TEMP']['max'] = 26.0
    thresholds['HUMID']['min'] = 40.0
    thresholds['HUMID']['max'] = 70.0
    thresholds['CO2']['min'] = 350
    thresholds['CO2']['max'] = 450
    
    # Unused security thresholds
    thresholds['SECURE']['ACCESS_LVL'] = 3
    thresholds['SECURE']['ENCRYPT'] = True
    
    return thresholds

# Main analysis with conditional overrides and bit flags
def analyze_readings(data, limits):
    flags = 0
    diagnostics = []
    
    for param, stats in data.items():
        if param == 'ENTROPY_DIAGNOSTIC':
            continue  # Skip distractor
            
        mean_val = stats['mean']
        min_limit = limits[param]['min']
        max_limit = limits[param]['max']
        
        # Bit flag assignment (only relevant for TEMP and CO2)
        if param == 'TEMP':
            if mean_val < min_limit:
                flags |= 1  # Cold warning
            elif mean_val > max_limit:
                flags |= 2  # Hot warning
            else:
                flags |= 4  # Normal range
        
        if param == 'CO2':
            if mean_val > max_limit:
                flags |= 8   # High CO2
            else:
                flags |= 16  # Acceptable CO2
        
        # Logical check chain (only one affects result)
        status_code = 0
        if mean_val < min_limit * 0.9:
            status_code = -1
        elif mean_val > max_limit * 1.1:
            status_code = -2
        else:
            status_code = int(mean_val + 0.5)  # Round to nearest int
        
        diagnostics.append(status_code)
    
    # Only the CO2 mean contributes to final diagnostic value
    co2_mean = data['CO2']['mean']
    adjustment_factor = 1.0
    
    # Misleading nested conditionals
    if flags & 8:  # High CO2 detected
        if data['TEMP']['variance'] > 0.5:
            adjustment_factor = 0.9
        elif data['HUMID']['mean'] < 50:
            adjustment_factor = 1.05
        else:
            adjustment_factor = 0.95
    
    # Final diagnostic is adjusted CO2 mean multiplied by active bit count
    bit_count = bin(flags).count('1')
    final_value = co2_mean * adjustment_factor * bit_count
    
    # Decoy transformation (never used)
    squared_chain = 0
    for i in range(3):
        squared_chain += final_value ** (i+1)
    
    # Actual answer
    final_diagnostic = int(round(final_value))
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Orchestration function with unused trace log
def run_diagnostics():
    trace_log = []
    trace_log.append("Starting environmental diagnostic suite")
    
    raw_data = fetch_sensor_data()
    trace_log.append(f"Fetched {len(raw_data)} sensor entries")
    
    processed_data = process_readings(raw_data)
    trace_log.append("Data processing complete")
    
    threshold_map = build_threshold_map()
    trace_log.append("Thresholds initialized")
    
    # Key execution point
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Final trace not printed
    trace_log.append(f"Final diagnostic code: {final_diagnostic}")
    
    return final_diagnostic

# Execute main logic
result = run_diagnostics()