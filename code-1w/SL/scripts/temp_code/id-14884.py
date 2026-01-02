from collections import Counter, defaultdict

def analyze_performance(logs):
    counts = Counter()
    trend = []
    for entry in logs:
        action = entry['action']
        status = entry['status']
        counts[action] += 1
        if status == 'success':
            trend.append(1)
        else:
            trend.append(-1)
    
    # Distractor: irrelevant aggregation
    failure_rate = len([x for x in logs if x['status'] == 'fail']) / len(logs) if logs else 0
    avg_run_duration = sum(entry.get('duration', 1) for entry in logs) / len(logs) if logs else 0

    return dict(counts), trend

def generate_ranking_metrics(base_counts):
    total_actions = sum(base_counts.values())
    normalized = {k: v / total_actions for k, v in base_counts.items()}
    
    # Distractor: unused transformation
    inverted = {k: 1 / (v + 0.1) for k, v in normalized.items()}
    
    ranking = sorted(normalized.keys(), key=lambda x: normalized[x], reverse=True)
    rank_map = {item: idx + 1 for idx, item in enumerate(ranking)}
    
    return rank_map, normalized

def calculate_trend_momentum(trend):
    if not trend:
        return 0.0
    
    momentum = 0
    decay = 0.9
    for i, val in enumerate(reversed(trend)):
        momentum += val * (decay ** i)
    
    # Distractor: alternative calculation not used
    peak_runs = max(sum(1 for x in trend[i:i+3] if x == 1) for i in range(len(trend)-2)) if len(trend) >= 3 else 0
    
    return round(momentum, 4)

def calculate_final_score(ranks, trend_signal):
    base_score = 0
    for task, rank in ranks.items():
        if 'deploy' in task.lower():
            base_score += 10 / rank
        elif 'build' in task.lower():
            base_score += 5 / rank
        else:
            base_score += 1 / rank
    
    adjustment = sum(trend_signal) * 0.25
    final = base_score + adjustment
    
    # Distractor: redundant intermediate
    scaled_final = final * 1.05
    capped_final = min(scaled_final, 100)
    
    return int(round(final))

# Main execution
log_data = [
    {'action': 'build_module', 'status': 'success', 'duration': 120},
    {'action': 'deploy_staging', 'status': 'success', 'duration': 80},
    {'action': 'run_tests', 'status': 'fail', 'duration': 60},
    {'action': 'build_module', 'status': 'success', 'duration': 110},
    {'action': 'deploy_production', 'status': 'success', 'duration': 200},
    {'action': 'backup_data', 'status': 'success', 'duration': 300},
    {'action': 'deploy_staging', 'status': 'fail', 'duration': 90},
    {'action': 'build_docs', 'status': 'success', 'duration': 40},
    {'action': 'deploy_staging', 'status': 'success', 'duration': 85}
]

# Extract performance data
count_summary, performance_trend = analyze_performance(log_data)

# Generate ranking system
rankings, norms = generate_ranking_metrics(count_summary)

# Calculate derived trend index
trend_index = calculate_trend_momentum(performance_trend)

# Final score computation - KEY STATEMENT
final_score = calculate_final_score(rankings, performance_trend)

# Output result
print(f"Result: {final_score}")