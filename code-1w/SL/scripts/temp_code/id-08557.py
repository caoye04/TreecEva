from itertools import combinations, chain
from math import log, ceil

# Simulated dataset: user engagement metrics across multiple platforms
user_metrics = [
    {'id': 101, 'clicks': 45, 'dwell_time': 120, 'conversions': 3, 'platform': 'A'},
    {'id': 102, 'clicks': 67, 'dwell_time': 95, 'conversions': 1, 'platform': 'B'},
    {'id': 103, 'clicks': 23, 'dwell_time': 300, 'conversions': 4, 'platform': 'A'},
    {'id': 104, 'clicks': 89, 'dwell_time': 60, 'conversions': 0, 'platform': 'C'},
    {'id': 105, 'clicks': 55, 'dwell_time': 210, 'conversions': 2, 'platform': 'B'},
]

# Irrelevant statistical decoy: computes unused entropy measure
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * log(p) for p in probs)

entropy_decoy = compute_entropy([len(user_metrics), 10, 5])

# Misleading transformation: looks important but unused later
transformed_metrics = []
for um in user_metrics:
    temp = um.copy()
    temp['engagement_ratio'] = (um['clicks'] * 1.5 + um['dwell_time'] * 0.1) / (um['conversions'] + 1)
    temp['tier'] = 'high' if temp['engagement_ratio'] > 50 else 'low'
    transformed_metrics.append(temp)

# Decoy function that is never called
def generate_combinations(data):
    ids = [d['id'] for d in data]
    return list(combinations(ids, 2))

# Auxiliary function to filter high-conversion users (used indirectly)
def get_high_conversion_users(metrics):
    return [m for m in metrics if m['conversions'] >= 2]

# Bit manipulation red herring: simulates 'performance flags'
def calculate_performance_flags(clicks, dwell):
    base_flag = (clicks & 0xFF) ^ (dwell >> 2)
    return (base_flag << 1) | (base_flag >> 7)

# Attach flags unnecessarily
for m in user_metrics:
    m['flag'] = calculate_performance_flags(m['clicks'], m['dwell_time'])

# Real processing begins here — filtering and aggregation
filtered_data = get_high_conversion_users(user_metrics)

# Extract platform A users for secondary analysis (partially relevant)
platform_a_set = {u['id'] for u in user_metrics if u['platform'] == 'A'}
unused_intersection = set(chain(*[combinations(platform_a_set, 2)]))  # Dead computation

# Core feature engineering
def extract_features(user_list):
    clicks_list = [u['clicks'] for u in user_list]
    time_list = [u['dwell_time'] for u in user_list]
    conv_list = [u['conversions'] for u in user_list]
    
    avg_clicks = sum(clicks_list) / len(clicks_list)
    max_dwell = max(time_list)
    total_conversions = sum(conv_list)
    
    # Hidden dependency: uses bitwise to mask noise
    magic_offset = (total_conversions ^ 0x5A) & 0xFF
    adjusted_avg = avg_clicks + (magic_offset * 0.01)
    
    return {
        'adjusted_avg': adjusted_avg,
        'max_dwell': max_dwell,
        'count': len(user_list),
        'total_conv': total_conversions
    }

# Apply feature extraction
features = extract_features(filtered_data)

# Secondary decoy: complex set logic with no impact
all_ids = {u['id'] for u in user_metrics}
dropped_ids = {102, 104}
surviving_pairs = set(combinations(all_ids - dropped_ids, 2))
pair_count_estimate = ceil(len(surviving_pairs) * 0.1)  # Unused

# Real signal path: compute composite score
intermediate_vals = []
for i in range(features['count']):
    val = (features['adjusted_avg'] * (i + 1)) / (features['max_dwell'] / 100 + 1)
    intermediate_vals.append(val)

aggregate_signal = sum(intermediate_vals) * features['total_conv']

# Final nonlinear scaling using logarithmic bias correction
def compute_final_score(data_dict):
    raw = aggregate_signal
    bias_factor = log(features['max_dwell'] + 1) / 5
    corrected = raw * (1 + bias_factor)
    return int(corrected)  # Deterministic integer output

# Key execution point
processed_data = features
final_score = compute_final_score(processed_data)

print(f"Result: {final_score}")