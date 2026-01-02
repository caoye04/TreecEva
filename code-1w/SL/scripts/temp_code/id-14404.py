from collections import defaultdict

# Simulated user engagement metrics across different platforms
engagement_data = [
    {'platform': 'A', 'clicks': 120, 'views': 300, 'region': 'North'},
    {'platform': 'B', 'clicks': 85,  'views': 250, 'region': 'South'},
    {'platform': 'A', 'clicks': 200, 'views': 600, 'region': 'North'},
    {'platform': 'C', 'clicks': 45,  'views': 90,  'region': 'East'},
    {'platform': 'B', 'clicks': 110, 'views': 400, 'region': 'South'},
    {'platform': 'C', 'clicks': 130, 'views': 390, 'region': 'East'},
]

# Auxiliary data not directly used in final computation
user_satisfaction = [4.2, 4.5, 3.9, 4.7, 4.1, 4.6]
satisfaction_avg = sum(user_satisfaction) / len(user_satisfaction)
temp_multiplier = satisfaction_avg * 0.1

# Threshold for minimum CTR (Click-Through Rate)
threshold = 0.35

# Aggregation helper
platform_stats = defaultdict(lambda: {'total_clicks': 0, 'total_views': 0})

for record in engagement_data:
    platform = record['platform']
    platform_stats[platform]['total_clicks'] += record['clicks']
    platform_stats[platform]['total_views'] += record['views']

# Compute click-through rates per platform
ctr_values = {}
for platform, stats in platform_stats.items():
    ctr = stats['total_clicks'] / stats['total_views']
    ctr_values[platform] = round(ctr, 4)

# Identify underperforming platforms
underperforming = [p for p, ctr in ctr_values.items() if ctr < threshold]

# Dummy transformation (distractor)
dummy_transform = [round(val**0.5, 2) for val in ctr_values.values() if val > 0.2]

# Weight assignment based on performance
weights = {}
baseline_weight = 1.0
for p in ['A', 'B', 'C']:
    if p in underperforming:
        weights[p] = baseline_weight * 0.6
    else:
        weights[p] = baseline_weight * 1.2

# Secondary distraction: region-based adjustment (not used in final path)
region_contribution = defaultdict(int)
for record in engagement_data:
    region_contribution[record['region']] += record['clicks'] * 0.01

# Core processing function
def process_metrics(data, min_ctr):
    # Recompute effective CTRs
    clicks = sum(d['clicks'] for d in data)
    views = sum(d['views'] for d in data)
    overall_ctr = clicks / views
    
    # Apply penalty if below threshold
    if overall_ctr < min_ctr:
        penalty = 0.85
    else:
        penalty = 1.0
    
    # Bonus based on data diversity (number of unique platforms)
    unique_platforms = len(set(d['platform'] for d in data))
    diversity_bonus = 1 + (unique_platforms * 0.05)
    
    # Base score before adjustments
    base_score = clicks * 0.1 + views * 0.05
    
    # Apply adjustments
    adjusted_score = base_score * penalty * diversity_bonus
    
    # Red herring operation (no effect)
    _ = [x for x in range(1, 10) if x % 2 == 0]
    
    # Final scaling
    final_score = int(round(adjusted_score * 1.15))
    
    return final_score

# Execute main logic
interim_result = ctr_values['A'] * 1000  # unused beyond this
flagged_count = len(underperforming)

final_score = process_metrics(engagement_data, threshold)

# Print result as required
print(f"Target result: {final_score}")