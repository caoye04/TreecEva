import math

# Simulated sensor array diagnostics with signal processing
raw_data_points = [127, 255, 192, 64, 240, 31, 144, 208]
baseline_threshold = 128
calibration_factor = 0.87

# Irrelevant environmental constants (distractors)
temperature_offset = 23.5
humidity_bias = 0.042
pressure_compensation = 98.2

# Signal classification function (not used in final computation)
classify_signal_strength = lambda x: 'strong' if x > 200 else 'moderate' if x > 100 else 'weak'

# Step 1: Filter signals above baseline and apply calibration
filtered_signals = [x for x in raw_data_points if x >= baseline_threshold]
adjusted_signals = [int(x * calibration_factor) for x in filtered_signals]

# Step 2: Compute moving average over window of 2 (dead code path - not used later)
moving_avg = []
for i in range(len(adjusted_signals) - 1):
    moving_avg.append((adjusted_signals[i] + adjusted_signals[i+1]) // 2)

# Step 3: Transform into bit signatures for diagnostic analysis
bit_signatures = []
for val in adjusted_signals:
    ones = bin(val).count('1')
    zeros = bin(val).count('0') - 1  # Subtract '0b' prefix
    bit_signatures.append((ones - zeros) * (1 if val & 1 else -1))

# Step 4: Apply diagnostic weighting using combinatoric logic
weights = []
for i in range(len(bit_signatures)):
    # Weight based on position and signature magnitude
    positional_weight = (i + 1) ** 2
    magnitude_effect = abs(bit_signatures[i])
    interaction_term = 1 if magnitude_effect & 1 else -1  # Parity-based flip
    weights.append(positional_weight * magnitude_effect * interaction_term)

# Step 5: Accumulate weighted diagnostics
weighted_sum = sum(weights)
weight_normalizer = len(weights) if weights else 1
normalized_diagnostic = weighted_sum / weight_normalizer if weight_normalizer != 0 else 0

# Step 6: Secondary transformation via unused entropy calculation (red herring)
entropy_metric = 0.0
if normalized_diagnostic != 0:
    for w in weights:
        if w != 0:
            entropy_metric += (w / normalized_diagnostic) * math.log(abs(w / normalized_diagnostic) + 1e-9)

# Step 7: Final processing pipeline — actual critical path
processed_signals = []
for idx, sig in enumerate(bit_signatures):
    # Non-linear amplification based on index parity and sign
    amplification = 2.5 if idx % 2 == 0 else 0.4
    shifted_val = sig * amplification
    clamped_val = max(-127, min(127, shifted_val))
    processed_signals.append(int(clamped_val))

# Decoy function — looks important but never called
def compute_system_entropy(data):
    total = 0
    for x in data:
        total += abs(x) ^ 7
    return total % 1000

# Critical diagnostic analyzer — this IS used
analyze_readings = lambda readings: sum(
    val ** 2 if i % 3 == 0 else 
    val + i if val < 0 else 
    val // (i + 1) if i > 0 else 
    val
    for i, val in enumerate(readings)
)

# Final computation — key statement
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Target result: {final_diagnostic}")