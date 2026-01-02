import math

# Irrelevant helper function (decoy)
def compute_legacy_metric(x):
    return sum(xi ** 0.5 for xi in x) * 0.33

# Misleading data transformation (distractor)
def transform_signal(data):
    shifted = [math.sin(d / 10) * 2 for d in data]
    normalized = [(s + 2) / 4 for s in shifted]
    return [round(n * 100) for n in normalized]

# Unused but plausible preprocessing function
def filter_outliers(values, threshold=1.5):
    median_val = sorted(values)[len(values)//2]
    return [v for v in values if abs(v - median_val) < threshold]

# Core logic disguised among distractions
def analyze_efficiency(records, config):
    base = sum(r['value'] for r in records)
    adjustment = len(records) % 7
    if adjustment > 4:
        base -= adjustment * 2
    else:
        base += adjustment
    return base * config.get('multiplier', 1.0)

# Another red herring: complex frequency counter with no impact
def count_transitions(seq):
    freq = {}
    for i in range(len(seq)-1):
        key = f'{seq[i]}->{seq[i+1]}'
        freq[key] = freq.get(key, 0) + 1
    total = sum(freq.values())
    return {k: v/total for k, v in freq.items()} if total else {}

def evaluate_performance(metrics, profile):
    # Real computation begins here — obscured by prior noise
    
    # Extract relevant features from nested structure
    raw_values = [m['reading'] for m in metrics if m['active']]
    
    # Conditional expression used meaningfully
    scaling_factor = 2.5 if profile['tier'] == 'advanced' else 1.2
    
    # Slicing operation on filtered data
    recent_subset = raw_values[-5:]  # Last five readings only
    
    # Dictionary accumulation with filtering
    stats = {}
    for val in recent_subset:
        bucket = 'high' if val > 80 else ('medium' if val > 50 else 'low')
        stats[bucket] = stats.get(bucket, 0) + 1
    
    # Actual answer depends on medium-count and scaling
    medium_count = stats.get('medium', 0)
    preliminary = medium_count * 17
    
    # Final calculation hidden in conditional expression
    final_score = preliminary * scaling_factor if profile['enabled'] else 0
    
    # Dead code path (never reached due to above)
    if not profile.get('enabled', True):
        fallback = sum(transform_signal(raw_values)) // len(raw_values)
        final_score = fallback - 5
    
    return int(final_score)

# Simulated input data with decoys
user_profile = {
    'tier': 'advanced',
    'enabled': True,
    'preferences': {'theme': 'dark', 'notifications': False},
    'legacy_id': 8821,
    'creation_year': 2019
}

metric_data = [
    {'reading': 45, 'active': True, 'timestamp': '2023-01-01', 'source': 'A'},
    {'reading': 52, 'active': True, 'timestamp': '2023-01-02', 'source': 'B'},
    {'reading': 61, 'active': True, 'timestamp': '2023-01-03', 'source': 'A'},
    {'reading': 49, 'active': True, 'timestamp': '2023-01-04', 'source': 'C'},
    {'reading': 85, 'active': True, 'timestamp': '2023-01-05', 'source': 'A'},
    {'reading': 30, 'active': False, 'timestamp': '2023-01-06', 'source': 'B'},  # inactive
    {'reading': 74, 'active': True, 'timestamp': '2023-01-07', 'source': 'C'}
]

# Auxiliary unused list comprehension (distraction)
summary_stats = [
    {'period': metric['timestamp'], 'impact': math.log(metric['reading'] + 1)}
    for metric in metric_data if metric['source'] == 'A'
]

# Key execution point
final_score = evaluate_performance(metric_data, user_profile)

# Print result as required
print(f"Target result: {final_score}")