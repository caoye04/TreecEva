import itertools

def analyze_sensor_network():
    # Simulated sensor grid readings (real data)
    raw_readings = [18, 22, 15, 30, 45, 28, 17, 25, 33, 20, 12, 50]
    
    # Irrelevant environmental constants (distractor)
    baseline_pressure = 101.3
    humidity_factor = 0.67
    elevation_bias = 0.03
    temperature_offset = -2.1
    
    # Critical configuration map (used later)
    threshold_map = {
        'normal': 25,
        'warning': 35,
        'critical': 45
    }
    
    # Decoy function that looks important but is never called
    def compute_air_quality_index(values):
        return sum(v ** 0.8 for v in values) / len(values)
    
    # Unused transformation pipeline (dead code path)
    processed_chain = list(itertools.accumulate(raw_readings, lambda x, y: x + y // 3))
    smoothed_data = [x * 0.9 for x in raw_readings if x > 10]  # Partial use, partial red herring
    
    # Logical filter based on dynamic condition (relevant)
    activation_threshold = 14
    filtered_data = [x for x in raw_readings if x > activation_threshold]
    
    # Spurious statistical computation (misleading intermediate)
    mean_val = sum(filtered_data) / len(filtered_data)
    variance = sum((x - mean_val) ** 2 for x in filtered_data) / len(filtered_data)
    stdev = variance ** 0.5
    
    # Dummy state tracker (irrelevant)
    system_states = ['idle', 'active', 'standby']
    current_state = system_states[1]
    state_code = hash(current_state) % 100
    
    # Complex conditional expression with bit manipulation (mixed relevance)
    mode_flag = 0b101
    if len(filtered_data) > 8 and mode_flag & 0b100:
        mode_flag ^= 0b010
    
    # Redundant dictionary update chain (mostly irrelevant)
    status_log = {}
    status_log.update({'init': 'complete'})
    status_log['timestamp'] = 123456789
    status_log['readings_count'] = len(raw_readings)
    
    # Core processing function (uses filtered_data and threshold_map)
    def process_readings(data, thresholds):
        count_normal = 0
        count_warning = 0
        count_critical = 0
        
        # Nested loop over combinations (combinatorics distraction)
        pairs = list(itertools.combinations(data, 2))
        high_pairs = [p for p in pairs if sum(p) > 60]  # Looks important
        
        # Actual classification logic (key path)
        for val in data:
            if val < thresholds['warning']:
                count_normal += 1
            elif val < thresholds['critical']:
                count_warning += 1
            else:
                count_critical += 1
        
        # Dummy recursion (looks complex but unused result)
        def recursive_weight(n):
            if n <= 1:
                return 1
            return n + recursive_weight(n - 2)
        
        # Final diagnostic score calculation (ANSWER COMPUTED HERE)
        base_score = count_normal * 10
        base_score += count_warning * 25
        base_score -= count_critical * 15
        
        # Additional decoy arithmetic
        adjustment = (state_code * stdev) // 10
        final_score = base_score - int(adjustment)  # adjustment is near-zero due to small stdev
        
        return final_score
    
    # Execution point of interest
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

# Run the analysis
analyze_sensor_network()