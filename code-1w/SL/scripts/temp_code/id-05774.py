from itertools import combinations

# Simulate cognitive task assessment with distraction handling
def analyze_sequence(seq):
    total = 0
    bonus = 0
    temp_tracker = []

    for i, val in enumerate(seq):
        if i % 3 == 0:
            total += val * 2
        elif i % 3 == 1 and val > 5:
            total += val // 2
        else:
            total -= val % 4

        # Distractor: tracking unused pattern
        if val % 2 == 0:
            temp_tracker.append(val + i)

    # Meaningless aggregation
    combo_sum = 0
    for combo in combinations(temp_tracker[:4], 2) if len(temp_tracker) >= 4 else [()]:
        if combo:
            combo_sum += combo[0] + combo[1] - 1  # Irrelevant to final result

    return total

# Auxiliary function with red herring parameters
def adjust_metrics(data, scale=1.5, offset=3, debug_mode=False):
    adjusted = []
    noise_accum = 0

    for x in data:
        transformed = (x * scale) + offset
        if transformed > 20:
            noise_accum += transformed % 7  # Dead-end accumulation
        adjusted.append(int(transformed))
    
    # Unused diagnostic info
    if debug_mode:
        print(f'Diagnostic: noise={noise_accum}')

    return adjusted

# Core processing with embedded logic chain
def process_results(raw_data):
    base_values = [analyze_sequence(chunk) for chunk in raw_data]
    
    # Distractor: string-based metadata parsing
    metadata_tags = "err_threshold@7;mode=strict;fmt=hex"
    tag_pairs = {tag.split("=")[0]: tag.split("=")[1] for tag in metadata_tags.split(";") if "=" in tag}
    err_limit = int(tag_pairs.get("err_threshold", 5).split("@")[1])

    scaled_data = adjust_metrics(base_values)

    # Key state variables
    running_total = 0
    penalty = 0
    peak_value = max(scaled_data) if scaled_data else 0

    for idx, value in enumerate(scaled_data):
        if value > peak_value * 0.75:
            running_total += value * (idx + 1)
        elif idx % 2 == 0:
            running_total += value
        else:
            penalty += value % 3

        # Fake branching logic
        if value < 10:
            _ = value ** 2 - 1  # Unused computation

    # Final adjustment using modular arithmetic and conditional override
    intermediate = (running_total - penalty) % 97
    if intermediate % 2 == 0:
        final_score = intermediate + 5
    else:
        final_score = intermediate - 3

    return final_score

# Input data setup
sequence_batch = [
    [3, 8, 1, 6, 4, 9, 2],
    [7, 5, 3, 8, 6],
    [9, 2, 4, 7, 1, 5]
]

# Execute main logic
temp_analysis = [sum(seq) for seq in sequence_batch]  # Irrelevant pre-scan
normalization_factor = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 1

final_score = process_results(sequence_batch)
print(f"Result: {final_score}")