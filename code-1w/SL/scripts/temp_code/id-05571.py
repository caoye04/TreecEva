def analyze_trends(data, threshold=0.5):
    high_performers = []
    temp_sum = 0
    for i, value in enumerate(data):
        normalized = value / (sum(data) + 1e-8)
        if normalized > threshold:
            high_performers.append(i)
        temp_sum += normalized * i
    adjustment = len(high_performers) if temp_sum > threshold else 0
    return adjustment


def extract_signals(logs):
    signal_strength = 0
    for log in logs:
        clean_log = log.strip().lower()
        if 'alert' in clean_log:
            signal_strength += 2
        elif 'warning' in clean_log:
            signal_strength += 1
    # Distractor: irrelevant transformation
    coded = ''.join([chr((ord(c) % 26) + 97) for c in clean_log[:3]])
    return signal_strength


def compute_stability(values):
    variance = sum([(v - sum(values)/len(values))**2 for v in values]) / len(values)
    stability = 1 / (1 + variance)
    return stability

# Simulated dataset
productivity = [85, 90, 78, 92, 88]
risk_logs = [
    'System operational',
    'Minor warning detected',
    'All systems nominal',
    'WARNING: threshold exceeded',
    'Alert: immediate action required'
]

# Irrelevant preprocessing
baseline_shift = sum(p * 0.1 for p in productivity if p > 80)
dummy_flags = set(['active', 'verified'])

# Real computation chain
raw_trend = analyze_trends(productivity, threshold=0.2)
signal_count = extract_signals(risk_logs)
stability_metric = compute_stability(productivity)

# Intermediate distractor variables
placeholder = [x * raw_trend for x in range(3)]
fallback_mode = False

# Key state tracking
risk_factor = signal_count * (1 - stability_metric)

# Main evaluation logic
if raw_trend > 0:
    base_score = sum(productivity) / len(productivity)
else:
    base_score = 75

adjustment_factor = 1 + (raw_trend * 0.05)
penalty = risk_factor * 2 if risk_factor > 3 else 0

# Final score calculation
final_score = (base_score * adjustment_factor) - penalty

# Output target result
print(f"Result: {final_score}")