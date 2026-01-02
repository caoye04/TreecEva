def analyze_signal(samples, threshold):
    """
    Analyze signal strength and filter anomalies.
    This function is unrelated to the final result but included as a distractor.
    """
    if not samples:
        return []
    filtered = [s for s in samples if abs(s) > threshold]
    normalized = [round(x / max(filtered), 3) for x in filtered if x != 0]
    return normalized


def transform_sequence(seq, shift):
    """
    Circularly shifts sequence — decoy logic with no impact on final answer.
    """
    if len(seq) == 0:
        return seq
    shift = shift % len(seq)
    return seq[-shift:] + seq[:-shift]


def calculate_entropy(data):
    """
    Computes entropy-like metric — looks important but irrelevant.
    """
    from math import log2
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)


def integrate_segments(bands, weights):
    """
    Weighted sum across frequency bands — dead-end calculation.
    """
    return sum(bands[i] * w for i, w in enumerate(weights)) if len(bands) == len(weights) else 0


def evaluate_performance(metrics, base):
    """
    Core function that computes the final score through layered logic.
    Depends on prior state and threshold filtering.
    """
    adjusted = []
    scaling_factor = 1.5
    
    # Irrelevant pre-processing block (distractor)
    temp_cache = {}
    for i, val in enumerate(metrics):
        temp_cache[f'entry_{i}'] = val ** 0.5 if val > 0 else 0

    # Real logic begins: filter and scale
    for val in metrics:
        if val < base:
            adjusted.append(val * 1.1)
        elif val == base:
            adjusted.append(val + 5)
        else:
            adjusted.append(val * 0.95)

    # Simulate performance decay over time using slicing
    window_size = 3
    rolling_adjusted = [
        sum(adjusted[i:i+window_size]) / window_size
        for i in range(len(adjusted) - window_size + 1)
    ]

    # Secondary adjustment based on modulo behavior
    refined = []
    for i, adj_val in enumerate(rolling_adjusted):
        if i % 3 == 0:
            refined.append(adj_val + 2)
        elif i % 3 == 1:
            refined.append(adj_val * 0.9)
        else:
            refined.append(adj_val - 1)

    # Final aggregation using nested logic and bit manipulation red herring
    aggregate = 0
    bit_accum = 0
    for x in refined:
        truncated = int(x)
        aggregate += truncated
        # Bit manipulation decoy — computed but unused
        bit_accum ^= (truncated << 1) | (truncated >> 2)

    # Final transformation involving modular arithmetic
    modifier = len(refined) % 7
    if modifier > 0:
        aggregate = (aggregate + modifier * 2) // modifier
    else:
        aggregate = aggregate or 1

    return aggregate

# --- Main execution block ---

# Distractor data (simulated sensor inputs)
signal_samples = [-2.1, 0.0, 3.5, 8.2, -1.3, 4.4, 6.7]
filtered_signal = analyze_signal(signal_samples, threshold=2.0)

# Distractor: transform sequence (never used later)
crypto_sequence = [23, 7, 14, 88, 19]
circular_shifted = transform_sequence(crypto_sequence, shift=3)

# Distractor: entropy calculation on arbitrary data
symbol_stream = [1, 1, 0, 1, 0, 0, 1, 1, 1]
entropy_metric = calculate_entropy(symbol_stream)

# Distractor: integration of dummy bands
frequency_bands = [4.2, 5.1, 3.8, 6.0]
weight_vector = [0.25, 0.25, 0.25, 0.25]
integrated_power = integrate_segments(frequency_bands, weight_vector)

# Key data for actual computation
metric_data = [12, 15, 10, 18, 14, 9, 16, 11]
base_threshold = 13

# Critical statement
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")