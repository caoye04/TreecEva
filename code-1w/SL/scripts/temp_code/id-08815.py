import math

# Sensor calibration constants (some are decoys)
CALIBRATION_A = 0.987
CALIBRATION_B = 1.013
CALIBRATION_C = 2.45  # Unused constant - red herring
OFFSET_X = 17.3   # Unused - misleading
OFFSET_Y = -8.21  # Unused

# Simulated sensor readings (real data mixed with dummy)
signal_chain_a = [12.1, 14.3, 15.6, 13.9, 16.2]
signal_chain_b = [11.8, 15.1, 14.7, 13.4, 16.0]
dummy_readings = [9.2, 10.5, 11.1, 10.8]  # Dead-end data

# Preprocess signals using list comprehension with filtering and scaling
cleaned_a = [x * CALIBRATION_A for x in signal_chain_a if x > 12.0]
cleaned_b = [x * CALIBRATION_B for x in signal_chain_b if x > 12.0]

# Combine signals with phase shift simulation
combined_signal = []
for i in range(len(cleaned_a)):
    combined_value = (cleaned_a[i] + cleaned_b[i]) / 2.0
    combined_signal.append(round(combined_value, 3))

# Apply moving average filter (relevant transformation)
def moving_average(data, window=2):
    if len(data) < window:
        return [0]
    return [sum(data[i:i+window]) / window for i in range(len(data)-window+1)]

filtered_output = moving_average(combined_signal, 2)

# Compute entropy-like metric on distribution (distraction)
def compute_entropy(arr):
    total = sum(arr)
    probs = [x/total for x in arr]
    return -sum(p * math.log(p) for p in probs if p > 0)

entropy_score = compute_entropy(filtered_output)  # Computed but unused

# Transform data into frequency domain approximation (red herring function)
def time_to_frequency(signal):
    n = len(signal)
    freqs = []
    for k in range(n//2):
        re = sum(signal[i] * math.cos(2*math.pi*k*i/n) for i in range(n))
        im = sum(-signal[i] * math.sin(2*math.pi*k*i/n) for i in range(n))
        freqs.append(math.sqrt(re*re + im*im))
    return freqs or [0]

frequency_analysis = time_to_frequency(filtered_output)  # Dead end
peak_frequency = max(frequency_analysis) if frequency_analysis else 0  # Misleading

# Core diagnostic logic (critical path)
def normalize_and_classify(val):
    if val < 13.0:
        return 1
    elif val < 14.5:
        return 2
    else:
        return 3

# Process each filtered reading through classification
classification_bins = [normalize_and_classify(x) for x in filtered_output]

def count_transitions(classes):
    transitions = 0
    for i in range(1, len(classes)):
        if classes[i] != classes[i-1]:
            transitions += 1
    return transitions

transition_count = count_transitions(classification_bins)  # Important intermediate

# Analyze signal stability based on transition density
stability_index = len(classification_bins) / (transition_count + 1) if transition_count else float('inf')

# Final processing pipeline
processed_signals = {
    'raw_a': signal_chain_a,
    'raw_b': signal_chain_b,
    'clean_a': cleaned_a,
    'clean_b': cleaned_b,
    'combined': combined_signal,
    'filtered': filtered_output,
    'classifications': classification_bins,
    'transitions': transition_count,
    'index': stability_index
}

# Decoy analysis functions
def validate_timing_sequence(seq):  # Unused function
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

def calculate_snr(signal, noise_floor=0.5):  # Computed but irrelevant
    power = sum(x*x for x in signal)
    noise = len(signal) * noise_floor**2
    return round(power / noise, 4)

snr_ratio = calculate_snr(combined_signal)  # Distractor result

# Actual final analysis function
def analyze_readings(data_dict):
    # Extract relevant metrics
    transitions = data_dict['transitions']
    classes = data_dict['classifications']
    filtered = data_dict['filtered']
    
    # Compute weighted variance (looks complex, partially relevant)
    mean_val = sum(filtered) / len(filtered)
    deviations = [(x - mean_val)**2 for x in filtered]
    weighted_var = sum(w * d for w, d in enumerate(deviations, 1)) / sum(range(1, len(deviations)+1))
    
    # Key decision logic: classify system state
    if transitions == 0:
        base_score = 500
    elif transitions == 1:
        base_score = 750
    else:
        base_score = 1000
    
    # Refine by variance influence
    adjustment = int(weighted_var * 10)
    final_score = base_score - adjustment
    
    # Additional correction based on pattern symmetry (minor effect)
    if len(classes) >= 4 and classes[1:-1] == classes[-2:0:-1]:
        final_score += 25
    
    return final_score

# Execute critical statement
final_diagnostic = analyze_readings(processed_signals)
print(f"Result: {final_diagnostic}")