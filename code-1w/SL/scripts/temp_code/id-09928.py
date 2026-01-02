from itertools import combinations

def analyze_pattern(sequence):
    # Irrelevant helper: counts vowels in string representation of numbers
    str_seq = ''.join(map(str, sequence))
    vowel_count = sum(1 for c in str_seq if c.lower() in 'aeiou')

    # Distractor: generates all 2-combinations but only uses count
    combo_count = len(list(combinations(sequence, 2)))

    # Semi-relevant transformation
    transformed = [x ** 2 - x for x in sequence]

    # Actual signal: sum of even-indexed elements after transformation
    signal_value = sum(transformed[i] for i in range(0, len(transformed), 2))

    # Dead code path (never executed)
    if False:
        signal_value *= -1

    return signal_value


def compute_aggregate(data_string, multiplier):
    # Parse input string into list of integers
    raw_values = list(map(int, data_string.split(',')))

    # Slice operation: reverse and take first half
    reversed_half = raw_values[::-1][:len(raw_values)//2]

    # Count occurrences of max value (distractor)
    max_val = max(reversed_half) if reversed_half else 0
    max_count = sum(1 for x in reversed_half if x == max_val)

    # Another distractor: conditional expression based on length parity
    adjustment = 10 if len(raw_values) % 2 == 0 else 5

    # Key computation chain
    base_score = sum(x for x in raw_values if x > 0)
    penalty = sum(abs(x) for x in raw_values if x < 0)
    normalized = (base_score - penalty) // max(1, adjustment)

    # Use of analyze_pattern on a derived sequence
    pattern_input = [normalized, len(raw_values), multiplier]
    pattern_score = analyze_pattern(pattern_input)

    # Final score with irrelevant scaling
    scaling_factor = len(raw_values) / (multiplier or 1)
    final_score = int((normalized + pattern_score) * (1 + 0.1 * (scaling_factor > 2)))

    return final_score

# Main execution
input_data = "3,-2,7,1,8,-5,4"
multiplier_param = 3

intermediate_result = compute_aggregate(input_data, multiplier_param)
final_score = compute_aggregate(input_data, multiplier_param)

print(f"Result: {final_score}")