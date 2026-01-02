import math

# System telemetry simulation with diagnostic processing
raw_readings = [384, 256, 512, 192, 448, 320, 384, 416]
thresholds = {'low': 200, 'high': 400, 'critical': 500}
system_flags = [True, False, True, False, True, True, False, True]

# Irrelevant signal smoothing (red herring)
def smooth_signal(data, factor=0.3):
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(smoothed[-1] * (1 - factor) + data[i] * factor)
    return smoothed

# Distractor: Frequency domain analysis (unused)
def compute_fft_magnitude(signal):
    N = len(signal)
    fft_result = [0] * N
    for k in range(N):
        real = imag = 0
        for n in range(N):
            angle = 2 * math.pi * k * n / N
            real += signal[n] * math.cos(angle)
            imag -= signal[n] * math.sin(angle)
        fft_result[k] = math.sqrt(real*real + imag*imag)
    return fft_result

# Signal normalization with threshold logic
normalized_signals = []
for reading in raw_readings:
    if reading < thresholds['low']:
        normalized_signals.append(reading * 1.5)
    elif reading > thresholds['high']:
        if reading > thresholds['critical']:
            normalized_signals.append(reading * 0.8)
        else:
            normalized_signals.append(reading * 1.1)
    else:
        normalized_signals.append(reading)

# Dead code path - never called (distractor)
def legacy_calibration(x):
    return (x >> 2) ^ 0x1F

# Decoy transformation chain
temp_sequence = [x ^ 0xFF for x in raw_readings if x % 128 == 0]
processed_temp = [math.log(x + 10) for x in temp_sequence]
summary_stat = sum(processed_temp) / len(processed_temp) if processed_temp else 0

# Real computation begins here
active_indices = [i for i, flag in enumerate(system_flags) if flag]
filtered_signals = [normalized_signals[i] for i in active_indices]

# Secondary filtering based on dynamic condition
reference_baseline = sum(filtered_signals) / len(filtered_signals)
variance_pool = []
for sig in filtered_signals:
    deviation = sig - reference_baseline
    variance_pool.append(deviation * deviation)

# Tertiary aggregation with weighted contribution
weight_map = {}
counter = 0
for idx in active_indices:
    weight = 1.0 + (idx % 3) * 0.1
    weight_map[counter] = weight
    counter += 1

# Accumulation with weighted variance scaling
weighted_accumulator = 0.0
count = 0
for dev_sq in variance_pool:
    weight = weight_map.get(count, 1.0)
    weighted_accumulator += dev_sq * weight
    count += 1

# Final non-linear transformation
if weighted_accumulator > 10000:
    final_score = math.sqrt(weighted_accumulator) * 1.2
elif weighted_accumulator > 5000:
    final_score = weighted_accumulator * 0.15
else:
    final_score = weighted_accumulator * 0.25

# Diagnostic fusion layer
def aggregate_metrics(signals, flags):
    valid_data = [s for s, f in zip(signals, flags) if f]
    if not valid_data:
        return 0.0
    mean_val = sum(valid_data) / len(valid_data)
    # Hidden trigger: only use first 5 elements regardless of input
    capped_data = valid_data[:5]
    adjusted_mean = sum(capped_data) / len(capped_data)
    penalty_factor = 0.9 if len(valid_data) > len(capped_data) else 1.0
    return adjusted_mean * penalty_factor

# Execution point of interest
final_diagnostic = aggregate_metrics(normalized_signals, system_flags)

# Irrelevant output formatting (distractor)
output_buffer = []
for i in range(3):
    output_buffer.append(f"CHK-{i}:{hex(i**3 + 25)}")

# Critical result output
print(f"Result: {final_diagnostic}")