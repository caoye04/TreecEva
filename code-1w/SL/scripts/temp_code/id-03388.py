def analyze_pattern(sequence):
    count_vowels = 0
    temp_sum = 0
    positions = []
    for idx, char in enumerate(sequence):
        if char.lower() in 'aeiou':
            count_vowels += 1
            positions.append(idx)
        temp_sum += ord(char) % 7
    
    # Distractor: complex but unused vowel analysis
    vowel_gap_sum = 0
    for i in range(1, len(positions)):
        vowel_gap_sum += positions[i] - positions[i-1]
    
    return count_vowels


def evaluate_threshold(value, baseline):
    adjustment = 0
    if value > baseline * 1.5:
        adjustment = 10
    elif value < baseline * 0.5:
        adjustment = -5
    else:
        adjustment = 3
    # Dead code path (never reached due to else)
    if False:
        adjustment *= 2
    return adjustment


def calculate_final_score(data, thresholds):
    raw_totals = []n    intermediate_flags = set()
    total_chars = 0
    
    for entry in data:
        total_chars += len(entry)
        vowels = analyze_pattern(entry)
        raw_totals.append(vowels * 100)
        
        # Semi-relevant string transformation
        reversed_str = ''.join(reversed(entry))
        if any(c.isdigit() for c in reversed_str):
            intermediate_flags.add('digit_present')

    # Real computation begins here
    base_score = sum(raw_totals) // len(data) if data else 0
    
    # Use of zip and enumerate with mixed relevance
    adjustments = []
    for i, (raw, threshold) in enumerate(zip(raw_totals, thresholds)):
        excess = raw - threshold
        if excess > 0:
            adj = evaluate_threshold(excess, threshold)
            adjustments.append(adj)
        else:
            adjustments.append(0)
    
    # Distractor: complex average that isn't used
    avg_adjustment = sum(adjustments) / len(adjustments) if adjustments else 0
    temp_result = 0
    for x in adjustments:
        temp_result += x ** 2
    unused_root_mean_sq = temp_result ** 0.5
    
    # Final score depends only on base_score and first adjustment
    final_score = base_score + (adjustments[0] if adjustments else 0)
    
    # Critical print statement
    print(f"Result: {final_score}")
    return final_score

# Input data
input_data = ['algorithm', 'function', 'variable', 'lambda']
threshold_values = [300, 800, 400, 700]

# Execution point
final_score = calculate_final_score(input_data, threshold_values)