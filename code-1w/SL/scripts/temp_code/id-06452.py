from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == 'A' and i % 2 == 0:
            count += 1
    return count

def transform_values(raw_list):
    temp_result = []
    offset = 7
    for num in raw_list:
        transformed = (num * 2) + offset
        if transformed % 3 == 0:
            temp_result.append(transformed // 3)
        else:
            temp_result.append(transformed)
    # Irrelevant filtering
    filtered = [x for x in temp_result if x > 10]
    return temp_result

def generate_pairs(data):
    return list(combinations(data, 2))

def calculate_optimal_yield(metrics):
    base_score = 0
    adjustment = 0.0
    
    for val in metrics:
        if val > 25:
            base_score += val
        elif val < 10:
            adjustment -= 1.5
    
    # Distractor: complex-looking but unused calculation
    redundant_calc = sum([x**2 for x in metrics if x % 4 == 0])
    dummy_tracker = set()
    for v in metrics:
        dummy_tracker.add(v % 5)
    
    final_yield = base_score + adjustment
    return final_yield

# Main execution
raw_sequence = "ABACADAF"
irrelevant_count = analyze_pattern(raw_sequence)

primary_values = [4, 8, 15, 16, 23, 42]
processed_data = transform_values(primary_values)

# Unused pair generation - adds cognitive load
pairs = generate_pairs(processed_data)

# Key statement
final_yield = calculate_optimal_yield(processed_data)

print(f"Result: {final_yield}")