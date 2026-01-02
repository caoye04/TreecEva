from itertools import compress, count

def analyze_performance(log_data, threshold=50):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.05 for x in log_data if x > 0]
    outliers = [x for x in normalized if x > 100]
    filtered = [x for x in normalized if x <= 100]

    # Semi-relevant transformation
    adjusted = [int(x + 0.75) for x in filtered]

    # Key logic: identify high performers above dynamic threshold
    index_counter = count(1)
    indexed_scores = list(zip(adjusted, index_counter))
    above_threshold = list(compress(indexed_scores, (s >= threshold for s, _ in indexed_scores)))

    # Extract only scores, discard indices after use
    high_performers = [score for score, idx in above_threshold]

    # Distractor: unused branch with dead code
    if len(outliers) > 10:
        backup_result = sum(outliers) // len(outliers)
    else:
        temp_offset = sum(1 for x in adjusted if x < 20)
        adjustment = temp_offset * 2

    return high_performers

def calculate_penalty(level, base=3):
    # Simple recursion as red herring
    if level <= 1:
        return base
    return base + calculate_penalty(level - 1, base - 1)

def process_results(entries, penalty_multiplier):
    # String manipulation distractor
    tag = ''.join(['p', 'e', 'n', '_', 'c', 't', 'r', 'l']).upper()
    version_info = "v1.4b"
    version_digits = [int(d) for d in version_info if d.isdigit()]
    offset = sum(version_digits)

    # Core calculation masked by noise
    raw_total = sum(entries)
    count_bonus = len(entries) * 5
    raw_score = raw_total + count_bonus

    # Actual penalty application
    applied_penalty = raw_score * penalty_multiplier
    final_score = raw_score - applied_penalty

    # Unused intermediate
    checksum = raw_score ^ applied_penalty

    return int(final_score)

# Main execution flow
log_input = [45, 60, 52, 15, 88, 73, 5, 91, 44, 67, 23, 58]
penalty_factor = calculate_penalty(4) / 10  # Results in 0.6

valid_entries = analyze_performance(log_input, threshold=55)

# Critical statement
final_score = process_results(valid_entries, penalty_factor)

print(f"Result: {final_score}")