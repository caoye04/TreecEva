def analyze_productivity(logs):
    total_chars = 0
    action_count = 0
    error_flags = []
    temp_sum = 0

    for log in logs:
        stripped = log.strip()
        if not stripped.startswith('DEBUG'):
            total_chars += len(stripped)
            action_count += 1
            if 'ERROR' in stripped:
                error_flags.append(len(stripped))

    # Distractor computation: average length of non-DEBUG lines (not used later)
    avg_length = total_chars / action_count if action_count else 0

    # Real signal: count of ERROR occurrences
    error_count = len(error_flags)

    return total_chars, error_count


def calculate_efficiency(raw_input, baseline):
    # Normalize input
    cleaned = raw_input.lower().replace('-', '').replace('_', '')
    digit_sum = sum(int(c) for c in cleaned if c.isdigit())
    
    # Distractor: character frequency analysis (unused)
    freq_map = {}
    for c in cleaned:
        freq_map[c] = freq_map.get(c, 0) + 1
    
    # Efficiency score based on digit sum and baseline
    efficiency_score = (digit_sum * 100) // baseline if baseline else 0
    return efficiency_score

# Main execution
log_data = [
    'INFO: user login successful',
    'DEBUG: system heartbeat',
    'WARNING: low memory',
    'ERROR: database timeout',
    'INFO: file upload complete'
]

input_token = 'a5b2c3-d4e1f'
baseline_value = 15

# Extract productivity metrics
productivity, errors = analyze_productivity(log_data)

# Compute auxiliary metric (some distraction)
candidate_ranks = [productivity // (errors + 1)]
for i in range(2):
    candidate_ranks.append(candidate_ranks[-1] // 2)

# Compute efficiency
efficiency = calculate_efficiency(input_token, baseline_value)

# Final performance evaluation
status_flags = set(['ACTIVE', 'VERIFIED'])
bonus = 10 if 'VERIFIED' in status_flags else 0

scaling_factor = 0.85
final_score = 0
final_score += productivity * 0.1
final_score -= errors * 5
final_score += efficiency * 0.5
final_score += bonus
final_score = int(final_score * scaling_factor)

Result: final_score