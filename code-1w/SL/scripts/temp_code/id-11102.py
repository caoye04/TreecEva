from collections import defaultdict, Counter

# Simulated system log analysis with performance metrics
def analyze_log_integrity(log_entries):
    integrity_map = defaultdict(int)
    for idx, entry in enumerate(log_entries):
        if 'ERROR' in entry:
            integrity_map['errors'] += 1
        elif 'WARNING' in entry:
            integrity_map['warnings'] += 1
        if len(entry) > 50:
            integrity_map['long_entries'] += 1
    return dict(integrity_map)

# Irrelevant helper: counts character frequency (distractor)
def character_frequency(text_list):
    freq = Counter()
    for text in text_list:
        freq.update(text.lower())
    return freq

# Misleading data transformation (dead path)
def transform_legacy_data(data):
    shifted = []
    for item in data:
        transformed = ''.join(chr((ord(c) - 97 + 3) % 26 + 97) if c.isalpha() else c for c in item)
        shifted.append(transformed)
    return shifted

# Decoy function that looks important but is unused
def compute_system_health(health_logs):
    score = 0
    for log in health_logs:
        if 'CRITICAL' in log:
            score -= 10
        elif 'INFO' in log:
            score += 1
    return score / len(health_logs) if health_logs else 0

# Core logic disguised among distractors
def evaluate_stability_factors(entries):
    stability_weights = {}
    for i, entry in enumerate(entries):
        weight = 1.0
        if 'INIT' in entry:
            weight *= 0.8
        if 'SYNC' in entry:
            weight *= 1.2
        if i % 4 == 0:
            weight *= 1.1
        stability_weights[f'entry_{i}'] = round(weight, 4)
    return stability_weights

# Main aggregation function - key to answer
def aggregate_performance(log_entries, system_flags):
    # Step 1: Count relevant event types
    event_counts = {'init': 0, 'sync': 0, 'halt': 0}
    for entry in log_entries:
        if 'INIT' in entry:
            event_counts['init'] += 1
        if 'SYNC' in entry:
            event_counts['sync'] += 1
        if 'HALT' in entry:
            event_counts['halt'] += 1

    # Step 2: Compute base metric
    base_metric = (event_counts['init'] * 3) + (event_counts['sync'] * 7)

    # Step 3: Apply flag modifiers
    modifier = 1.0
    if system_flags.get('overclock', False):
        modifier += 0.25
    if system_flags.get('secure_mode', True):
        modifier -= 0.1
    if system_flags.get('debug_trace', False):
        modifier += 0.05

    adjusted_metric = base_metric * modifier

    # Step 4: Stability bonus from evaluation
    stability_scores = evaluate_stability_factors(log_entries)
    bonus = sum(v * 0.5 for k, v in stability_scores.items() if 'entry_' in k)

    # Step 5: Final composition
    final_score = int(round(adjusted_metric + bonus - (event_counts['halt'] * 5)))

    # Irrelevant string manipulation (distractor)
    labels = ['node_a', 'node_b', 'node_c']
    indexed_labels = {i: label.upper() for i, label in enumerate(labels)}
    paired = list(zip(indexed_labels.values(), [x[::-1] for x in labels]))

    # Unused complex structure (red herring)
    decoy_matrix = [[i * j for j in range(3)] for i in range(3)]

    # Another distraction: character frequency on logs (never used)
    _ = character_frequency(log_entries)

    # Critical print statement
    return final_score

# Input data
log_entries = [
    'INIT process sequence at node A',
    'SYNC timestamp alignment SUCCESS',
    'NORMAL operation within tolerance',
    'SYNC recalibration triggered',
    'INIT secondary subsystems',
    'HALT emergency shutdown received',
    'SYNC global clock sync achieved',
    'DEBUG memory dump initiated'
]

system_flags = {
    'overclock': True,
    'secure_mode': True,
    'debug_trace': False,
    'legacy_compat': True,
    'verbose_logging': True
}

# Execution point of interest
final_score = aggregate_performance(log_entries, system_flags)
print(f"Target result: {final_score}")