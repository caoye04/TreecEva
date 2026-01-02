def analyze_pattern(sequence):
    frequency = {c: sequence.count(c) for c in set(sequence)}
    max_char = max(frequency, key=frequency.get)
    return frequency[max_char]


def validate_sequence(seq):
    if len(seq) < 5:
        return False
    unique_chars = len(set(seq))
    avg_count = len(seq) / unique_chars
    return avg_count > 2.0


def calculate_performance(data):
    # Irrelevant intermediate computation (distractor)
    temp_buffer = [x * 2 for x in data if x % 3 == 0]
    temp_sum = sum(temp_buffer) // 2 if temp_buffer else 0
    
    # Core logic: count even numbers above threshold
    filtered_values = [x for x in data if x > 25 and x % 2 == 0]
    base_score = len(filtered_values)
    
    # Secondary logic: sum of squares of odd numbers below 20
    auxiliary_total = sum(x**2 for x in data if x < 20 and x % 2 == 1)
    adjustment_factor = auxiliary_total // 10 if auxiliary_total > 0 else 0
    
    # Tertiary distraction: string-based pattern analysis on hex representation
    hex_string = ''.join([hex(n)[-1] for n in data])
    pattern_repetition = analyze_pattern(hex_string)
    noise_offset = pattern_repetition * 2 if validate_sequence(hex_string) else -1
    
    # Final calculation with interdependent components
    final_score = base_score + adjustment_factor - noise_offset
    
    # Dead code path (never executed under normal input)
    if temp_sum > 1000:
        final_score *= 2  # Unreachable in practice
        
    return final_score

# Input data
benchmark_data = [12, 15, 26, 27, 30, 33, 34, 35, 36, 11, 13, 17]

# Execute
final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")