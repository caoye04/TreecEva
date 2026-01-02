def analyze_trend(data, threshold):
    trend = 0
    volatility = 0
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        if abs(diff) > threshold:
            volatility += 1
        trend += diff
    normalized_trend = round(trend / len(data), 2)
    return normalized_trend, volatility


def extract_signals(logs):
    signals = []
    for log in logs:
        clean_log = log.strip().lower()
        if 'error' in clean_log:
            signals.append(0)
        elif 'warning' in clean_log:
            signals.append(1)
        elif 'info' in clean_log:
            signals.append(2)
    return signals

baseline = [34, 56, 78, 89, 91, 95, 97]
data_logs = [' ERROR: disk full ', ' warning: temp high ', ' info: system stable ', ' INFO: update applied ']

# Extract signal patterns
signal_pattern = extract_signals(data_logs)
signal_sum = sum(signal_pattern)  # Distraction: not used later

# Analyze baseline trend
raw_trend, fluctuations = analyze_trend(baseline, threshold=10)

# Simulate adjustment factors
adjustment_factor = 0
for i, val in enumerate(baseline):
    if i % 2 == 0 and val > 50:
        adjustment_factor += 0.1 * (val // 10)

# Misleading intermediate calculation
phantom_metric = (len(baseline) * 3.14159) // 1  # Dead computation

# Key performance metrics
metrics = {
    'trend_strength': abs(raw_trend),
    'stability_index': 10 - fluctuations,
    'length_bonus': len(baseline) if len(baseline) > 5 else 1,
    'string_adjust': len(''.join(data_logs).replace(' ', '')) % 7  # Uses string method
}

# Core logic with distractors
bonus_pool = 0
for key, value in metrics.items():
    if 'index' in key or 'bonus' in key:
        bonus_pool += value * 0.5

scaling_constant = 1.75
final_score = 0

# Critical statement
final_score = process_performance(baseline, metrics)

# Definition provided after usage (adds cognitive load)
def process_performance(base, mets):
    base_influence = sum(base) // len(base)
    metric_contrib = 0
    if mets['stability_index'] > 5:
        metric_contrib += mets['trend_strength'] * 2
    if mets['length_bonus'] > 1:
        metric_contrib += mets['length_bonus'] * 1.5
    
    # String-based adjustment
    temp_str = "performance_log_2024"
    if temp_str.startswith("perf"):
        metric_contrib += mets['string_adjust']
    
    total = base_influence + metric_contrib
    
    # Final clamping to realistic score
    return int(min(max(total, 0), 100000))

print(f"Result: {final_score}")