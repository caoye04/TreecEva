import itertools

# Simulated sensor data preprocessing pipeline
raw_readings = [0.7, -1.2, 0.95, -0.3, 1.4, -0.8, 0.65, -1.1]
baseline_offset = 0.1
noise_floor = 0.25

def filter_outliers(data, threshold=1.0):
    return [x for x in data if abs(x) <= threshold]

def amplify_signal(data, factor=2.0):
    amplified = []
    for val in data:
        new_val = val * factor
        if abs(new_val) > 2.0:
            new_val = 2.0 if new_val > 0 else -2.0
        amplified.append(new_val)
    return amplified

def compute_coherence(sequence):
    # Irrelevant computation - decoy function
    total = 0.0
    for i in range(len(sequence)):
        total += sequence[i] * sequence[-(i+1)]
    return round(total, 3)

def generate_combinations(values):
    # Distractor: generates unused combinations
    combo_results = []
    for r in range(2, 4):
        combo_results.extend(list(itertools.combinations(values, r)))
    return combo_results  # Never used

def phase_shift(elements, shift=1):
    if not elements:
        return []
    shift = shift % len(elements)
    return elements[-shift:] + elements[:-shift]

def integrate_samples(snippet):
    accumulator = 0.0
    decay = 0.9
    for sample in snippet:
        accumulator = accumulator * decay + sample
    return round(accumulator, 4)

def validate_calibration(signal_chunk):
    # Dead code path - never actually called
    if len(signal_chunk) < 3:
        return False
    energy = sum(x**2 for x in signal_chunk)
    return energy > 0.5

def extract_features(dataset):
    features = []
    for segment in dataset:
        mean_val = sum(segment) / len(segment)
        variance = sum((x - mean_val)**2 for x in segment) / len(segment)
        features.append((mean_val, variance))
    return features

def analyze_signal(clean_data):
    if not clean_data:
        return 0.0
    
    # Break into chunks
    chunk_size = 2
    chunks = [clean_data[i:i+chunk_size] for i in range(0, len(clean_data), chunk_size)]
    
    # Extract statistical features (some will be ignored)
    stats = extract_features(chunks)
    
    # Only use first feature pair for final calculation
    primary_mean, primary_var = stats[0]
    
    # Compute entropy approximation (unused red herring)
    entropy_approx = 0.0
    for m, v in stats:
        if v > 0:
            entropy_approx += 0.5 * __import__('math').log(2 * 3.14159 * v)
    
    # Key computation path begins here
    integrated = integrate_samples(clean_data)
    adjusted = integrated + primary_mean
    
    # Apply nonlinearity
    if adjusted < 0:
        result = -((-adjusted) ** 0.7)
    else:
        result = adjusted ** 0.7
    
    # Final transformation
    return int(round(result * 1000))

# Main processing chain
adjusted_readings = [x - baseline_offset for x in raw_readings]
filtered_samples = filter_outliers(adjusted_readings)
boosted_signal = amplify_signal(filtered_samples, factor=1.8)

temp_diagnostic = compute_coherence(boosted_signal)  # Misleading intermediate

# Generate unused combinatorial analysis
sample_subset = boosted_signal[:4]
decoys = generate_combinations(sample_subset)  # Dead end

# Phase manipulation with no impact
shifted_primary = phase_shift(boosted_signal, 2)
shifted_secondary = phase_shift(boosted_signal, -1)

# Critical assignment
processed_samples = shifted_primary  # This is what gets used

# Add irrelevant tuple unpacking
meta_stats = [(len(boosted_signal), temp_diagnostic)]
size, coherence_score = meta_stats[0]

# Unused logical evaluation
is_stable = size >= 4 and coherence_score > -1.0 or False

# Core execution point
final_diagnostic = analyze_signal(processed_samples)

print(f"Result: {final_diagnostic}")