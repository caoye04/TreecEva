import math

def preprocess_readings(raw_signal):
    # Distractor: Signal smoothing with irrelevant filter
    filtered = [x * 0.98 for x in raw_signal if x > 0]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    return [abs(x - baseline) for x in filtered]

def compute_entropy(values):
    # Real but misleading: computes entropy, not used in final result
    total = sum(values)
    probs = [(v / total) for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs if p > 0)

def evaluate_stability(readings):
    if len(readings) < 3:
        return 0
    variance = sum((readings[i] - readings[i-1])**2 for i in range(1, len(readings)))
    return variance / (len(readings) - 1)

def generate_diagnostic_chain(data_stream):
    # Heavily nested and partially irrelevant processing chain
    stage_a = [x for x in data_stream if x % 2 == 0]
    stage_b = [x**2 for x in stage_a if x > 5]
    temp_score = sum(stage_b) // len(stage_b) if stage_b else 0

    # Red herring: complex transformation that isn't used
    derived_flags = []
    for val in stage_b:
        if val > 100:
            derived_flags.append(val & 7)
        elif val > 50:
            derived_flags.append(val ^ 3)
        else:
            derived_flags.append(val | 1)
    
    # Decoy accumulation
    cumulative_risk = 0
    for flag in derived_flags:
        cumulative_risk += flag * 0.7
        if cumulative_risk > 40:
            cumulative_risk -= 10

    # Actual relevant path buried here
    critical_path = sum(x for x in data_stream if x < 0)
    return temp_score, critical_path  # Only second value matters

def analyze_metrics(health_vector, threshold_map):
    # Core logic mixed with distractions
    
    # Irrelevant unpacking and unused assignments
    primary_metric, _ = generate_diagnostic_chain(health_vector)
    
    # Meaningful but obscured computation
    base_level = sum(health_vector)
    adjustment_factor = threshold_map.get('sensitivity', 1.5)
    
    # Conditional expression - required feature
    offset = -50 if base_level < 0 else 50
    
    # List comprehension - required feature
    refined_inputs = [x for x in health_vector if x in threshold_map.values()]
    
    # Dead code path: never reached due to fixed keys
    debug_modes = ['full', 'lite', 'off']
    mode_index = 0
    while mode_index < len(debug_modes):
        if debug_modes[mode_index] == 'tracing':
            break
        mode_index += 1
    
    # Core calculation hidden among distractors
    trigger_value = 0
    for k, v in threshold_map.items():
        if k.startswith('t_') and v % 2 == 1:
            trigger_value += v

    # Key dependency from outside
    _, critical_path = generate_diagnostic_chain(health_vector)
    
    # Final result combines real and fake elements
    final_diagnostic = base_level + trigger_value * adjustment_factor + critical_path + offset
    
    # Prints result as required
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    # Input setup
    raw_health_data = [-12, 8, -6, 15, 3, 0, -21, 9]
    config_thresholds = {
        't_1': 7,
        't_2': 4,
        't_3': 11,
        'sensitivity': 2.0,
        'baseline': 100
    }
    
    # Preprocessing that doesn't affect outcome
    processed = preprocess_readings(raw_health_data)
    entropy = compute_entropy(processed)
    stability = evaluate_stability(processed)
    
    # Irrelevant recursive structure (never alters anything)
    def dummy_recursive(n):
        if n <= 1:
            return 1
        return n + dummy_recursive(n - 2)
    
    dummy_recursive(10)
    
    # Critical execution point
    final_diagnostic = analyze_metrics(raw_health_data, config_thresholds)