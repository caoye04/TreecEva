def calculate_final_score(data, weight_dict):
    # Initialize intermediate variables
    base_values = []
    temp_accum = 0
    adjustment_factor = 0.85
    
    for key in ['temp', 'pressure', 'humidity']:
        if key in data:
            base_values.append(data[key] * weight_dict.get(key, 1.0))
    
    # Irrelevant computation: tracking unused stats
    unused_stat_1 = sum(base_values) / len(base_values) if base_values else 0
    unused_stat_2 = max(base_values) - min(base_values) if len(base_values) > 1 else 0

    # Real logic begins: apply nonlinear transform on critical component
    critical_input = data.get('flow_rate', 0)
    processed_flow = (lambda x: x ** 2 - 2 * x + 1)(critical_input)  # (x-1)^2

    # Secondary distraction: dead code path with misleading name
    def deprecated_calc(x):
        return x * 0.9 + 10

    # More irrelevant variables
    dummy_correction = 7.2
    scaling_offset = 3.1415

    # Actual contribution from flow rate
    flow_contribution = processed_flow * weight_dict.get('flow_rate', 0.5)

    # Combine base values with flow contribution
    raw_total = sum(base_values) + flow_contribution

    # Apply final adjustment using fixed factor (not the dummy ones!)
    final_adjusted = raw_total * adjustment_factor

    # Additional state tracking (unused)
    history_log = {'input': data.copy(), 'output': final_adjusted}

    # Final score calculation
    final_score = int(final_adjusted + 0.5)  # Round to nearest integer

    return final_score

# Main execution context
if __name__ == '__main__':
    # Input data map with sensor readings
    data_map = {
        'temp': 23,
        'pressure': 101.3,
        'humidity': 45,
        'flow_rate': 5
    }

    # Weight configuration dictionary
    weights = {
        'temp': 0.2,
        'pressure': 0.15,
        'humidity': 0.1,
        'flow_rate': 0.4
    }

    # Perform calculation
    final_score = calculate_final_score(data_map, weights)

    # Output result
    print(f"Result: {final_score}")