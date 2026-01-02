from collections import defaultdict
from itertools import zip_longest

# Simulate user engagement metrics across multiple platforms
def analyze_engagement Trends(raw_logs):
    daily_stats = defaultdict(lambda: {'views': 0, 'likes': 0, 'shares': 0})
    platform_summary = {platform: 0 for platform in ['web', 'mobile', 'tablet']}

    for entry in raw_logs:
        day, platform, actions = entry
        daily_stats[day]['views'] += actions.get('view', 0)
        daily_stats[day]['likes'] += actions.get('like', 0)
        daily_stats[day]['shares'] += actions.get('share', 0)
        if platform in platform_summary:
            platform_summary[platform] += sum(actions.values())

    # Irrelevant transformation (distractor)
    normalized = {k: {ik: iv / (sum(v.values()) + 1) for ik, iv in v.items()} 
                  for k, v in daily_stats.items()}

    return daily_stats, platform_summary

# Weighted ranking system with decay function
def apply_decay(rank_list, decay_factor=0.9):
    return [score * (decay_factor ** i) for i, score in enumerate(rank_list)]

# Core scoring logic
def calculate_composite_rank(metrics_dict):
    composite_scores = []
    for day_data in metrics_dict.values():
        base_score = day_data['views'] * 0.5 + day_data['likes'] * 0.3 + day_data['shares'] * 0.2
        bonus = 5 if day_data['shares'] > 100 else 0
        penalty = 3 if day_data['views'] < 50 else 0
        composite_scores.append(base_score + bonus - penalty)
    
    # Apply decay to prioritize recent activity
    decayed_scores = apply_decay(sorted(composite_scores, reverse=True))
    return sum(decayed_scores)

# Final aggregation with irrelevant helper
def calculate_final_score(rank_data, weights):
    total = 0
    weight_sum = sum(weights)
    
    # Real computation
    for i, (key, val) in enumerate(rank_data.items()):
        weighted_val = val * weights[i % len(weights)]
        total += weighted_val

    # Dead code path (distractor)
    temp_buffer = [0] * 100
    for i in range(len(temp_buffer) - 1):
        temp_buffer[i+1] = temp_buffer[i] + i
    buffer_checksum = sum(x * x for x in temp_buffer if x % 10 == 0)

    # Unused statistical calculation (distractor)
    avg = sum(rank_data.values()) / len(rank_data) if rank_data else 0
    variance_proxy = sum(abs(v - avg) for v in rank_data.values())

    return int(total // 1.8)  # Final transformation

# Main execution
if __name__ == '__main__':
    # Input data: (day, platform, actions)
    logs = [
        (1, 'web', {'view': 120, 'like': 15, 'share': 25}),
        (1, 'mobile', {'view': 80, 'like': 20, 'share': 30}),
        (2, 'tablet', {'view': 200, 'like': 40, 'share': 60}),
        (3, 'web', {'view': 180, 'like': 35, 'share': 45}),
        (4, 'mobile', {'view': 95, 'like': 10, 'share': 15}),
        (5, 'web', {'view': 250, 'like': 50, 'share': 80}),
        (6, 'tablet', {'view': 70, 'like': 5, 'share': 5}),
        (7, 'web', {'view': 300, 'like': 60, 'share': 105})
    ]

    # Extract meaningful metrics
    engagement_metrics, _ = analyze_engagement_Trends(logs)
    
    # Compute time-decayed composite ranks
    composite_ranking = calculate_composite_rank(engagement_metrics)
    
    # Prepare ranked data for final score (key step)
    sorted_ranks = sorted(engagement_metrics.items(), key=lambda x: x[1]['views'], reverse=True)
    rank_data = {f'day_{k}': int(v['views'] * 0.1 + v['shares']) for k, v in sorted_ranks}
    
    # Weights with partial use (only length matters, values not all used)
    weights = [0.7, 1.2, 0.9, 1.5]
    
    # Critical statement
    final_score = calculate_final_score(rank_data, weights)
    
    print(f"Result: {final_score}")