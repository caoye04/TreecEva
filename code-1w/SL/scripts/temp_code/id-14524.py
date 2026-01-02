from collections import defaultdict, Counter

# Simulate a codebase analyzing developer sprint performance across multiple metrics
def analyze_sprint_efficiency(dev_logs):
    efficiency_map = defaultdict(float)
    error_count = 0

    for log in dev_logs:
        dev_id = log['id']
        commits = log['commits']
        bugs = log['bugs_resolved']
        hours = log['hours_active']

        # Real metric: velocity score
        if hours > 0:
            base_velocity = (commits * 2 + bugs) / hours
        else:
            base_velocity = 0

        # Distractor: unused complexity
        temp_factor = commits ** 0.5 if commits > 0 else 0
        penalty = 0.1 * error_count  # Never updated, red herring

        efficiency_map[dev_id] += base_velocity

        # Irrelevant accumulation
        shadow_accumulator = 0
        for i in range(2):  # Artificial loop depth
            for j in range(3):
                shadow_accumulator += (i + j) % 2

    return efficiency_map


def rank_developers(efficiency_map):
    sorted_pairs = sorted(efficiency_map.items(), key=lambda x: x[1], reverse=True)
    rankings = {item[0]: idx + 1 for idx, item in enumerate(sorted_pairs)}
    
    # Dead code path - looks relevant but unused
    if len(rankings) > 100:
        fallback = sum(rankings.values()) // len(rankings)
    else:
        fallback = -1  # Unused

    return rankings

def calculate_performance_trend(metrics):
    trend_accum = 0.0
    for val in metrics:
        trend_accum += val * 0.9
    return trend_accum  # Computed but not used later

# Additional distractor function
def compute_theoretical_capacity(n):
    if n <= 1:
        return 1
    return n * compute_theoretical_capacity(n - 1)  # Unused recursion

# Main logic starts here
log_data = [
    {'id': 'D01', 'commits': 15, 'bugs_resolved': 8, 'hours_active': 20},
    {'id': 'D02', 'commits': 12, 'bugs_resolved': 10, 'hours_active': 18},
    {'id': 'D03', 'commits': 20, 'bugs_resolved': 5, 'hours_active': 25},
    {'id': 'D04', 'commits': 18, 'bugs_resolved': 12, 'hours_active': 22}
]

# Step 1: Analyze sprint efficiency
efficiency_scores = analyze_sprint_efficiency(log_data)

# Step 2: Generate rankings
rankings = rank_developers(efficiency_scores)

# Step 3: Prepare auxiliary metrics (some irrelevant)
performance_metrics = []
for dev_id in ['D01', 'D02', 'D03', 'D04']:
    raw_score = efficiency_scores[dev_id]
    adjusted = raw_score * (1.1 if rankings[dev_id] < 3 else 0.95)
    performance_metrics.append(adjusted)

# Distractor: complex unused structure
aggregated_stats = {
    'max_efficiency': max(efficiency_scores.values()),
    'min_rank': min(rankings.values()),
    'size_hint': len(log_data) * 3 // 2,
    'phantom_key': compute_theoretical_capacity(5)  # Calls recursive dead code
}

# Another red herring computation
historical_weights = [0.8, 1.0, 0.9, 1.1]
weighted_sum = sum(a * b for a, b in zip(performance_metrics, historical_weights))  # Not used

# Core final calculation with moderate nesting and dictionary use
bonus_multiplier = defaultdict(lambda: 1.0)
for dev_id, rank in rankings.items():
    if rank == 1:
        bonus_multiplier[dev_id] = 1.25
    elif rank == 2:
        bonus_multiplier[dev_id] = 1.15
    else:
        bonus_multiplier[dev_id] = 1.05

# Final score computation — this is the critical path
base_total = sum(efficiency_scores.values())
tier_bonus = 0
for dev_id in rankings:
    normalized_rank = rankings[dev_id]
    multiplier = bonus_multiplier[dev_id]
    tier_bonus += efficiency_scores[dev_id] * (multiplier - 1)

# Key statement
final_score = base_total + tier_bonus

# Output result as required
Result: {final_score}