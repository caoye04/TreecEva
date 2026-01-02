from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline with diagnostic analysis
def fetch_raw_readings():
    return [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def apply_noise_filter(data):
    # Irrelevant transformation: adds noise compensation that isn't used later
    filtered = [x + (x % 4) for x in data]
    adjustment_log = defaultdict(int)
    for val in filtered:
        adjustment_log[val % 7] += 1
    return filtered  # Only return data; log is unused

def compute_thermal_baseline(samples):
    # Dead code path: this function is defined but never called
    base = sum(samples) / len(samples)
    return round(base * 1.08, 2)

def generate_frequency_map(seq):
    # Distractor: computes frequency but not used in final logic
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    return freq

def shift_cipher(values, key=3):
    # Misleading encryption-like operation, only used once in irrelevant context
    encoded = [(v * key + 7) % 37 for v in values]
    decoded = [( (c - 7) * 25 ) % 37 for c in encoded]  # Modular inverse of 3 mod 37 is 25
    return decoded  # Restores original modulo 37, but data has changed

def extract_prime_signatures(nums):
    # Complex but partially irrelevant prime factor tracking
    signature = defaultdict(set)
    decoy_accumulator = 0
    for n in nums:
        for factor in range(2, int(math.sqrt(n)) + 1):
            while n % factor == 0:
                signature[factor].add(n)
                decoy_accumulator += factor ^ n  # Useless accumulation
                n //= factor
        if n > 1:
            signature[n].add(n)
    # Return only odd-sized signatures
    return {k: v for k, v in signature.items() if len(v) % 2 == 1}

def transform_signal(readings):
    # Core transformation with embedded distractions
    squared = [x ** 2 for x in readings]
    shifted = [x >> 1 for x in squared]  # Right shift by 1 (divide by 2, floor)
    masked = [x & 0xFF for x in shifted]  # Keep only lowest 8 bits
    
    # Decoy normalization (not actually used)
    max_val = max(masked) if masked else 1
    normalized = [round(x / max_val, 3) for x in masked] if max_val != 0 else masked
    
    # Real processing step hidden among distractions
    processed = []
    for i, val in enumerate(masked):
        if i % 2 == 0:
            processed.append(val - 50)
        else:
            processed.append(val + 10)
    
    # Inject a fixed pattern at indices divisible by 3
    for j in range(0, len(processed), 3):
        processed[j] = processed[j] ^ 15  # XOR with 15
    
    return processed

def evaluate_stability_metrics(data):
    # Compute several metrics, many of which are ignored
    stats = {}
    stats['mean'] = sum(data) / len(data)
    stats['peak'] = max(data)
    stats['trough'] = min(data)
    stats['range'] = stats['peak'] - stats['trough']
    stats['variance'] = sum((x - stats['mean']) ** 2 for x in data) / len(data)
    stats['skew_hint'] = (stats['mean'] - stats['trough']) / (stats['range'] + 1)
    
    # Red herring: complex flag logic that doesn't affect outcome
    flag_state = 0
    for val in data:
        if val > 400:
            flag_state |= 1
        elif val < 100:
            flag_state ^= 2
    
    # Return only select metrics
    return {
        'mean': stats['mean'],
        'adjusted_range': max(50, stats['range'] - 25)
    }

def analyze_pattern(dataset, config):
    # Final analysis combining multiple concepts
    count_obj = Counter(dataset)
    unique_values = set(dataset)
    
    # Destructuring assignment distraction
    (a, b), (c, d) = [(1, 2), (3, 4)]  # Unused tuple unpacking
    
    threshold = config.get('critical', 200)
    signal_mass = 0
    activation_peaks = []
    
    for idx, val in enumerate(dataset):
        if val > threshold and idx % 2 == 1:
            signal_mass += val
            activation_peaks.append(idx)
    
    # Secondary filter based on peak spacing
    valid_transitions = 0
    for i in range(1, len(activation_peaks)):
        gap = activation_peaks[i] - activation_peaks[i-1]
        if gap >= 3:
            valid_transitions += 1
    
    # Core formula hidden in middle of distractions
    base_score = len(unique_values) * 17
    modifier = signal_mass // 100
    transition_bonus = valid_transitions * 22
    
    # Decoy calculation using bitwise operations
    decoy_key = 0
    for v in count_obj.values():
        decoy_key ^= (v << 2) | (v & 5)
    
    # Final result computed from relevant components only
    result = base_score + modifier + transition_bonus
    
    # Early return red herring (condition never met due to data)
    if len(dataset) > 100 and threshold < 0:
        return -999
        
    return result

# Main execution flow
if __name__ == '__main__':
    raw_data = fetch_raw_readings()
    cleaned_data = apply_noise_filter(raw_data)
    
    # Irrelevant frequency analysis
    freq_map = generate_frequency_map(cleaned_data)
    
    # Transform data through main pipeline
    transformed_data = transform_signal(cleaned_data)
    
    # Evaluate stability (partially relevant)
    metrics = evaluate_stability_metrics(transformed_data)
    
    # Build configuration with multiple entries (some unused)
    thresholds = {
        'warning': 150,
        'critical': 200,
        'decay_rate': 0.85,
        'window_size': 5
    }
    
    # Perform final diagnostic analysis
    final_diagnostic = analyze_pattern(transformed_data, thresholds)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")