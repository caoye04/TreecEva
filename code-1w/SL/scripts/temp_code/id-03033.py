def analyze_text_patterns(input_str):
    char_count = {}
    for c in input_str:
        char_count[c] = char_count.get(c, 0) + 1
    
    vowels = 'aeiou'
    vowel_total = sum(char_count.get(v, 0) for v in vowels)
    consonant_total = len(input_str) - vowel_total - char_count.get(' ', 0)
    
    # Distractor: unused statistical measure
    avg_frequency = sum(char_count.values()) / len(char_count) if char_count else 0
    
    return vowel_total, consonant_total, len(input_str.split())


def compute_efficiency(tasks_completed, time_spent):
    if time_spent == 0:
        return 0
    base_efficiency = tasks_completed / time_spent
    penalty = 0.1 * (tasks_completed // 5)  # Diminishing returns
    return max(base_efficiency - penalty, 0.5)


def evaluate_performance(metrics, factor):
    accuracy = metrics['accuracy']
    consistency = metrics['consistency']
    completeness = metrics['completeness']
    
    # Core logic
    raw_score = (accuracy * 0.4) + (consistency * 0.3) + (completeness * 0.3)
    adjusted = raw_score * factor
    
    # Distractor: irrelevant normalization branch
    if adjusted > 100:
        adjusted = 100 + (adjusted - 100) / 10  # barely applicable
    
    # Additional distraction: dead code path
    temp_debug = [x for x in range(5) if x > 10]
    
    return int(round(adjusted))

# Simulate task environment
log_data = "completed task alpha, then beta, followed by gamma completion"
tokens = log_data.split(', ')
task_count = len(tokens)
duration = 25  # minutes

# Extract linguistic features for side analysis
vowels, consonants, word_groups = analyze_text_patterns(log_data)
side_ratio = vowels / consonants if consonants else 0

# Performance metrics (some values derived, some fixed)
base_metrics = {
    'accuracy': 92.5,
    'consistency': 88.0,
    'completeness': 94.0,
    'redundancy_check': task_count * 2  # unused field
}

# Efficiency factor influenced by text structure
noise_chars = log_data.count(' ') + log_data.count(',')
useful_chars = len(log_data) - noise_chars
character_utilization = useful_chars / len(log_data)
efficiency_factor = compute_efficiency(task_count, duration) * character_utilization

# State tracking with red herring variables
state_log = []
for i in range(3):
    state_log.append(f'Stage {i+1}: active')

# Key execution point
final_score = evaluate_performance(base_metrics, efficiency_factor)

# Print result as required
print(f"Target result: {final_score}")