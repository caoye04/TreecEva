from collections import defaultdict, Counter

# Simulated sensor data from a distributed environmental monitoring system
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 23.7]
humidity_readings = [45, 47, 46, 50, 52, 49, 48]
pressure_readings = [1013, 1015, 1012, 1010, 1014, 1016, 1011]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B3', 'C9', 'D1', 'E8']
error_flags = {code: False for code in legacy_codes}
checksum_lookup = defaultdict(lambda: 0)
for i, code in enumerate(legacy_codes):
    checksum_lookup[code] = (i + 1) * len(code)

# Data transformation pipeline
smoothed_temps = [round(t * 1.01, 2) for t in temperature_readings]  # minor calibration
humidity_bins = Counter([h // 5 * 5 for h in humidity_readings])

# Misleading intermediate calculations (red herring)
avg_pressure = sum(pressure_readings) / len(pressure_readings)
pressure_variance = sum((p - avg_pressure) ** 2 for p in pressure_readings) / len(pressure_readings)
theoretical_max = max(smoothed_temps) * 1.5

# Core signal extraction (relevant)
base_signal = sum(smoothed_temps) / len(smoothed_temps)
amplitude_fluctuation = max(smoothed_temps) - min(smoothed_temps)
phase_modulator = int(base_signal) % 4 or 1

# Decoy function that looks important but isn't used in final result
def compute_entropy(data):
    freqs = Counter(data)
    total = len(data)
    return -sum((count / total) * (count / total).__log__ for count in freqs.values())

# Another decoy: complex but unused transformation
temp_histogram = []
for temp in smoothed_temps:
    bucket = int((temp - 20) * 2)
    temp_histogram.append(f"T{bucket}:{'+' * int(temp % 1 * 10)}")

# Real computation path begins here
weight_map = list(map(lambda x: 0.5 + (x - 20) / 100, smoothed_temps))
weighted_sum = sum(w * t for w, t in zip(weight_map, smoothed_temps))
aggregate_score = int(weighted_sum * 2)

# Temperature factor derived from fluctuation patterns
if amplitude_fluctuation > 2.0:
    temperature_factor = 15
else:
    temperature_factor = 8

# Dead code path (never executed - distraction)
if __debug__:
    debug_snapshot = {
        'raw': temperature_readings[:],
        'calibrated': smoothed_temps,
        'weights': weight_map
    }
    for k in debug_snapshot:
        pass  # placeholder logic

# Critical execution point
final_diagnostic = aggregate_score + temperature_factor * phase_modulator

# Output result
print(f"Result: {final_diagnostic}")