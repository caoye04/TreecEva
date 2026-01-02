def analyze_trend(data, window):
    trends = []
    for i in range(len(data) - window + 1):
        segment = data[i:i + window]
        avg = sum(segment) / window
        trend = 1 if segment[-1] > avg else -1
        trends.append(trend)
    return trends

# Simulate sensor data drift over time
data_stream = [23.5, 24.1, 23.9, 24.6, 25.2, 26.0, 25.8, 26.3, 27.1, 27.4]

def adjust_threshold(base, factor=1.05):
    # Irrelevant helper function for noise adjustment
    return base * factor

def calculate_volatility(prices):
    changes = [abs(prices[i+1] - prices[i]) for i in range(len(prices)-1)]
    return sum(changes) / len(changes) if changes else 0

volatility_index = calculate_volatility(data_stream)  # Unused distraction
adjusted_levels = [adjust_threshold(x) for x in data_stream]  # Dead computation path

# Core evaluation logic
baseline_metrics = {
    'stability': 85,
    'response_time': 42,
    'consistency': 78,
    'drift_count': 3
}

weights = {'stability': 0.3, 'response_time': 0.2, 'consistency': 0.35, 'drift_count': 0.15}

# Misleading normalization block (not actually used)
temp_normalized = {}
for k, v in baseline_metrics.items():
    temp_normalized[k] = v / 100.0 if k != 'drift_count' else (10 - v) / 10.0

# Real processing with slicing and accumulation
def extract_key_periods(series, length=4):
    mid_point = len(series) // 2
    early_phase = series[:mid_point]
    late_phase = series[mid_point:]
    return late_phase[-length:]  # Most recent period slice

recent_data = extract_key_periods(data_stream)
event_count = len([x for x in recent_data if x > 25.0])

# Simulated recursive scoring
def recursive_impact(depth, base):
    if depth <= 0:
        return 1
    return base * recursive_impact(depth - 1, base - 0.1)

impact_factor = recursive_impact(3, 1.2)  # Minor influence on final score

# Main scoring function combining multiple concepts
def evaluate_performance(metrs, wts):
    score = 0.0
    penalty = 0.0
    
    # Direct metric contributions
    for key, val in metrs.items():
        if key in wts:
            contribution = val * wts[key]
            score += contribution
    
    # Conditional bonus based on event count from sliced data
    if event_count >= 2:
        bonus = 7.5 * impact_factor
        score += bonus
    
    # Artificial penalty layer (mostly unused)
    if metrs['drift_count'] > 2:
        penalty += 5.0
    
    # Final adjustment using irrelevant volatility index (no effect due to comment)
    # score -= volatility_index * 0.5  
    
    return round(score - penalty, 4)

final_score = evaluate_performance(baseline_metrics, weights)
print(f"Result: {final_score}")