import itertools

# Simulated bio-signal processing pipeline with red herrings
def preprocess_waveform(signal):
    filtered = [x for x in signal if x > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Irrelevant transformation - dead end function
def deprecated_envelope(signal):
    envelope = []
    for i in range(len(signal) - 1):
        envelope.append(abs(signal[i+1] - signal[i]))
    smoothed = [sum(envelope[i:i+3]) / 3 for i in range(len(envelope) - 2)]
    return smoothed  # never used in main logic

# Decoy data from unrelated sensor modality
auxiliary_data = [0.81, 0.76, 0.92, 0.65, 0.88]
decoys = {f'decoy_{i}': val ** 2 for i, val in enumerate(auxiliary_data)}

# Real signal input (simulated neural spike train)
primary_signal = [0.5, 0.3, 0.7, 0.2, 0.9, 0.4, 0.6]
secondary_signal = [0.1, 0.8, 0.3, 0.7, 0.5]

# Misleading intermediate calculation - looks important but unused
aggregated_risk = sum((x * 1.5) for x in primary_signal if x < 0.6)
temporal_weighting = [x * (i + 1) for i, x in enumerate(secondary_signal)]

# Signal fusion via Cartesian product (itertools usage)
sync_pairs = list(itertools.product(primary_signal, secondary_signal))
combined_magnitude = [a * b for a, b in sync_pairs if a > 0.4 and b > 0.4]

# Distraction: complex-looking but unused set operation
unique_magnitudes = set(round(x, 2) for x in combined_magnitude)
excluded_outliers = {x for x in unique_magnitudes if x < 0.3}

# Core processing chain
filtered_primary = preprocess_waveform(primary_signal)
filtered_secondary = preprocess_waveform(secondary_signal)

# Simulated time alignment heuristic (nested conditionals)
if len(filtered_primary) > len(filtered_secondary):
    adjusted_signal = filtered_primary[:len(filtered_secondary)]
    padding_correction = sum(1.0 for _ in range(len(filtered_primary) - len(filtered_secondary)))
else:
    adjusted_signal = filtered_secondary[:len(filtered_primary)]
    padding_correction = -sum(0.5 for _ in range(len(filtered_secondary) - len(filtered_primary)))

# Weighted interaction matrix (list comprehension with filtering)
interactions = []
for i, a in enumerate(filtered_primary):
    row = []
    for j, b in enumerate(adjusted_signal):
        if abs(i - j) <= 2:
            weight = a * b * (abs(i - j) + 1)
            if weight > 0.1:
                row.append(weight)
    if row:
        interactions.append(row)

# Flattening with nested comprehension
flattened_interactions = [item for row in interactions for item in row]

# Red herring: unused statistical moment calculation
variance_proxy = sum((x - 0.5) ** 2 for x in flattened_interactions) / len(flattened_interactions) if flattened_interactions else 0
skew_attempt = sum((x - 0.5) ** 3 for x in flattened_interactions)  # calculated but ignored

# Critical pathway: combinatorial activation pattern detection
thresholded = [1 if x >= 0.25 else 0 for x in flattened_interactions]
activation_sequences = list(itertools.combinations(thresholded, 4))

# Count non-trivial activation patterns
pattern_counter = 0
for seq in activation_sequences:
    if sum(seq) >= 3:  # at least three activations
        if seq[0] == 1 or seq[-1] == 1:  # starts or ends with activation
            pattern_counter += 1

# Simulated diagnostic integration
baseline_score = len([x for x in flattened_interactions if x > 0.3])
penalty_factor = len(excluded_outliers) * 0.5  # uses excluded set but not critical

# Auxiliary string-based identifier (string method red herring)
device_id = "neuroX-9000-pro"
serial_parts = device_id.split('-')
model_generation = serial_parts[1] if len(serial_parts) > 1 else "unknown"
firmware_check = model_generation.startswith('X') and "validated" or "pending"

# Final combination before analysis
combined_signal = [
    baseline_score * 1.2,
    pattern_counter * 0.8,
    padding_correction,
    variance_proxy * 10
]

# THE KEY STATEMENT — answer derived here
def analyze_pathway(metrics):
    # Multi-stage weighting with conditional overrides
    adjusted = []
    for i, val in enumerate(metrics):
        if i == 0:
            adjusted.append(val * 1.5)
        elif i == 1:
            temp = val * 2.0
            if temp > 10:
                temp = 10 + (temp - 10) * 0.1  # compression
            adjusted.append(temp)
        elif i == 2:
            adjusted.append(max(val, 0) * 5)  # only positive padding counts
        else:
            adjusted.append(min(val, 7))  # cap on variance contribution
    
    # Final integration with tie-breaking logic
    total = sum(adjusted)
    if total.is_integer():
        final = int(total) + 1
    else:
        final = round(total, 2)
    
    # Tie-breaker based on pattern parity
    if pattern_counter % 2 == 1:
        final += 0.25
    
    return final

final_diagnostic = analyze_pathway(combined_signal)
print(f"Result: {final_diagnostic}")