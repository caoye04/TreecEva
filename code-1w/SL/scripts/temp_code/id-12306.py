from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i, char in enumerate(sequence):
        if char.lower() == 'a' and (i + 1) % 3 == 0:
            count += 1
    return count

def transform_data(raw):
    transformed = []
    temp_sum = 0
    for idx, val in enumerate(raw):
        if idx % 2 == 0:
            transformed.append(val * 2)
        else:
            transformed.append(val + 1)
        temp_sum += val  # Irrelevant accumulator
    avg_val = temp_sum / len(raw) if raw else 0
    return transformed

def filter_and_combine(data_list):
    filtered = [x for x in data_list if x > 10]
    pairs = list(combinations(filtered, 2))
    pair_sums = [sum(p) for p in pairs]
    return pair_sums if pair_sums else [0]

def compute_final_score(data):
    base = sum(data) // len(data)
    bonus = 0
    for item in data:
        if item > 15:
            bonus += 2
        elif item > 5:
            bonus += 1
    return base + bonus

# Main execution flow
raw_input = [3, 7, 4, 12, 9, 16, 8]
processed_data = transform_data(raw_input)

# Side computation - irrelevant to final result
string_analysis = "AlgorithmicPattern"
dummy_count = analyze_pattern(string_analysis)
intermediate_pairs = filter_and_combine(processed_data)
extra_metric = sum(intermediate_pairs[:3]) if len(intermediate_pairs) >= 3 else 0

# Key statement
final_score = compute_final_score(processed_data)
print(f"Result: {final_score}")