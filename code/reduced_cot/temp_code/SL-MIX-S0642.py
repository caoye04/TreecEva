from collections import Counter

def evaluate_conditions(x_values):
    results = []
    for x in x_values:
        # Main logical evaluation chain
        condition_a = (x > 5) and (x % 2 == 0)
        condition_b = (x < 10) or (x == 15)
        final_condition = condition_a and not condition_b
        results.append(final_condition)
    return results

# Input data processing
input_data = [3, 8, 12, 6, 15, 7, 4]
processed_results = evaluate_conditions(input_data)
result_counter = Counter(processed_results)

# Final computation
final_count = result_counter[True] - result_counter[False]
print(f"Result: {final_count}")