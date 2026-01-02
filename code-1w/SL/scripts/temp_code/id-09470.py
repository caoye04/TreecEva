from collections import defaultdict

# Simulate agricultural yield analysis across microplots
def analyze_microplot_trends(raw_observations):
    plot_stats = defaultdict(lambda: {'count': 0, 'total_yield': 0})
    temp_aggregate = 0
    
    for obs in raw_observations:
        plot_id = obs['plot']
        season = obs['season']
        yield_amt = obs['yield']
        
        if season == 'dry' and yield_amt < 150:
            continue
            
        plot_stats[plot_id]['count'] += 1
        plot_stats[plot_id]['total_yield'] += yield_amt
        temp_aggregate += yield_amt * 0.1  # Irrelevant dampening factor

    return dict(plot_stats)

# Calculate efficiency with conditional logic and distractors
def calculate_harvest_efficiency(data, base_threshold):
    efficiency_map = {}
    adjustment_factor = 1.25
    dummy_sum = 0
    outlier_count = 0

    aggregated_totals = [sum(d['total_yield'] for d in data.values())]

    for pid, stats in data.items():
        count = stats['count']
        total = stats['total_yield']
        average = total / count if count else 0

        # Distractor: complex but unused seasonal weight
        seasonal_weight = 1.1 if pid.startswith('X') else 0.9
        weighted_avg = average * seasonal_weight
        dummy_sum += weighted_avg

        # Actual logic path
        if average > base_threshold:
            status = 'high'
        elif average > base_threshold * 0.7:
            status = 'moderate'
        else:
            status = 'low'
            outlier_count += 1

        efficiency_map[pid] = {
            'avg': average,
            'status': status
        }

    # Secondary processing with red herring variables
    high_performers = [k for k, v in efficiency_map.items() if v['status'] == 'high']
    suppression_factor = 0.8 if len(high_performers) > 2 else 1.0

    total_efficient_yield = sum(v['avg'] for v in efficiency_map.values() if v['status'] != 'low')
    adjustment_applied = total_efficient_yield * adjustment_factor * suppression_factor

    final_yield = int(adjustment_applied + 0.5)  # Final deterministic answer

    # Dead code branch (never reached in normal execution)
    if False:
        backup_estimator = dummy_sum * 2.1
        final_yield = int(backup_estimator)

    return final_yield

# Input data - fixed and deterministic
field_data_raw = [
    {'plot': 'A1', 'season': 'wet', 'yield': 210},
    {'plot': 'A1', 'season': 'dry', 'yield': 130},
    {'plot': 'A2', 'season': 'wet', 'yield': 195},
    {'plot': 'A2', 'season': 'wet', 'yield': 220},
    {'plot': 'B1', 'season': 'dry', 'yield': 110},
    {'plot': 'B1', 'season': 'wet', 'yield': 180},
    {'plot': 'C1', 'season': 'wet', 'yield': 230},
    {'plot': 'C1', 'season': 'wet', 'yield': 240},
    {'plot': 'C2', 'season': 'dry', 'yield': 100},
    {'plot': 'D1', 'season': 'wet', 'yield': 160}
]

# Process observations
processed_stats = analyze_microplot_trends(field_data_raw)
threshold = 175
final_yield = calculate_harvest_efficiency(processed_stats, threshold)
print(f"Result: {final_yield}")