def analyze_efficiency(data, threshold=0.75):
    """Irrelevant efficiency analysis function (dead code path)."""
    if not data:
        return 0
    filtered = [x for x in data if x > threshold]
    return len(filtered) / len(data)


def preprocess_inputs(raw_list):
    """Misleading preprocessing with side effects that don't affect final result."""
    temp_processed = []
    offset = 3
    for item in raw_list:
        adjusted = (item + offset) * 2
        if adjusted % 2 == 0:
            temp_processed.append(adjusted // 2)
        else:
            temp_processed.append(adjusted)
    return temp_processed

# Irrelevant global tracking variables (distractors)
counter_tick = 0
status_flags = {"active": True, "debug": False, "stage": 3}

# Core input data — meaningful but obscured by noise
event_log = [12, 8, 15, 6, 9, 11]
baseline = [7, 9, 10, 8, 12, 7]

# Decoy data structures
decoys = {
    'phantom': [1, 3, 5],
    'shadow_metrics': set([22, 14, 19]),
    'dummy_calc': lambda x: x ** 2 + 1
}

# Auxiliary functions with misleading relevance
def calculate_headroom(value, cap=20):
    return cap - value

# Real computation begins here
weight_map = {'precision': 0.4, 'recall': 0.3, 'f1': 0.3}

metrics = {
    'precision': sum(event_log[i] / baseline[i] for i in range(len(baseline)) if baseline[i] != 0) / len(baseline),
    'recall': len([e for e in event_log if e >= 9]) / len(event_log),
    'f1': 0.0  # Will be computed conditionally later
}

benchmark = {
    'thresholds': {'min_precision': 0.7, 'min_recall': 0.5},
    'weights': weight_map,
    'bonus_active': False
}

# Simulated conditional f1-score calculation (irrelevant due to bonus_active=False)
temp_f1 = 0.0
if metrics['precision'] > 0 and metrics['recall'] > 0:
    temp_f1 = 2 * (metrics['precision'] * metrics['recall']) / (metrics['precision'] + metrics['recall'])

if benchmark['bonus_active']:
    metrics['f1'] = temp_f1
else:
    metrics['f1'] = 0.65  # Hardcoded fallback

# Red herring: complex bit manipulation with no downstream impact
critical_flag = 0b10101
shifted = (critical_flag << 3) & 0b11111
checksum = shifted ^ 0b11001

# Another decoy structure
task_queue = [{'id': 'A', 'prio': 2}, {'id': 'B', 'prio': 1}]
for entry in task_queue:
    entry['prio'] += counter_tick  # counter_tick is always 0

# Real scoring logic buried in distractions
def evaluate_performance(performance_dict, config):
    score = 0.0
    w = config['weights']
    t = config['thresholds']
    
    # Apply weighted sum
    score += performance_dict['precision'] * w['precision']
    score += performance_dict['recall'] * w['recall']
    score += performance_dict['f1'] * w['f1']
    
    # Apply threshold bonus (not triggered)
    if performance_dict['precision'] >= t['min_precision'] and performance_dict['recall'] >= t['min_recall']:
        score += 0.1
    
    # Hidden adjustment: case conversion on dummy string affects nothing
    mode_str = "AdJuStScOrE".lower().upper().title()  # Result: "Adjustscore"
    
    # Final scaling to integer-like float output
    return round(score * 1000, 4)

# Key execution point
final_score = evaluate_performance(metrics, benchmark)

# Output required format
print(f"Target result: {final_score}")