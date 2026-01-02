import math

# Simulated sensor data processing for environmental monitoring system
def analyze_readings(raw_samples):
    filtered = [x for x in raw_samples if 10 <= x <= 100]
    offset = sum(1 for x in raw_samples if x < 10)
    bonus = len(filtered) // 5
    return sorted(filtered, reverse=True), offset, bonus

def transform_scale(readings, factor=1.1):
    return [round(x * factor, 2) for x in readings]

def calculate_entropy(values):
    total = sum(values)
    probs = [v / total for v in values]
    return round(-sum(p * math.log2(p) for p in probs if p > 0), 4)

def shift_cipher(text, key):
    # Irrelevant string manipulation - distractor
    return ''.join(chr((ord(c) - 97 + key) % 26 + 97) if c.islower() else c for c in text)

def dummy_aggregate(data):
    # Dead function - never called in execution path
    return sum(d ** 0.5 for d in data) / len(data)

def bitwise_normalize(val):
    # Misleading bit manipulation - used but result discarded
    val ^= 0xFF
    val &= 0x7F
    val >>= 3
    return val

def compute_baseline(reference, mode='avg'):
    if mode == 'avg':
        return sum(reference) / len(reference)
    elif mode == 'median':
        s = sorted(reference)
        n = len(s)
        return s[n//2] if n % 2 else (s[n//2-1] + s[n//2]) / 2
    return 0

def evaluate_metrics(signal, noise):
    snr = 20 * math.log10(sum(signal) / sum(noise)) if sum(noise) > 0 else 0
    coherence = len([i for i in range(1, len(signal)) if signal[i] >= signal[i-1]])
    trend_ratio = coherence / (len(signal) - 1) if len(signal) > 1 else 1
    return snr, trend_ratio

def main():
    # Core input data
    samples = [85, 92, 78, 63, 96, 88, 73, 105, 55, 44, 30, 77, 89, 94, 67, 12, 90]

    # Primary processing chain
    clean_data, underflow, extra_credit = analyze_readings(samples)
    scaled_values = transform_scale(clean_data, 1.08)

    # Distractor: unused transformation
    inverted = [100 - x for x in clean_data]
    entropy_value = calculate_entropy(scaled_values[:10])  # Partial use only

    # Meaningful intermediate calculation
    base = compute_baseline(scaled_values, 'avg')
    adjusted = [x - base for x in scaled_values]

    # Simulated secondary metric
    fluctuation = sum(abs(adjusted[i] - adjusted[i-1]) for i in range(1, len(adjusted)))

    # Bitwise red herring
    key_mask = 0b1101101
    temp_flags = []
    for x in adjusted[:5]:
        flag = int(abs(x)) ^ key_mask
        flag = bitwise_normalize(flag)  # Computation with no impact
        temp_flags.append(flag & 1)

    # Control flow distraction
    status_codes = {}
    for i, val in enumerate(scaled_values):
        if val > 90:
            status_codes[i] = 'HIGH'
        elif val > 75:
            status_codes[i] = 'NORMAL'
        else:
            status_codes[i] = 'LOW'

    # Dictionary operation - relevant
    metric_data = {
        'amplitude': sum(scaled_values) / 100,
        'stability': 100 - fluctuation / 10,
        'consistency': len([x for x in adjusted if x > 0]),
        'entropy': float(str(entropy_value)[:6])  # Truncated precision
    }

    # Lambda function usage - meaningful
    normalizer = lambda x, m: round(x * 100 / m, 3)
    max_val = max(scaled_values)
    normalized_metrics = {k: normalizer(v, max_val) for k, v in metric_data.items()}

    # Weight assignment - some weights are decoys
    weights = {
        'amplitude': 0.4,
        'stability': 0.3,
        'consistency': 0.2,
        'entropy': 0.1,
        'dummy_metric': 0.0  # Unused weight
    }

    # Final evaluation - this is where final_score is computed
    final_score = evaluate_performance(normalized_metrics, weights)

    # Decoy output lines - irrelevant prints
    debug_info = {
        'raw_count': len(samples),
        'clean_count': len(clean_data),
        'offset': underflow,
        'bonus': extra_credit,
        'flags': temp_flags
    }

    ciphered = shift_cipher('debugdata', 7)  # String method - pure distractor
    _ = [math.sqrt(z) for z in inverted if z > 80]  # Dead computation

    print(f"Target result: {final_score}")

# Critical function containing answer logic
def evaluate_performance(metrics, weight_map):
    score = 0.0
    # Only process defined, non-zero weighted metrics
    for name, weight in weight_map.items():
        if name in metrics and weight > 0:
            score += metrics[name] * weight
    return round(score, 4)

if __name__ == '__main__':
    main()