from collections import defaultdict

# Simulate system performance analysis with noise and filtering
def analyze_system_metrics(raw_data, threshold=0.75):
    efficiency = {}
    diagnostics = []
    temp_accumulator = 0

    for module, readings in raw_data.items():
        valid_readings = [r for r in readings if r > threshold]
        efficiency[module] = len(valid_readings) / len(readings)

        # Irrelevant diagnostic accumulation (distractor)
        if len(valid_readings) > 2:
            diagnostics.append(f"{module}_stable")
        else:
            diagnostics.append(f"{module}_caution")

        temp_accumulator += sum(valid_readings)

    # Dead code path - never accessed in normal flow (mild red herring)
    if temp_accumulator < 0:
        efficiency['fallback'] = 0.0

    return efficiency

def generate_error_profile(config_layers):
    error_log = defaultdict(int)
    shadow_count = 0  # Unused tracking variable

    for layer in config_layers:
        if 'critical' in layer:
            error_log['critical'] += 1
        elif 'core' in layer:
            error_log['core'] += 2
        else:
            error_log['other'] += 1

        # Misleading computation
        shadow_count += len(layer) * 0.1

    # Additional irrelevant transformation
    normalized = {k: v * 1.0 for k, v in error_log.items()}
    return dict(error_log)

def calculate_weight_distribution(factors):
    base_weights = {f: (i + 1) * 10 for i, f in enumerate(factors)}
    adjustment = sum(base_weights.values()) / 100

    # Complex but ultimately unused alternate weighting
    alt_scheme = {k: v / adjustment for k, v in base_weights.items()}

    # Final weight selection
    weights = {k: v / 10 for k, v in base_weights.items()}  # Only this matters
    return weights

def evaluate_performance(efficiency, error_log, weights):
    base_score = 0
    penalty = 0

    # Primary scoring logic
    for module, score in efficiency.items():
        if 'module_a' in module:
            base_score += score * weights.get('critical', 10)
        elif 'module_b' in module:
            base_score += score * weights.get('core', 8)
        else:
            base_score += score * weights.get('other', 5)

    # Penalty application based on error types
    for err_type, count in error_log.items():
        if err_type == 'critical':
            penalty += count * 15
        elif err_type == 'core':
            penalty += count * 8
        else:
            penalty += count * 3

    # Final composite score
    final_score = int(base_score * 100) - penalty  # Key result

    # Distractor: unused intermediate
    normalized_final = round(final_score / 100.0, 2)

    return final_score

# Main execution
if __name__ == "__main__":
    raw_data = {
        'module_a_1': [0.8, 0.9, 0.76, 0.85],
        'module_a_2': [0.92, 0.88, 0.95],
        'module_b_1': [0.6, 0.81, 0.72, 0.88],
        'module_b_2': [0.55, 0.65, 0.75, 0.85, 0.95]
    }

    config_layers = ['critical_init', 'core_processor', 'core_validator', 'post_process']
    factors = ['critical', 'core', 'other']

    # Execute pipeline
    efficiency = analyze_system_metrics(raw_data)
    error_log = generate_error_profile(config_layers)
    weights = calculate_weight_distribution(factors)
    
    # Critical execution point
    final_score = evaluate_performance(efficiency, error_log, weights)
    
    print(f"Target result: {final_score}")