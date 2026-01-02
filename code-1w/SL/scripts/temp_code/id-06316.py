def calculate_final_score(raw_data, importance_weights):
    # Initialize tracking variables
    base_sum = 0
    adjustment_factor = 0
    temp_result = []
    cumulative_shift = 0

    # Irrelevant pre-processing (distractor)
    outlier_buffer = [x for x in raw_data if x > 50]
    filtered_data = [x for x in raw_data if x % 2 == 0]

    for i, value in enumerate(raw_data):
        weighted_val = value * importance_weights[i % len(importance_weights)]
        mod_index = i % 4
        
        if mod_index == 0:
            adjusted = (weighted_val + 10) % 87
        elif mod_index == 1:
            adjusted = (weighted_val * 2) % 87
        elif mod_index == 2:
            adjusted = abs(weighted_val - 5) % 87
        else:
            adjusted = (weighted_val + 3) % 87

        base_sum += adjusted

        # Dead computation branch (distractor)
        if i > 100:
            cumulative_shift += adjusted * 0.1

        temp_result.append(adjusted)

    # Secondary loop with semi-relevant transformation
    decay_factor = 1.0
    decayed_sum = 0
    for val in temp_result:
        decayed_sum += val * decay_factor
        decay_factor *= 0.95  # Not used in final result but looks important

    # Dictionary-based bonus calculation (actual relevant logic)
    score_categories = {
        'A': sum(temp_result[::3]),
        'B': sum(temp_result[1::3]),
        'C': sum(temp_result[2::3])
    }

    category_bonus = 0
    for key, total in score_categories.items():
        if total > 30:
            category_bonus += total // 10

    # Final computation (this is what matters)
    adjustment_factor = sum(score_categories.values()) % 97
    final_score = (base_sum + category_bonus) % 10000

    # Unused diagnostic output (distractor)
    diagnostics = {
        'input_length': len(raw_data),
        'peak_value': max(temp_result),
        'shift_total': cumulative_shift
    }

    return final_score

# Main execution
import math
raw_input_data = [12, 45, 23, 67, 34, 89, 21, 56, 78, 33]
weights_config = [0.8, 1.2, 0.9, 1.1, 1.0]
counter_mirror = [x * 2 for x in raw_input_data]  # Irrelevant mirror array

# Key statement
final_score = calculate_final_score(raw_input_data, weights_config)
print(f"Result: {final_score}")