import math

# Simulated environmental monitoring system for water quality analysis

def collect_sensor_data():
    # Real data collection (simulated)
    return [
        {'ph': 7.2, 'turbidity': 3.1, 'chlorine': 0.8, 'location': 'north'},
        {'ph': 6.9, 'turbidity': 4.5, 'chlorine': 0.6, 'location': 'south'},
        {'ph': 7.5, 'turbidity': 2.3, 'chlorine': 1.1, 'location': 'east'},
        {'ph': 7.0, 'turbidity': 5.1, 'chlorine': 0.4, 'location': 'west'},
        {'ph': 7.3, 'turbidity': 1.8, 'chlorine': 1.3, 'location': 'central'}
    ]

# Irrelevant auxiliary function - dead code path
def deprecated_normalization(data):
    max_val = max(max(d.values()) for d in data)
    return [{k: v/max_val for k, v in item.items() if isinstance(v, float)} for item in data]

# Unused transformation map
transformation_map = {
    'ph': lambda x: round(math.log(x) * 100, 2),
    'turbidity': lambda x: round(x ** 1.5, 2),
    'chlorine': lambda x: round(math.exp(x) - 2, 2)
}

# Decoy statistical calculator with misleading intermediate results
def compute_redundant_stats(samples):
    avg_ph = sum(s['ph'] for s in samples) / len(samples)
    high_turbidity_count = len([s for s in samples if s['turbidity'] > 4.0])
    total_chlorine = sum(s['chlorine'] for s in samples)
    entropy_proxy = -sum((x/total_chlorine)*math.log(x/total_chlorine) for x in [s['chlorine'] for s in samples])
    # This function returns complex stats but they are not used in final calculation
    return {
        'avg_ph': avg_ph,
        'high_turbidity_count': high_turbidity_count,
        'diversity_index': entropy_proxy
    }

# Red herring: unused advanced filtering algorithm
advanced_filter = lambda sample: all(
    (k != 'turbidity' or v < 4.2) and 
    (k != 'ph' or 6.5 <= v <= 7.5) 
    for k, v in sample.items() if isinstance(v, (int, float))
)

# Real processing begins here
water_samples = collect_sensor_data()

# Misleading normalization (not actually used in final score)
current_state_snapshot = [
    {key: round(value * 1.05, 2) if isinstance(value, float) else value 
     for key, value in sample.items()}
    for sample in water_samples
]

# Conditional branching with distractor logic
if any(s['ph'] > 7.4 for s in water_samples):
    baseline_adjustment = 0.95
else:
    baseline_adjustment = 1.05  # Not ultimately used

# Actual core analysis function
def analyze_purity_levels(samples):
    # Weighted scoring based on normalized deviation from ideal values
    ideal_ph = 7.0
    ideal_turbidity = 1.0
    ideal_chlorine = 1.0
    
    weights = {'ph': 0.3, 'turbidity': 0.5, 'chlorine': 0.2}
    
    # Compute composite deviation scores per sample
    deviations = []
    for s in samples:
        ph_dev = abs(s['ph'] - ideal_ph) * 10  # Scale to 0-10
        turb_dev = min(s['turbidity'], 10)      # Cap at 10
        chlor_dev = abs(s['chlorine'] - ideal_chlorine) * 5
        composite = (
            weights['ph'] * (10 - ph_dev) +
            weights['turbidity'] * (10 - turb_dev) +
            weights['chlorine'] * (10 - chlor_dev)
        )
        deviations.append(composite)
    
    # Sort scores (suggested paradigm)
sorted_deviations = sorted(deviations, reverse=True)
    
    # Apply position-based decay (top samples weighted more)
    decayed_scores = [
        score * (0.95 ** i) for i, score in enumerate(sorted_deviations)
    ]
    
    # Final aggregation using dictionary reduction
    score_summary = {
        'raw_avg': sum(deviations) / len(deviations),
        'weighted_avg': sum(decayed_scores) / len(decayed_scores),
        'max_score': max(decayed_scores),
        'penalty_factor': 0.98 if len([d for d in deviations if d < 6.0]) > 1 else 1.0
    }
    
    # The real answer computation
    result = int(round(score_summary['weighted_avg'] * score_summary['penalty_factor'] * 100))
    return result

# Spurious data transformation (dead code)
filtered_by_lambda = list(filter(lambda x: x['turbidity'] < 4.0, current_state_snapshot))

# Another decoy operation
aggregated_map = {s['location']: {k: v for k, v in s.items() if k != 'location'} 
                 for s in current_state_snapshot}

# Key execution point
filtration_score = analyze_purity_levels(water_samples)

# Print final result as required
print(f"Target result: {filtration_score}")