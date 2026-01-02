import math

# Simulated sensor data stream with noise
data_stream = [12, -5, 8, 0, 15, -3, 9, 2, 7, -1, 6, 4]
noise_threshold = 3
amplitude_factor = 2.5

def apply_noise_filter(signal, threshold):
    return [x for x in signal if abs(x) > threshold]

def amplify_signal(signal, factor):
    return list(map(lambda x: x * factor, signal))

def compute_envelope(signal):
    return max(signal) - min(signal)

def smooth_data(signal):
    smoothed = []
    for i in range(1, len(signal)-1):
        smoothed.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
    return smoothed

def evaluate_stability(metric):
    return "stable" if metric < 20 else "unstable"

def calculate_entropy(signal):
    # Irrelevant distractor function (not used in final path)
    mean_val = sum(signal) / len(signal)
    variance = sum((x - mean_val)**2 for x in signal) / len(signal)
    return math.log(variance) if variance > 0 else 0

def assess_risk_level(envelope):
    return 1 if envelope > 25 else 0

# Step 1: Filter out low-amplitude noise
filtered_data = apply_noise_filter(data_stream, noise_threshold)

# Step 2: Amplify relevant signals
amplified_data = amplify_signal(filtered_data, amplitude_factor)

# Step 3: Compute signal envelope (peak-to-peak)
envelope_value = compute_envelope(amplified_data)

# Step 4: Smooth amplified data for further analysis
smoothed_amplified = smooth_data(amplified_data)

# Distractor computation: Stability evaluation (not used later)
stability_status = evaluate_stability(envelope_value)

# Distractor: Entropy calculation (dead end)
entropy_metric = calculate_entropy(amplified_data)

# Conditional processing based on envelope
if envelope_value > 20:
    temp_offset = 5.0
else:
    temp_offset = 0.0

# Nested logic with conditional expression
baseline_shift = 10 if stability_status == "stable" else 7
adjusted_envelope = envelope_value + baseline_shift - temp_offset

# Further intermediate variables (some irrelevant)
dummy_aggregate = sum(smoothed_amplified[:2]) if len(smoothed_amplified) > 2 else 0
placeholder_score = dummy_aggregate * 0.5  # Unused beyond this point

# Core processing chain
processed_magnitude = math.sqrt(adjusted_envelope ** 2 + 9)

# Final transformation using slicing and lambda
transform_window = amplified_data[::2]  # Every other element
weight_function = lambda w: w * 0.1
weighted_sum = sum(weight_function(w) for w in transform_window)

# Critical statement
final_output = process_signals(filtered_data)

# Actual definition of process_signals (deliberately defined late)
def process_signals(seq):
    base = sum(x > 0 for x in seq)  # Count positives
    modifier = int(any(x % 2 == 0 for x in seq))  # Check even exists
    return base * 3 + modifier

# Print result for observability
print(f"Result: {final_output}")