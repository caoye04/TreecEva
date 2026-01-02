def analyze_trend(data, threshold):
    trend = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend.append(1)
        elif data[i] < data[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    return sum(t for t in trend if abs(t) == 1)

# Irrelevant helper function (decoy)
def compute_entropy(values):
    from math import log
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 3)

# Unused transformation path (dead code)
def transform_sequence(seq):
    return [x ^ 3 for x in seq if x % 2 == 0][::2]

# Simulate sensor drift compensation (red herring)
current_offset = 0.75
drift_buffer = [round(i * 0.15 + current_offset, 2) for i in range(8)]
adjusted_readings = [x - drift_buffer[0] for x in drift_buffer]

# Core logic disguised among distractions
baseline = {'alpha': 85, 'beta': 72, 'gamma': 93}
raw_metrics = [88, 70, 95]

# Misleading intermediate calculation
aggregated = sum(x * 1.05 for x in raw_metrics if x > 75)
weight_map = {'alpha': 0.4, 'beta': 0.3, 'gamma': 0.3}

# Real processing begins here
metric_keys = ['alpha', 'beta', 'gamma']
metrics = {k: v for k, v in zip(metric_keys, raw_metrics)}

# Bit manipulation as noise
flag_register = 0b1010
flag_register ^= 0b1100
flag_register |= 0b0010
status_flag = flag_register & 0b1000  # Always 8

# Set operation distraction
duplicate_flags = {88, 70, 95} | {85, 72, 93}
overlap_count = len(duplicate_flags.intersection({88, 85}))

# Actual evaluation logic (buried)
def evaluate_performance(perf, base):
    score = 0
    for key in base:
        deviation = abs(perf[key] - base[key])
        if deviation <= 3:
            score += 10
        elif deviation <= 6:
            score += 5
        else:
            score -= 2
    # Secondary adjustment based on trend
    recent_values = list(perf.values())
    trend_strength = analyze_trend(recent_values, threshold=0)
    if trend_strength > 0:
        score += 3
    # Final twist: bitwise parity bonus
    total_deviation = sum(abs(perf[k] - base[k]) for k in base)
    if total_deviation & 1:  # Odd total?
        score += 1
    return score

# Key execution point
final_score = evaluate_performance(metrics, baseline)

# Output requirement
print(f"Result: {final_score}")