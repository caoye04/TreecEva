from itertools import combinations

def analyze_pattern(sequence):
    # Irrelevant helper: counts increasing pairs (not used in final logic)
    increasing_pairs = sum(1 for a, b in zip(sequence, sequence[1:]) if a < b)
    avg = sum(sequence) / len(sequence)
    return avg

def compute_aggregate(data, threshold):
    # Core logic hidden among distractions
    temp_buffer = []
    cumulative = 0
    special_cases = 0

    # Distractor loop: processes data but only modifies dead-end vars
    for x in data:
        if x > threshold * 1.5:
            temp_buffer.append(x ** 0.5)
        elif x < threshold * 0.5:
            temp_buffer.append(-x)

    # Real logic begins: find all 3-element combos where sum exceeds threshold
    valid_combinations = list(combinations(data, 3))
    filtered = [combo for combo in valid_combinations if sum(combo) > threshold]

    # Accumulate sum of products of valid combos
    for combo in filtered:
        product = 1
        for val in combo:
            product *= val
        cumulative += product

    # Semi-relevant transformation
    adjustment_factor = len(filtered) if filtered else 1
    adjusted_total = cumulative / adjustment_factor

    # Additional red herring: string-based case tracking
    status_log = []
    for i, combo in enumerate(filtered):
        parity = "even" if sum(combo) % 2 == 0 else "odd"
        status_log.append(f"Combo-{i}:{parity}")

    # Final score calculation – depends only on adjusted_total and fixed offset
    base_score = adjusted_total
    penalty = len(temp_buffer) * 0.1  # minor effect, but distracting
    final_score = int(base_score - penalty + 5)  # deterministic integer result

    # Dead code: never executed but looks important
    def debug_dump():
        return {"raw": data, "buffer_len": len(temp_buffer)}

    return final_score

# Main execution
input_data = [2, 3, 5, 7, 11]
limit = 10

# Call the function and store result
result_cache = {}
result_cache['score'] = compute_aggregate(input_data, limit)

final_score = result_cache['score']
print(f"Result: {final_score}")