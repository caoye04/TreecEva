from collections import defaultdict

# Simulate system health monitoring with performance metrics
def collect_telemetry(log_entries):
    stats = defaultdict(int)
    temp_flags = []
    total_entries = 0

    for entry in log_entries:
        level = entry['level']
        code = entry['code']
        stats[level] += 1
        total_entries += 1

        if code > 300:
            temp_flags.append('warning')
        elif code < 100:
            temp_flags.append('info')
        else:
            temp_flags.append('normal')

    # Irrelevant transformation
    flag_summary = ''.join(temp_flags).upper().count('WARNING')
    return stats, total_entries, flag_summary

def normalize_values(raw_stats):
    normalized = {}
    total = sum(raw_stats.values())
    if total == 0:
        return {}
    for k, v in raw_stats.items():
        normalized[k] = round(v / total * 100, 2)
    
    # Dead computation - not used later
    magnitude = sum([v**2 for v in normalized.values()]) ** 0.5
    return normalized

def calculate_entropy(distribution):
    import math
    entropy = 0.0
    for prob in distribution.values():
        if prob > 0:
            entropy -= prob * math.log(prob + 1e-8)
    return round(entropy, 4)

def evaluate_performance(metrics, base):
    score = 0
    offset = metrics.get('ERROR', 0) - base.get('ERROR', 0)
    if offset <= 0:
        score += 10
    else:
        score -= 5 * offset

    if 'CRITICAL' in metrics and metrics['CRITICAL'] == 0:
        score += 15

    active_types = len(metrics)
    score += max(10 - active_types * 2, 0)

    # Distractor logic: computing but not affecting final score directly
    peak_load = max(metrics.values()) if metrics else 0
    avg_load = sum(metrics.values()) / len(metrics) if metrics else 0
    variance_proxy = sum((v - avg_load) ** 2 for v in metrics.values()) / len(metrics) if metrics else 0

    consistency_bonus = 10 if variance_proxy < 50 else 5
    score += consistency_bonus

    return int(score)

# Main execution
log_data = [
    {'level': 'INFO', 'code': 50},
    {'level': 'WARNING', 'code': 150},
    {'level': 'ERROR', 'code': 320},
    {'level': 'INFO', 'code': 80},
    {'level': 'WARNING', 'code': 200},
    {'level': 'ERROR', 'code': 310},
    {'level': 'DEBUG', 'code': 40},
    {'level': 'DEBUG', 'code': 60},
    {'level': 'WARNING', 'code': 180}
]

# Step 1: Collect telemetry
raw_metrics, count, warnings = collect_telemetry(log_data)

# Step 2: Normalize metrics (for display purposes only)
normalized_metrics = normalize_values(raw_metrics)

# Step 3: Calculate entropy (irrelevant to final score but adds cognitive load)
entropy_value = calculate_entropy(normalized_metrics)

# Step 4: Define baseline for comparison
baseline_profile = {
    'ERROR': 3,
    'WARNING': 4,
    'INFO': 2,
    'DEBUG': 2,
    'CRITICAL': 1
}

# Key statement
final_score = evaluate_performance(raw_metrics, baseline_profile)

# Output result
print(f"Result: {final_score}")