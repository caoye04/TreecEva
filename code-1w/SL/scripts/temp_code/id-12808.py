import math

# Simulated sensor data preprocessing pipeline
raw_readings = [i * 0.5 + (i % 7) for i in range(30)]
offset_calibration = sum([x ** 0.5 for x in raw_readings if x > 5])
scaled_readings = [x * 1.07 + 2.1 for x in raw_readings]

# Irrelevant noise modeling (distractor)
noise_floor = 0.03
thermal_drift = [noise_floor * math.sin(i / 5.0) for i in range(20)]
phantom_signals = [abs(math.cos(x) * 0.1) for x in thermal_drift]  # Unused path

# Real processing begins
filtered_samples = [x for x in scaled_readings if x > 6.0 and (x * 1.1) % 1 < 0.9]
integration_window = min(len(filtered_samples), 25)

def accumulate_trend(data, window):
    trend = 0
    for i in range(window):
        if i % 4 == 0:
            trend += data[i] * 0.8
        elif i % 3 == 0:
            trend -= data[i] * 0.3
        else:
            trend += data[i] * 0.5
    return round(trend, 4)

# Secondary transformation chain
transformed = []
for val in filtered_samples:
    temp = val ** 2
    temp = temp / 4.7
    if temp > 50:
        temp = temp ** 0.5
    transformed.append(temp)

# Dead-end function (decoy)
def compute_entropy(arr):
    entropy = 0.0
    for x in arr:
        if x > 0:
            entropy -= x * math.log(x)
    return entropy  # Never called

# Signal folding with conditional compression
folded_signal = []
half_len = len(transformed) // 2
for i in range(half_len):
    left = transformed[i]
    right = transformed[-(i+1)]
    if left + right > 8.0:
        folded_signal.append((left * 0.6) + (right * 0.4))
    else:
        folded_signal.append((left + right) / 2.5)

# Accumulate diagnostic baseline
baseline_metric = 0
for x in folded_signal:
    if x > 4.0:
        baseline_metric += x * 1.2
    else:
        baseline_metric += x * 0.7

# Spurious auxiliary calculation (red herring)
counterfeit_index = 0
for x in raw_readings:
    if x > 10:
        counterfeit_index += int(x % 3)
    else:
        counterfeit_index -= 1
counterfeit_index = abs(counterfeit_index) % 97  # Unused

# Critical computation path
compressed = [round(x * 0.9 + 0.1, 3) for x in folded_signal if x > 2.0]
smoothed = sum(compressed) / len(compressed) if compressed else 0

# Advanced feature extraction
feature_vector = [math.tanh(x - 3.0) for x in compressed]
polarity_score = sum(1 for f in feature_vector if f > 0) - sum(1 for f in feature_vector if f <= 0)

# Final analysis function
def analyze_signal(signal_chunk):
    total_power = sum([s**2 for s in signal_chunk])
    avg_power = total_power / len(signal_chunk) if signal_chunk else 0
    peak = max(signal_chunk) if signal_chunk else 0
    
    # Misleading intermediate blend
    dummy_blend = 0.3 * peak + 0.7 * avg_power
    temp_adjust = math.log(avg_power + 1) if avg_power > 0 else 0
    
    # Core formula (non-obvious due to distractions)
    diagnostic_value = (avg_power * 0.6) + (temp_adjust * 0.3) + (polarity_score * 0.1)
    return round(diagnostic_value, 4)

# Execution point of interest
processed_samples = [min(x, 12.0) for x in compressed]
final_diagnostic = analyze_signal(processed_samples)
print(f"Target result: {final_diagnostic}")