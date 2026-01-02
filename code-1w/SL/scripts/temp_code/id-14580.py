from collections import defaultdict
import math

def analyze_log(text_log):
    lines = text_log.split('\n')
    log_data = defaultdict(int)
    char_count = 0

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        
        # Irrelevant but plausible processing
        words = stripped.split(' ')
        log_data['word_lines'] += len(words) > 3
        
        for char in stripped:
            if char.isalpha():
                char_count += 1

        if 'ERROR' in stripped:
            log_data['errors'] += 1
        elif 'INFO' in stripped:
            log_data['info_count'] += 1

    # Distractor computation
    avg_chars_per_line = char_count / len(lines) if lines else 0
    redundancy_factor = math.log(1 + log_data['info_count'])

    return dict(log_data), char_count, avg_chars_per_line


def calculate_efficiency(raw_ops, duration):
    if duration <= 0:
        return 0
    base_efficiency = (raw_ops / duration) * 0.75
    penalty = 0
    
    # Simulate complex branching logic with red herrings
    thresholds = [10, 50, 100]
    for t in thresholds:
        if raw_ops > t:
            penalty += 0.01
    
    adjusted = base_efficiency - penalty
    return max(adjusted, 0.1)

# Simulated system log
system_log = '''
INFO: System started
INFO: User login successful
ERROR: File not found
INFO: Backup initiated
ERROR: Timeout on request
'''

# Parse log
log_summary, total_chars, avg_length = analyze_log(system_log)
error_count = log_summary.get('errors', 0)

# Performance metrics
operations = 86
elapsed_time = 12.5
efficiency = calculate_efficiency(operations, elapsed_time)

# Secondary distractor analysis
character_frequency = defaultdict(int)
for c in system_log.lower():
    if c in 'abcdefghijklmnopqrstuvwxyz':
        character_frequency[c] += 1
vowel_count = sum(character_frequency[v] for v in 'aeiou')
consonant_ratio = (total_chars - vowel_count) / total_chars if total_chars else 0

# Core logic chain
baseline = 50
adjustment = 0
if error_count == 0:
    adjustment = 20
elif error_count == 1:
    adjustment = 10
elif error_count == 2:
    adjustment = -15  # Critical threshold
else:
    adjustment = -30

# Final evaluation with dependency on prior steps
def evaluate_performance(eff, err):
    base = baseline + adjustment
    eff_bonus = int(eff * 2) if eff > 5 else 0
    error_penalty = err * 5
    temp_result = base + eff_bonus - error_penalty
    
    # More distractions
    intermediate_values = []
    for i in range(3):
        intermediate_values.append(temp_result + (i * 2))
    
    final_value = temp_result + len(intermediate_values)
    return final_value

final_score = evaluate_performance(efficiency, error_count)
Result: {final_score}