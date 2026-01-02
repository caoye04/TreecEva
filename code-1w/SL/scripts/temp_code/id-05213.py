def analyze_pattern(sequence):
    if not sequence:
        return 0
    
    # Irrelevant transformation (distractor)
    transformed = list(map(lambda x: (x ** 2 + 3) % 7, sequence))
    count_even = sum(1 for x in sequence if x % 2 == 0)
    total_shift = 0
    
    for i in range(len(transformed)):
        if i % 3 == 0:
            total_shift += transformed[i] >> 1

    # Real computation starts here
    base_value = sum(sequence[i] for i in range(0, len(sequence), 2))
    adjustment = len([x for x in sequence if x > 5]) * 2
    
    temp_result = base_value - adjustment
    
    # Simulate data filtering
    filtered = sequence[1:-1]  # Slicing operation
    if len(filtered) > 2:
        mid_values = filtered[len(filtered)//3 : 2*len(filtered)//3]
        temp_result += sum(mid_values) // 2
    
    return temp_result


def process_results(data, limit):
    score = 0
    penalty = 0
    
    # Dead code path (misleading)
    if limit < 0:
        return -1
    
    for val in data:
        if val >= limit:
            score += val // 3
        else:
            # This block is never reached due to data generation
            penalty += 1

    # Key early break (affects logic flow)
    temp_array = [i * 2 for i in range(6)]
    for x in temp_array:
        if x > 10:
            break
        score += x % 4
    
    # Red herring calculation
    fake_aggregate = sum(x**0.5 for x in temp_array if x % 2 == 0) / (len(temp_array) or 1)
    
    # Final relevant adjustment
    multiplier = 2 if score > 20 else 1
    final = (score * multiplier) - penalty
    
    return final

# Main execution
raw_input = [4, 7, 2, 9, 5, 8, 6]
collected_data = []
threshold = 6

for n in raw_input:
    result = analyze_pattern(list(range(n)))
    collected_data.append(result)

# Misleading normalization step
normalized = [round(x / 4.0) * 4 for x in collected_data]
placeholder_sum = sum(normalized)  # Unused variable

# Critical statement
final_score = process_results(collected_data, threshold)

print(f"Result: {final_score}")