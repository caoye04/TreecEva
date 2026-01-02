from collections import defaultdict, Counter

# Simulate user feedback analysis for a coding tutor system
def analyze_feedback_patterns(feedback_log):
    pattern_count = defaultdict(int)
    temp_tracker = []
    total_entries = 0
    ignored_counter = 0  # Distractor: not used in final logic

    for entry in feedback_log:
        if len(entry) > 2:
            key_char = entry[0].lower()
            if key_char in 'abcde':
                pattern_count[key_char] += 1
                total_entries += 1
            else:
                temp_tracker.append(entry)  # Logged but unused
        else:
            continue  # Minor dead path

    return pattern_count, total_entries

# Scoring logic with red herrings
def compute_raw_metrics(data):
    char_freq = Counter(''.join(data).lower())
    bonus_points = 0
    penalty = 0
    phantom_sum = 0  # Distractor variable

    for char, count in char_freq.items():
        if char in 'aeiou':
            bonus_points += count * 1.5
        elif char.isalpha():
            penalty += count * 0.7
        phantom_sum += count ** 0.5  # Computation with no impact

    base_score = bonus_points - penalty
    return base_score  # Only this matters

# Secondary validator (not actually used but looks important)
def validate_consistency(patterns):
    expected_keys = set('abcde')
    missing = expected_keys - set(patterns.keys())
    consistency_ratio = (5 - len(missing)) / 5
    debug_values = [len(missing), consistency_ratio]  # Unused
    return consistency_ratio > 0.6

# Main evaluation pipeline
def evaluate_performance(feedback_sequence):
    # Step 1: Extract patterns
    patterns, total_valid = analyze_feedback_patterns(feedback_sequence)
    
    # Step 2: Compute metrics
    raw_score = compute_raw_metrics(feedback_sequence)
    
    # Step 3: Apply scaling based on volume (only uses total_valid indirectly)
    volume_factor = min(total_valid / 10.0, 1.0)  # Caps at 10 entries
    adjusted_score = raw_score * volume_factor
    
    # Step 4: Conditional boost (never triggers due to data, but looks relevant)
    if validate_consistency(patterns) and total_valid > 15:
        adjusted_score *= 1.2
    
    # Step 5: Final normalization
    normalized = round(adjusted_score + 5, 2)  # Add constant offset
    
    # Irrelevant transformation chain
    temp_result = normalized * 1.05
    temp_result = int(temp_result // 1)
    temp_result = float(temp_result)  # Back to float, no effect
    
    # Final score assignment
    final_score = int(temp_result)  # Cast to int for discrete scoring
    
    # Extra unused variables to increase cognitive load
    summary_report = {"score": final_score, "entries": total_valid}
    export_timestamp = "2023-12-15T10:30:00Z"  # Dead variable
    
    return final_score

# Input data with mixed valid and invalid entries
feedback_input = [
    "Error: syntax issue",      # -> 'e' counts
    "Bug in loop logic",       # -> 'b' counts
    "Exception occurred",     # -> 'e' counts
    "Assertion failed",       # -> 'a' counts
    "Edge case missed",       # -> 'e' counts
    "Compilation error",      # -> 'c' counts
    "Null pointer",           # -> 'n' → ignored
    "Timeout",                # -> 't' → ignored
    "Bad input format",       # -> 'b' counts
    "Stack overflow"          # -> 's' → ignored
]

# Execute main logic
result_dict = {}
interim_list = []
for item in feedback_input:
    if 'error' in item.lower() or 'exception' in item.lower():
        interim_list.append(item)

# Critical execution point
temp_var = sum(len(x) for x in interim_list)  # Distractor computation
final_score = evaluate_performance(feedback_input)
print(f"Result: {final_score}")