import math

# Simulated sensor data processing with diagnostic evaluation
def preprocess_signal(raw_stream, threshold=0.75):
    filtered = [x for x in raw_stream if abs(x) > threshold]
    normalized = [round(x / max(filtered), 6) if max(filtered) != 0 else 0 for x in filtered]
    return normalized

# Irrelevant helper - looks important but unused in final path
def legacy_calibrate(signal):
    return [s * 0.98 for s in signal]

# Core transformation: apply phase shift and fold negative values
def transform_readings(data_points):
    shifted = [math.sin(point * math.pi / 4) for point in data_points]
    folded = [abs(s) ** 2 for s in shifted]
    return [round(f, 6) for f in folded]

# Frequency analysis (distraction) - computes power spectrum but unused
def compute_spectrum(signal):
    spectrum = {}
    for i in range(1, len(signal)+1):
        component = sum(math.cos(x * i) for x in signal)
        spectrum[f'freq_{i}'] = round(component, 4)
    return spectrum

# String-based pattern tagging (uses string methods)
def generate_tags(indices):
    base_names = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    tags = set()
    for i in indices:
        tag = f'{base_names[i % len(base_names)]}-{i}'
        if 'a' in tag:
            tag = tag.replace('a', 'X')
        tags.add(tag.upper())
    return sorted(tags)

# Main pattern analyzer (key function)
def analyze_pattern(processed, settings):
    window_size = settings['window']
    tolerance = settings['tolerance']
    
    # Accumulate energy in sliding windows
    energies = []
    for i in range(len(processed) - window_size + 1):
        window = processed[i:i+window_size]
        energy = sum(w ** 2 for w in window)
        energies.append(round(energy, 6))
    
    # Compute rolling mean difference (decoy computation)
    if len(energies) > 1:
        diffs = [abs(energies[i+1] - energies[i]) for i in range(len(energies)-1)]
        avg_diff = sum(diffs) / len(diffs)
    else:
        avg_diff = 0
    
    # Actual decision logic: count how many windows exceed dynamic threshold
    dynamic_threshold = sum(energies) / len(energies) * tolerance if energies else 0
    valid_count = sum(1 for e in energies if e >= dynamic_threshold)
    
    # Dummy combinatorics (red herring)
    def combination(n, r):
        if r > n or r < 0:
            return 0
        res = 1
        for i in range(min(r, n-r)):
            res = res * (n-i) // (i+1)
        return res
    
    dummy_sum = sum(combination(valid_count + i, i) for i in range(3))  # Unused
    
    # Final diagnostic based on count and system mode
    if settings['mode'] == 'high_precision':
        adjustment = math.ceil(math.log(valid_count + 1))
    else:
        adjustment = math.floor(math.sqrt(valid_count))
    
    result = valid_count * 17 + adjustment
    
    # Destructuring distraction
    metadata = {'version': '2.1', 'nodes': 5, 'active': True}
    version_str, node_count, _ = str(metadata['version']), metadata['nodes'], metadata['active']
    version_digits = list(version_str.replace('.', ''))
    
    # Decoy string join/split
    temp_parts = '-'.join([version_digits[0], str(node_count)]).split('-')
    decoy_value = int(temp_parts[0]) * int(temp_parts[1])  # Never used
    
    return result

# Global constants (some irrelevant)
BASE_SENSORS = 4
MAX_RANGE = 1024
CALIBRATION_FACTOR = 0.87  # Unused in final path
REFERENCE_PATTERN = [0.1, 0.3, 0.5, 0.7, 0.9]  # Partially referenced

# Entry point simulation
if __name__ == '__main__':
    # Initial data stream
    raw_input = [0.2, 0.81, 0.4, 0.93, -0.65, 0.15, -0.88, 0.72, 0.99, -0.33]
    
    # Preprocess stage
    cleaned_signal = preprocess_signal(raw_input, threshold=0.5)
    
    # Transform readings
    transformed_data = transform_readings(cleaned_signal)
    
    # Unused spectral analysis
    frequencies = compute_spectrum(transformed_data)  # Dead code path
    
    # Generate indices for tagging (partially distractive)
    critical_indices = [i for i, v in enumerate(transformed_data) if v > 0.5]
    diagnostic_tags = generate_tags(critical_indices)
    
    # Configuration for analyzer
    config = {
        'window': 3,
        'tolerance': 1.1,
        'mode': 'high_precision'
    }
    
    # Key statement
    final_diagnostic = analyze_pattern(transformed_data, config)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")