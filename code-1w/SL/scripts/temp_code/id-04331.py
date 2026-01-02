import math

# Simulated system performance analyzer (distractor: not actually used)
def compute_latency_score(response_times):
    avg = sum(response_times) / len(response_times)
    return 100 - (avg * 5) if avg < 20 else 50

def analyze_user_engagement(actions):
    # Real function but unused path
    counts = {}
    for a in actions:
        counts[a] = counts.get(a, 0) + 1
    return max(counts.values()) if counts else 0

# Irrelevant data structures
temp_logs = [
    {'event': 'login', 'ts': 1623456780},
    {'event': 'view', 'ts': 1623456789},
    {'event': 'logout', 'ts': 1623456801}
]

user_data = {
    'id': 'usr-7x3k9',
    'region': 'NA-West',
    'tier': 'premium',
    'joined_days_ago': 365,
    'activity_log': ['click', 'scroll', 'hover', 'click', 'click']
}

# Core metric dictionary with mixed relevance
metrics = {
    'response_time_avg': 12.4,
    'error_rate': 0.023,
    'throughput': 890,
    'uptime_ratio': 0.997,
    'concurrent_users': 153,
    'cache_hit_ratio': 0.87,
    'retry_count': 4
}

# Dead functions and decoys
def validate_config(cfg):
    return isinstance(cfg, dict) and 'version' in cfg

def normalize_value(v):
    return round(v * 100) / 100

# Unused transformation chain
intermediate_results = []
for key, val in metrics.items():
    if 'ratio' in key:
        intermediate_results.append(val * 100)

snapshot = ''.join([str(int(v)) for v in metrics.values() if isinstance(v, (int, float)) and v > 10])
snapshot_hash = sum([ord(c) for c in snapshot]) % 97

# Real processing begins here
def evaluate_stability(mt):
    score = 50
    if mt['uptime_ratio'] > 0.99:
        score += 30
    if mt['error_rate'] < 0.03:
        score += 15
    if mt['retry_count'] < 5:
        score += 5
    return score

def evaluate_efficiency(mt):
    score = 0
    if mt['response_time_avg'] < 15:
        score += 40
    if mt['throughput'] > 800:
        score += 35
    if mt['cache_hit_ratio'] > 0.85:
        score += 15
    return score

def calculate_user_impact(data):
    base = len(data['activity_log'])
    modifiers = {
        'premium': 1.5,
        'standard': 1.0,
        'basic': 0.7
    }
    multiplier = modifiers.get(data['tier'], 1.0)
    return int(base * multiplier)

def process_performance(m, u):
    stability = evaluate_stability(m)
    efficiency = evaluate_efficiency(m)
    
    # Distractor: complex string operation with no impact
    tier_code = u['tier'][:3].upper()
    id_sum = sum([ord(c) for c in u['id']])
    magic_offset = (id_sum % 11) - 5
    
    # Real logic with conditional override
    base_score = stability + efficiency
    
    # Conditional adjustment based on user impact
    impact = calculate_user_impact(u)
    if impact >= 6:
        adjusted = base_score * 1.2
    else:
        adjusted = base_score * 0.9
    
    # Final clamping and rounding
    final = min(max(round(adjusted), 50), 200)
    
    # Red herring: modifying unused list
    temp_logs.append({'event': 'analysis_complete', 'score': final})
    
    # This is the actual target variable
    final_score = final + magic_offset  # Only magic_offset affects result, others are distractions
    
    return final_score

# Execution point of interest
final_score = process_performance(metrics, user_data)

# Output required format
print(f"Result: {final_score}")