import math

def analyze_pattern(sequence):
    # Irrelevant helper: computes statistical spread (not used in final logic)
    mean_val = sum(sequence) / len(sequence)
    variance = sum((x - mean_val) ** 2 for x in sequence) / len(sequence)
    return math.sqrt(variance)


def extract_features(data_chunk):
    # Semi-relevant transformation with distractors
    offset = 17
    adjusted = [x + offset for x in data_chunk]
    shifted = adjusted[2:] + adjusted[:2]  # slicing operation
    filtered = [x for x in shifted if x % 3 == 0]  # only multiples of 3
    
    # Dead computation: no impact on output
    temp_magnitude = sum(x ** 2 for x in filtered) ** 0.5
    
    return shifted  # returns unfiltered version, making filtering irrelevant


def evaluate_thresholds(values):
    # Complex conditional logic with red herring variables
    high_count = 0
    low_count = 0
    trend_flags = []
    
    for v in values:
        if v > 50:
            high_count += 1
            trend_flags.append(True)
        elif v < 30:
            low_count += 1
            trend_flags.append(False)
    
    # Distractor: unused aggregation
    balance_score = high_count - low_count
    flag_streak = 0
    max_streak = 0
    for flag in trend_flags:
        if flag:
            flag_streak += 1
        else:
            max_streak = max(max_streak, flag_streak)
            flag_streak = 0
    max_streak = max(max_streak, flag_streak)
    
    # Actual relevant result
    return len([v for v in values if v > 40])


def calculate_final_score(dataset):
    base_total = sum(dataset)
    correction_factor = 0.85
    penalty = 0
    
    # Nested conditionals with misleading intermediate steps
    if base_total > 200:
        penalty += 10
        temp_adjust = base_total * 0.9
        if temp_adjust % 2 == 0:
            penalty += 5  # never reached due to float nature
    
    # Core logic embedded among distractions
    valid_entries = [x for x in dataset if x >= 15]
    avg_entry = sum(valid_entries) / len(valid_entries) if valid_entries else 0
    
    # Key slicing operation affecting outcome
    segment = valid_entries[1:-1]  # exclude first and last
    segment_avg = sum(segment) / len(segment) if segment else 0
    
    # Final computation using correct path
    score_component = int(avg_entry)
    adjustment = int(segment_avg * 0.5)
    final_score = score_component + adjustment - penalty
    
    return final_score

# Main execution flow
raw_input = [10, 25, 35, 45, 55, 20, 30]
data_profile = analyze_pattern(raw_input)
processed_data = extract_features(raw_input)
consistency_check = evaluate_thresholds(processed_data)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")