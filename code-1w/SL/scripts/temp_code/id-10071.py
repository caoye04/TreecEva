from collections import defaultdict
import math

# Simulated system health monitoring with performance evaluation

def analyze_trends(data_points):
    trend_scores = defaultdict(float)
    noise_floor = 0.05
    for i in range(1, len(data_points)):
        delta = data_points[i] - data_points[i-1]
        if abs(delta) > noise_floor:
            if delta > 0:
                trend_scores['upward'] += delta * 0.8
            else:
                trend_scores['downward'] += abs(delta) * 0.6
    return dict(trend_scores)


def compute_entropy(values):
    # Irrelevant entropy calculation (dead code path)
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)


def filter_outliers(stream, threshold=2.5):
    # Distractor: outlier filtering not actually used in main logic
    mean_val = sum(stream) / len(stream)
    std_dev = (sum((x - mean_val)**2 for x in stream) / len(stream))**0.5
    return [x for x in stream if abs(x - mean_val) <= threshold * std_dev]


def derive_insights(dataset):
    # Complex but partially irrelevant transformation
    window_size = 3
    smoothed = []
    for i in range(len(dataset) - window_size + 1):
        segment = dataset[i:i+window_size]
        weighted = sum(segment[j] * (j+1) for j in range(len(segment)))
        normalized = weighted / sum(j+1 for j in range(len(segment)))
        smoothed.append(normalized)
    
    # Dead assignment: misleading intermediate
    derived_meta = {
        'peaks': len([i for i in range(1, len(smoothed)-1) if smoothed[i] > max(smoothed[i-1], smoothed[i+1])]),
        'trend_strength': abs(smoothed[-1] - smoothed[0])
    }
    
    return smoothed


def evaluate_performance(metrics, baseline):
    # Core logic embedded within distractions
    adjustment_factor = 1.75
    penalty_rate = 0.9
    boost_threshold = 0.75
    
    # Key computation chain
    base_value = sum(metrics) / len(metrics)
    deviation = base_value - baseline
    
    # Conditional branching with red herring variables
    volatility = sum(abs(metrics[i] - metrics[i-1]) for i in range(1, len(metrics)))
    phantom_impact = volatility * 0.01  # Unused in final result
    
    if deviation > boost_threshold:
        applied_mod = adjustment_factor
    elif deviation < 0:
        applied_mod = penalty_rate
    else:
        applied_mod = 1.0
    
    # Bit manipulation decoy
    encoded = int(base_value * 100)
    masked = encoded ^ 0xFF  # XOR with 255 - looks important but unused
    extracted = (masked >> 4) & 0x0F  # More bit noise
    
    # Slicing operation (required)
    recent_focus = metrics[-3:]
    recency_bias = sum(recent_focus) / len(recent_focus)
    
    # Final calculation — only some inputs matter
    primary_contrib = base_value * applied_mod
    secondary_contrib = recency_bias * 0.2
    
    # ACTUAL ANSWER DEPENDS ON THIS LINE
    final_score = primary_contrib + secondary_contrib
    
    # Redundant print for distraction
    print(f'Debug: final_score={final_score}, phantom={phantom_impact}, extracted=0x{extracted:x}')
    return final_score

# Simulated telemetry input (realistic domain context)
data_stream = [0.45, 0.52, 0.61, 0.73, 0.67, 0.69, 0.78, 0.82, 0.79]

# Irrelevant preprocessing steps
filtered_data = filter_outliers(data_stream, threshold=1.8)
trend_analysis = analyze_trends(data_stream)
insight_vector = derive_insights(data_stream)
entropy_measure = compute_entropy([int(x*100) for x in data_stream])

# Core metric extraction (only this affects final answer)
working_metrics = [x * 1.1 for x in data_stream]  # Amplify signal
baseline_reference = 0.7

# Entry point: this triggers the key statement
final_score = evaluate_performance(working_metrics, baseline_reference)

# Output required format
print(f"Result: {final_score}")