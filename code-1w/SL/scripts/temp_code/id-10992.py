from collections import defaultdict
import itertools

def preprocess_records(raw_entries):
    # Irrelevant transformation (distractor)
    temp_mapping = {k: v * 1.5 for k, v in raw_entries.items()}
    filtered = {k: v for k, v in raw_entries.items() if v > 10}
    return filtered

def extract_segments(data_dict):
    segments = []
    total_sum = 0  # Unused accumulator (distractor)
    for key, value in data_dict.items():
        if len(key) % 2 == 0:
            segments.append(value * 2)
        else:
            segments.append(value + 3)
    return segments

def group_by_parity(values):
    grouped = defaultdict(list)
    for v in values:
        grouped[v % 2].append(v)
    return dict(grouped)

def calculate_final_score(segments):
    score = 0
    intermediate_log = []  # Dead storage (distractor)
    
    # Real computation begins
    for val in segments:
        if val < 25:
            score += val // 2
        elif val >= 25 and val < 50:
            score += val - 20
        else:
            score += 10
    
    # Misleading complex-looking but unused operation
    combo_pairs = list(itertools.combinations_with_replacement(segments, 2))
    avg_pair_sum = sum(a + b for a, b in combo_pairs) / len(combo_pairs) if combo_pairs else 0
    
    # Final adjustment based on length
    if len(segments) > 4:
        score -= 5
    
    return score

# Main execution flow
raw_data = {'ax': 12, 'byy': 15, 'cz': 8, 'dxxx': 22, 'e': 30}
filtered_data = preprocess_records(raw_data)
segment_list = extract_segments(filtered_data)
grouped_values = group_by_parity(segment_list)

# Key statement
final_score = calculate_final_score(segment_list)

print(f"Result: {final_score}")