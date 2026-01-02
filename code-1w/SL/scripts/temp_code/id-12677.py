def analyze_performance(data):
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(data) for x in data]
    weights = [0.1, 0.2, 0.3, 0.4]
    weighted_sum = sum(w * v for w, v in zip(weights, normalized[:4]))

    # Red herring: unused complex calculation
    entropy = 0.0
    for x in normalized:
        if x > 0:
            entropy -= x * __import__('math').log(x)

    # Fake signal: misleading intermediate
    volatility = max(normalized) - min(normalized)
    adjustment_factor = __import__('math').sin(volatility * 100)

    # Real but hidden logic begins
    raw_metrics = {
        'quality': sum(1 for x in data if x >= 80),
        'efficiency': sum(data[i] - data[i-1] for i in range(1, len(data))) // len(data),
        'reliability': len(data) - len([x for x in data if x < 50])
    }

    return raw_metrics


def evaluate_system(logs):
    # Dead code path (never executed)
    def deprecated_metric(seq):
        return sum(seq) % 7

    # Distractor: irrelevant transformation
    processed_logs = []
    for idx, entry in enumerate(logs):
        if idx % 2 == 0:
            processed_logs.append(entry * 1.1)
        else:
            processed_logs.append(entry * 0.9)

    # Unused statistical moment
    mean_val = sum(logs) / len(logs)
    variance = sum((x - mean_val) ** 2 for x in logs) / len(logs)
    skewness = sum((x - mean_val) ** 3 for x in logs) / (len(logs) * variance ** 1.5) if variance > 0 else 0

    # Actual relevant data extraction
    critical_events = sum(1 for x in logs if x > 95)
    baseline_stability = sum(1 for x in logs if 60 <= x <= 85)

    return critical_events, baseline_stability


def process_metrics(q, e, r):
    # Core computation buried in noise
    base = q * 10
    bonus = 0

    # Conditional red herrings
    if e > 5:
        bonus += 15
    elif e < -5:
        bonus -= 20  # Never reached due to data

    # Real logic
    penalty = 0
    if r < 3:
        penalty = 50

    # Distractor: bit manipulation with no effect
    masked_r = r ^ 0b111000
    shifted = (masked_r << 2) & 0xFF

    # Final formula (key)
    score = base + bonus - penalty

    # Fake alternative paths
    if q > 100:
        score = 0  # unreachable

    return score

# Main execution flow
system_data = [88, 92, 76, 85, 94, 67, 81, 73, 90, 87]

# Call analysis (real)
metrics = analyze_performance(system_data)

# Extract values
quality = metrics['quality']  # 6
efficiency = metrics['efficiency']  # (92-88)+(76-92)+...+(87-90) // 10 => (-4-16-9+...-3)//10 = -4
reliability = metrics['reliability']  # 10 - 1 (only 76 below 50?) -> actually none, so 10

# Unused side analysis
events, stability = evaluate_system(system_data)

# Decoy variables
config_flag = 0b101010
checksum = sum(system_data) ^ config_flag

# Key statement
final_score = process_metrics(quality, efficiency, reliability)

# Output result
print(f"Result: {final_score}")