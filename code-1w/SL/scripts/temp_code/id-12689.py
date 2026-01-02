import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 23.7]
humidity_readings = [45, 47, 50, 44, 46, 48, 49]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1013]

# Irrelevant transformation: unused FFT-like dummy processing
dummy_spectrum = [abs((t - 24) * 1j + (h - 45)) for t, h in zip(temperature_readings, humidity_readings)]
filtered_spectrum = [x for x in dummy_spectrum if x > 1.5]  # Dead-end analysis

# Real data path begins: normalize readings to baseline
norm_temps = [(t - 20) / 5 for t in temperature_readings]  # Convert to relative thermal index
norm_humidity = [h / 100 for h in humidity_readings]  # Fractional humidity

# Compute volatility (standard deviation approximation)
mean_temp = sum(norm_temps) / len(norm_temps)
temp_variance = sum((x - mean_temp) ** 2 for x in norm_temps)
temp_volatility = temp_variance ** 0.5

# Distractor: complex wavelet-inspired decomposition (unused)
def wavelet_decompose(series):
    if len(series) < 2:
        return series, []
    averaged = [(series[i] + series[i+1]) / 2 for i in range(0, len(series)-1, 2)]
    difference = [series[i] - series[i+1] for i in range(0, len(series)-1, 2)]
    return averaged, difference

# Unused recursive call creates red herring
_, _ = wavelet_decompose(pressure_readings)

# Real logic: detect anomalies using sliding window
anomaly_flags = []
for i in range(2, len(norm_temps)):
    window_avg = sum(norm_temps[i-2:i+1]) / 3
    if abs(norm_temps[i] - window_avg) > 0.15:
        anomaly_flags.append(1)
anomaly_count = sum(anomaly_flags)

# Secondary metric: stability score based on humidity consistency
consecutive_stable = 0
max_stable_run = 0
for h in norm_humidity:
    if 0.4 <= h <= 0.5:
        consecutive_stable += 1
    else:
        max_stable_run = max(max_stable_run, consecutive_stable)
        consecutive_stable = 0
max_stable_run = max(max_stable_run, consecutive_stable)

# Bit manipulation decoy: simulate checksum (not actually used in final result)
raw_bytes = [int(t * 10) for t in temperature_readings]
fake_checksum = 0
for b in raw_bytes:
    fake_checksum ^= b
    fake_checksum = (fake_checksum << 1) | (fake_checksum >> 7)
fake_checksum &= 0xFF  # Truncated and unused

# String-based distractor: encode status messages (irrelevant to output)
sensor_status = ['OK' if t < 25 else 'HIGH' for t in temperature_readings]
status_summary = ''.join([s[0] for s in sensor_status])
segmented = status_summary.split('H')
reconstructed = '-'.join(segmented)  # Nowhere used

# Real calculation chain begins here
base_index = sum(norm_temps) * 100
volatility_penalty = temp_volatility * 50
aggregate_score = base_index - volatility_penalty

# Hidden dependency: use itertools to generate weight combinations
weight_candidates = list(itertools.product([0.8, 0.9, 1.0], repeat=2))
precision_weight = weight_candidates[anomaly_count % len(weight_candidates)][0]  # Actual use

# Unused slicing operation creates distraction
temp_slice = temperature_readings[1:5:2]
spurious_sum = sum(temp_slice) / len(temp_slice)

# Set operations as secondary distractor
even_pressures = set(p for p in pressure_readings if p % 2 == 0)
odd_pressures = set(p for p in pressure_readings if p % 2 == 1)
pressure_gcd = len(even_pressures & odd_pressures)  # Always 0, misleading

# Critical statement with key variable assignment
correction_factor = max_stable_run * 2.5
final_diagnostic = aggregate_score + correction_factor * precision_weight

print(f"Result: {final_diagnostic}")