def analyze_trend(values):
    if len(values) < 3:
        return False
    trend = all(values[i] <= values[i+1] for i in range(len(values)-1))
    volatility = sum(abs(values[i+1] - values[i]) for i in range(len(values)-1))
    return trend and volatility < 50

# Irrelevant helper (distractor)
def calculate_entropy(data):
    import math
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Unused function (dead code path)
def normalize_vector(vec):
    magnitude = sum(x**2 for x in vec) ** 0.5
    return [x / magnitude for x in vec] if magnitude else vec

# Misleading intermediate computation
temp_records = [12, 15, 18, 22, 25, 24, 23]
adjusted = [t - 273 for t in temp_records]  # Kelvin to Celsius (red herring)
decoy_score = sum(adjusted) // len(adjusted)

# Real data path
metric_data = {
    'response_times': [102, 95, 98, 105, 110, 108, 101],
    'success_rate': [0.92, 0.95, 0.94, 0.96, 0.97, 0.95, 0.93],
    'retries': [3, 2, 1, 2, 4, 3, 2],
    'latency_spikes': [False, False, True, False, True, False, False]
}

# Distractor dictionary operations
summary_stats = {}
summary_stats['max_response'] = max(metric_data['response_times'])
summary_stats['min_success'] = min(metric_data['success_rate'])
summary_stats['total_retries'] = sum(metric_data['retries'])
summary_stats['spike_count'] = metric_data['latency_spikes'].count(True)

# Conditional expression with slicing distraction
recent_trend_data = metric_data['success_rate'][-5:]
is_improving = analyze_trend(recent_trend_data)
status_flag = 'optimal' if is_improving else 'review_needed'

# Decoy transformation chain
transformed = [x * 1.05 for x in metric_data['response_times']]
filtered = [t for t in transformed if t < 110]
avg_filtered = sum(filtered) / len(filtered) if filtered else 0

# Core logic buried among distractions
def evaluate_performance(data):
    base = sum(data['response_times']) / len(data['response_times'])
    success_avg = sum(data['success_rate']) / len(data['success_rate'])
    retry_penalty = sum(r * 2 for r in data['retries'])
    spike_bonus = -5 * data['latency_spikes'].count(True)
    
    # Conditional adjustments
    if success_avg >= 0.95 and analyze_trend(data['response_times']):
        base *= 0.9  # efficiency bonus
    elif success_avg < 0.93:
        base += 10
    
    # Final score calculation
    raw_score = base - success_avg * 10 + retry_penalty + spike_bonus
    
    # Additional noise
    noise_offset = len([x for x in data['response_times'] if x > 100]) - len(data['latency_spikes'])
    return int(raw_score) - noise_offset

# Key execution point
final_score = evaluate_performance(metric_data)
print(f"Target result: {final_score}")