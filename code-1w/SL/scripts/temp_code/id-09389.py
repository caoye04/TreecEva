import math

def analyze_readings(readings):
    # Irrelevant transformation (dead path)
    temp_adjusted = [r * 1.05 for r in readings if r > 0]
    normalized = [max(0, min(100, r)) for r in readings]  # Clamped to health range
    avg = sum(normalized) / len(normalized)
    return avg if avg > 0 else 50

def calculate_stress_index(x, y):
    # Misleading function: looks important but unused in critical path
    return int((abs(x - y) ** 0.5) * 10)

def recursive_filter(data, depth):
    if depth <= 0 or not data:
        return [d for d in data if d % 2 == 1]  # Keep only odd values at base
    return recursive_filter([d // 2 for d in data if d > 10], depth - 1)

def compute_baseline(values, mode='standard'):
    if mode == 'advanced':
        return sum(v ** 0.8 for v in values) / len(values)
    else:
        return sum(v * 0.9 for v in values) / len(values)

def evaluate_risk_level(score):
    risk_map = {'low': 30, 'med': 70, 'high': 90}
    # Conditional expression used
    return 'critical' if score > risk_map['high'] else ('high' if score > risk_map['med'] else ('med' if score > risk_map['low'] else 'low'))

def process_metrics(data, thresholds):
    # Core logic with distractions
    stage_one = [val for val in data if val >= thresholds.get('min_init', 0)]
    
    # Distractor block: complex but irrelevant calculation
    decoy_sum = 0
    for i in range(len(stage_one)):
        if i % 3 == 0:
            decoy_sum += int(math.sin(i + 0.1) * 100)
    
    # Real processing begins
    filtered = recursive_filter(stage_one, 3)
    base_score = compute_baseline(filtered, mode='standard')
    
    # Dictionary operations and conditional expression
    adjustment = {'critical': 1.2, 'high': 1.1, 'med': 1.0, 'low': 0.9}
    risk_state = evaluate_risk_level(base_score)
    adjusted_score = base_score * adjustment.get(risk_state, 1.0)
    
    # Final decision logic
    secondary_check = sum(1 for f in filtered if f > 20)
    final_modifier = 1.05 if secondary_check >= 2 else 0.95
    
    # Key result
    result = adjusted_score * final_modifier
    
    # Dead code - looks like logging but does nothing
    log_entry = {
        'raw_input_size': len(data),
        'filtered_count': len(filtered),
        'computed_score': result,
        'timestamp': 1678886400
    }
    
    # Actual answer variable
    final_diagnostic = int(round(result))
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Input data - biometric sensor readings
    health_data = [85, 92, 103, 45, 67, 110, 120, 50, 58]
    
    # Threshold configuration map (dictionary)
    threshold_map = {
        'min_init': 40,
        'max_spike': 120,
        'crit_window': 5
    }
    
    # Unused variables - red herrings
    calibration_sequence = [0.98, 1.02, 0.99, 1.01]
    system_uptime = 14236
    debug_mode = False
    
    # Critical call
    final_diagnostic = process_metrics(health_data, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")