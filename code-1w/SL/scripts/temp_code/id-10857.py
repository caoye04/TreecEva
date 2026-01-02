import itertools

# Sensor simulation and diagnostic system
base_frequencies = [12.5, 18.3, 9.7, 22.1, 14.6]
signal_strengths = [0.88, 0.94, 0.76, 0.81, 0.90]
noise_levels = [0.05, 0.12, 0.08, 0.15, 0.10]

def generate_waveform(frequency, strength, noise):
    return (strength * frequency) / (1 + noise)

def calculate_coherence(signals):
    # Irrelevant coherence metric (dead-end computation)
    total = 0
    for i in range(len(signals)):
        for j in range(i + 1, len(signals)):
            total += abs(signals[i] - signals[j])
    return total / (len(signals) ** 2) if signals else 0

def filter_outliers(data, threshold=0.85):
    # Misleading filtering that isn't actually used in main logic
    return [x for x in data if x > threshold]

def normalize_signal(signal_list):
    max_val = max(signal_list)
    return [s / max_val for s in signal_list]

def accumulate_diagnostics(normalized):
    cumulative_score = 0
    for idx, val in enumerate(normalized):
        if idx % 2 == 0:
            cumulative_score += val * 1.1
        else:
            cumulative_score += val * 0.9
    return cumulative_score

# Unused decoy function - looks important but does nothing
def compute_entropy(data):
    from math import log
    total = sum(data)
    probabilities = [x / total for x in data]
    entropy = -sum(p * log(p) for p in probabilities if p > 0)
    return entropy

# Simulate raw sensor readings
raw_signals = []
for f, s, n in zip(base_frequencies, signal_strengths, noise_levels):
    raw_signals.append(generate_waveform(f, s, n))

# Normalize signals for processing
processed_signals = normalize_signal(raw_signals)

# Distractor: compute irrelevant metrics
coherence_index = calculate_coherence(raw_signals)
entropy_approx = 0  # Placeholder - never actually computed
outlier_count = len([x for x in signal_strengths if x < 0.85])  # Red herring

# Real processing path begins here
weighted_sum = 0
for i, sig in enumerate(processed_signals):
    weight = 1.0 + (i * 0.1)
    weighted_sum += sig * weight

# Secondary transformation using itertools.cycle to create artificial complexity
phase_shifts = list(itertools.cycle([0.1, -0.05, 0.2]))
adjusted_signals = []
for i, sig in enumerate(processed_signals):
    adjusted_signals.append(sig + phase_shifts[i])

# Accumulate final diagnostic score
final_diagnostic = 0
def analyze_readings(signals):
    temp_result = 0
    for idx, val in enumerate(signals):
        if idx == 0:
            temp_result += val * 2
        elif idx == len(signals) - 1:
            temp_result += val * 1.5
        else:
            temp_result += val
    # Final adjustment based on pattern recognition
    if len(signals) > 3 and signals[1] < signals[2]:
        temp_result *= 1.2
    return int(temp_result * 1000)  # Scale to integer

# Key execution point
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Result: {final_diagnostic}")