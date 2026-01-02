def analyze_trends(data, threshold=10):
    trend_flags = []
    temp_accum = 0
    for i, value in enumerate(data):
        if value > threshold:
            temp_accum += value * 0.1
            trend_flags.append((i, True))
        else:
            temp_accum -= 1
            trend_flags.append((i, False))
    return temp_accum, trend_flags


def preprocess_inputs(raw_series):
    cleaned = [x for x in raw_series if isinstance(x, (int, float)) and x >= 0]
    offset = sum(cleaned) // len(cleaned) if cleaned else 0
    adjusted = [x - offset + 2 for x in cleaned]
    return adjusted


def calculate_performance(entries):
    base_points = 0
    penalty = 0
    shift_factor = 3
    
    # Irrelevant tracking (distractor)
    state_log = []
    buffer_val = 0
    
    for idx, item in enumerate(entries):
        if idx % 2 == 0:
            base_points += item ^ shift_factor  # XOR operation
        else:
            base_points += item >> 1
        
        # Dead computation branch (semi-relevant but not used)
        if item < 5:
            buffer_val += item * 2
            state_log.append(f'Low: {item}')

        # Actual key logic
        if item >= 8:
            penalty += 1
    
    # Secondary processing with zip (python idiom)
    paired = list(zip(entries[::2], entries[1::2]))
    bonus = 0
    for a, b in paired:
        if a + b > 10:
            bonus += 2

    # Final score calculation
    final_score = base_points - penalty + bonus
    
    # Unused variables (distractors)
    debug_info = f'State complete: {len(state_log)} events'
    temp_result = buffer_val * 0.5
    
    return final_score

# Main execution
raw_input = [12, 3, 7, 9, 4, 8, 6, 11]
benchmark_data = preprocess_inputs(raw_input)
extra_noise = analyze_trends(benchmark_data)
score_snapshot = []
final_score = calculate_performance(benchmark_data)
score_snapshot.append(final_score)
print(f"Result: {final_score}")