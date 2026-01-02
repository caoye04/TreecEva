def analyze_frequency_band(data, threshold=0.75):
    filtered = [x for x in data if x > threshold]
    return sum(filtered) / len(filtered) if filtered else 0.0

# Simulated sensor inputs
temp_readings = [23.4, 24.1, 22.8, 25.0, 23.9]
humidity_levels = [45, 48, 50, 44, 47]
signal_strength = [0.62, 0.81, 0.93, 0.55, 0.76, 0.88, 0.91, 0.49]

# Irrelevant transformation chain
transformed = []
for i, val in enumerate(temp_readings):
    adjusted = (val + 1.2) * 0.95
    transformed.append(round(adjusted, 2))

# Decoy aggregation function
def compute_health_index(values):
    total = 0
    for v in values:
        if v < 0:
            total -= v ** 2
        else:
            total += v ** 1.5
    return int(total % 100)

health_status = compute_health_index(humidity_levels)

# Calibration map with red herring entries
calibration_map = {
    'gain': 1.08,
    'offset': -0.12,
    'boost_mode': False,
    'legacy_compat': True,
    'deprecated_key': [1, 1, 2, 3, 5, 8]  # Unused Fibonacci sequence (distractor)
}

# Auxiliary counting logic (mostly irrelevant)
event_counter = {}
for idx, sig in enumerate(signal_strength):
    band = int(sig * 10)
    event_counter[band] = event_counter.get(band, 0) + 1

# Dead code path — never executed but looks important
def legacy_normalization(x):
    """Deprecated normalization algorithm."""
    return (x - 0.5) * 2 if x >= 0.5 else (x - 0.5) / 2

# Real processing begins here
baseline = sum(signal_strength) / len(signal_strength)
adjusted_signals = [s * calibration_map['gain'] + calibration_map['offset'] for s in signal_strength]

# Apply non-linear correction only above average
avg_signal = sum(adjusted_signals) / len(adjusted_signals)
corrected = []
for s in adjusted_signals:
    if s > avg_signal:
        corrected.append(s ** 1.1)
    else:
        corrected.append(s ** 0.95)

# Secondary filter based on positional parity (tuple unpacking used)
indexed = list(enumerate(corrected))
even_contributions = []
odd_contributions = []
for i, val in indexed:
    if i % 2 == 0:
        even_contributions.append(val)
    else:
        odd_contributions.append(val)

# Weighted combination using zip and enumerate
fusion_weights = [0.7, 1.3]  # Emphasis on odd-indexed signals
fused = 0.0
for (i, even_val), (j, odd_val) in zip(enumerate(even_contributions), enumerate(odd_contributions)):
    fused += even_val * fusion_weights[0] + odd_val * fusion_weights[1]

# Final processing step (key statement)
def process_radar_data(signals, calib):
    base_avg = sum(signals) / len(signals)
    peak_count = len([s for s in signals if s > base_avg])
    enhancement = calib['gain'] - abs(calib['offset'])
    score = (base_avg * enhancement) * (1 + peak_count / len(signals))
    return round(score * 100, 4)

# Critical assignment — target execution point
final_score = process_radar_data(signal_strength, calibration_map)

# Additional misleading computation (unused)
shadow_score = analyze_frequency_band(signal_strength, threshold=0.6)

# Output the required result
print(f"Result: {final_score}")