import itertools

# Simulate agricultural yield prediction with noise filtering and red herrings
def generate_noise(length):
    return [((i * 17 + 257) % 100) / 100 for i in range(length)]

def irrelevant_signal_processor(data):
    # Dead-end function: processes data but never used in final calculation
    processed = []
    for x in data:
        if x > 0.5:
            processed.append(x * 1.2)
        else:
            processed.append(x * 0.8)
    return [p + 0.05 for p in processed]

def decoy_aggregator(values):
    # Unused aggregation that looks important
    total = 0
    for v in values:
        total += v ** 2
    return total / len(values) if values else 0

def filter_outliers(seq, threshold=2.0):
    mean = sum(seq) / len(seq)
    std = (sum((x - mean) ** 2 for x in seq) / len(seq)) ** 0.5
    return [x for x in seq if abs(x - mean) <= threshold * std]

def apply_seasonal_weighting(data, weights):
    # Weighting that looks crucial but is bypassed in logic
    return [d * w for d, w in zip(data, itertools.cycle(weights))]

def calculate_trend_momentum(series):
    # Another distractor: computes trend but not used
    diffs = [series[i+1] - series[i] for i in range(len(series)-1)]
    return sum(diffs) / len(diffs) if diffs else 0

def reconstruct_base_pattern(observed):
    # Reconstructs a base pattern using modular arithmetic and shifts
    base = []
    for i, val in enumerate(observed):
        shifted = (val * 100) % 7
        adjusted = (shifted + i) % 5
        base.append(adjusted)
    return base

def calculate_harvest(config, factor):
    raw_input = [3.2, 4.5, 2.8, 5.1, 3.9, 4.7, 2.6]
    
    # Add noise that must be filtered out
    noise = generate_noise(len(raw_input))
    noisy_data = [r + n for r, n in zip(raw_input, noise)]
    
    # Filter outliers based on statistical threshold
    clean_data = filter_outliers(noisy_data, threshold=1.8)
    
    # Irrelevant transformations (red herrings)
    fake_weights = [0.9, 1.1, 1.0, 0.95]
    weighted = apply_seasonal_weighting(clean_data, fake_weights)  # Computed but unused
    momentum = calculate_trend_momentum(weighted)  # Also unused
    
    # Real computation begins here
    base_pattern = reconstruct_base_pattern([int(x * 10) % 13 for x in clean_data])
    
    # Use itertools to cycle through pattern for alignment
    cyclic_pattern = list(itertools.islice(itertools.cycle(base_pattern), len(clean_data)))
    
    # Apply config-based modulation
    modulated = []
    for i, val in enumerate(clean_data):
        if cyclic_pattern[i] % 2 == 0:
            modulated.append(val * 1.1)
        else:
            modulated.append(val * 0.95)
    
    # Aggregate with correction factor from input
    raw_sum = sum(modulated)
    correction = factor if factor > 0 else 1.0
    corrected = raw_sum * correction
    
    # Final adjustment using hidden rule: only every second element in base_pattern counts
    bonus = sum(1 for i in range(1, len(base_pattern), 2) if base_pattern[i] > 2)
    final = corrected + bonus * 0.25
    
    # Decoy variables that look like they might matter
    aggregate_noise = decoy_aggregator(noise)
    processed_signal = irrelevant_signal_processor(raw_input)
    dummy_merge = [a + b for a, b in zip(processed_signal, weighted[:len(processed_signal)])]
    
    return round(final, 6)

# Main execution flow
projection_data = {'region': 'midwest', 'crop_type': 'wheat', 'historical_avg': 4.1}
adjustment_factor = 0.98

intermediate_check = calculate_trend_momentum([1, 2, 3, 4])  # Red herring call
baseline_shift = decoy_aggregator([5, 6, 7])  # Unused baseline

final_yield = calculate_harvest(projection_data, adjustment_factor)
print(f"Target result: {final_yield}")