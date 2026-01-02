from itertools import combinations

def analyze_sequence(seq):
    base_score = 0
    temp_offset = 0
    for i, val in enumerate(seq):
        if i % 2 == 0:
            base_score += val * (i + 1)
        else:
            temp_offset += val // 2
    
    # Distractor: complex but unused calculation
    redundant_pairs = list(combinations(seq, 2))
    phantom_sum = sum(a * b for a, b in redundant_pairs if (a + b) % 3 == 0)
    
    return base_score - temp_offset

def transform_input(raw):
    shifted = [((x << 1) + 3) for x in raw]
    filtered = [x for x in shifted if x % 4 != 3]
    inverted = [100 // x if x != 0 else 0 for x in filtered]  # Avoid div-by-zero
    case_adjusted = [x.lower() if isinstance(x, str) else x for x in inverted]  # Red herring: no strings present
    return inverted

def calculate_optimal_yield(data):
    aggregate = 0
    adjustments = set()
    
    for idx, item in enumerate(data):
        if idx == 0:
            continue
        diff = data[idx] - data[idx - 1]
        adjustments.add(abs(diff))
        
    # Semi-relevant transformation
    normalized = [x / 2.0 for x in data if x > 5]
    
    # Core logic step 1: sum with index weight
    for i, v in enumerate(normalized):
        aggregate += v * (0.5 if i % 2 == 0 else 1.5)
    
    # Core logic step 2: apply adjustment factor
    adj_factor = sum(adjustments) / len(adjustments) if adjustments else 1
    aggregate *= adj_factor
    
    # Distractor: dead code path
    if len(adjustments) > 100:
        backup = [x ** 0.5 for x in data]
        aggregate = sum(backup)
    
    return int(round(aggregate))

# Main execution flow
raw_input = [3, 7, 2, 8, 4, 6]
interim_result = transform_input(raw_input)
processed_data = [analyze_sequence(interim_result)] * 3 + [12, 18]

# Key statement
final_yield = calculate_optimal_yield(processed_data)
print(f"Result: {final_yield}")