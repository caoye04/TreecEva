def calculate_performance(data):
    # Preprocessing: extract relevant metrics
    raw_values = [x['metric'] for x in data if x['active']]
    
    # Irrelevant distraction: compute unused stats
    avg_value = sum(raw_values) / len(raw_values) if raw_values else 0
    max_value = max(raw_values) if raw_values else 0
    min_value = min(raw_values) if raw_values else 0
    spike_count = len([i for i in range(1, len(raw_values)) if raw_values[i] - raw_values[i-1] > 3])

    # Distractor: string-based tagging (not used in final logic)
    tags = "".join(["H" if v > avg_value else "L" for v in raw_values[:5]])
    tag_analysis = tags.lower().replace("h", "high").split("high")

    # Core logic begins: analyze trend stability
    diffs = [raw_values[i] - raw_values[i-1] for i in range(1, len(raw_values))]
    stable_window = [d for d in diffs if abs(d) <= 1.5]
    
    # Apply conditional weighting using slicing and thresholds
    recent_trend = raw_values[-3:]
    weight = 1.8 if sum(recent_trend) / 3 > avg_value else 1.2
    
    # Secondary distraction: simulate unused prediction
    projected_next = raw_values[-1] + (sum(diffs[-3:]) / 3) if len(diffs) >= 3 else raw_values[-1]
    confidence = "high" if abs(projected_next - raw_values[-1]) < 2 else "low"

    # Key computation path
    base_score = sum(stable_window)
    bonus = len(recent_trend) * 2.5 if all(x > 10 for x in recent_trend) else 0
    penalty = len([d for d in diffs if d < -2]) * 1.7
    
    # Final score calculation
    final_score = base_score * weight + bonus - penalty
    
    return final_score

# Input data setup
dataset = [
    {'metric': 12.1, 'active': True},
    {'metric': 12.3, 'active': True},
    {'metric': 11.9, 'active': True},
    {'metric': 12.0, 'active': True},
    {'metric': 12.2, 'active': True},
    {'metric': 9.8, 'active': True},
    {'metric': 10.1, 'active': True},
    {'metric': 14.0, 'active': True},
    {'metric': 14.1, 'active': True},
    {'metric': 13.9, 'active': True}
]

# Execute critical statement
final_score = calculate_performance(dataset)
print(f"Result: {final_score}")