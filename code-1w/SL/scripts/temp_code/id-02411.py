from itertools import combinations

def analyze_segments(data_window):
    peak_moments = []
    baseline = sum(data_window) / len(data_window)
    
    for i, value in enumerate(data_window):
        if value > baseline * 1.1:
            peak_moments.append(i)
    
    # Irrelevant combination analysis (distractor)
    irrelevant_pairs = list(combinations(peak_moments, 2))
    pair_count = len(irrelevant_pairs)
    
    return peak_moments

def calculate_volatility(seq):
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    return avg_diff

def normalize_sequence(raw_seq):
    min_val, max_val = min(raw_seq), max(raw_seq)
    if max_val == min_val:
        return [0 for _ in raw_seq]
    return [(x - min_val) / (max_val - min_val) for x in raw_seq]

def compute_final_score(clean_data):
    volatility = calculate_volatility(clean_data)
    normalized = normalize_sequence(clean_data)
    
    # Dummy tracking variables (semi-relevant)
    adjustment_factor = 0.0
    if len(clean_data) > 5:
        adjustment_factor = 0.8
    else:
        adjustment_factor = 1.2
    
    score_components = []
    for norm_val in normalized:
        if norm_val > 0.5:
            score_components.append(norm_val * 100 * adjustment_factor)
    
    temp_offset = sum([i * 0.1 for i in range(len(score_components))])  # Distractor
    final_score = int(sum(score_components) - temp_offset)
    
    return final_score

# Main execution block
raw_input = [34, 87, 45, 92, 51, 70, 65]
processed_data = []

# Simulate preprocessing stages
for idx, val in enumerate(raw_input):
    if val % 2 == 0:
        processed_data.append(val - 5)
    else:
        processed_data.append(val + 3)

# Additional irrelevant set operation (distractor)
duplicate_check = set(raw_input)
size_check = len(duplicate_check)
expected_size = len(raw_input)

# Key computation
final_score = compute_final_score(processed_data)
print(f"Result: {final_score}")