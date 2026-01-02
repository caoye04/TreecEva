import itertools

# Simulated agricultural sensor data (temperature, humidity, soil_moisture)
data_stream = [(28, 65, 42), (31, 70, 38), (25, 80, 45), (33, 60, 35), (27, 75, 40)]

# Irrelevant baseline constants (distractors)
BASELINE_TEMP = 20
BASELINE_HUMIDITY = 50
NORMAL_GROWTH_RATE = 1.05
PREDICTION_OFFSET = 0.07

# Preprocessing: filter out extreme values using zip and enumerate
cleaned_data = []
for i, (temp, hum, moist) in enumerate(data_stream):
    if temp > 32 or temp < 24:
        continue  # Skip outlier temperatures
    cleaned_data.append((temp, hum, moist))

# Dead code path - never executed due to condition (red herring)
optimized_settings = []
if len(cleaned_data) > 10:
    for t, h, m in cleaned_data:
        optimized_settings.append((t - 2, h + 5, m * 1.1))

# Transform data using rolling average (only relevant part)
smoothed = []
for i in range(len(cleaned_data) - 1):
    prev = cleaned_data[i]
    curr = cleaned_data[i + 1]
    avg_temp = (prev[0] + curr[0]) / 2
    avg_hum = (prev[1] + curr[1]) / 2
    avg_moist = (prev[2] + curr[2]) / 2
    smoothed.append((avg_temp, avg_hum, avg_moist))

# Apply correction factors with string-based mode selection (misleading use of string methods)
mode_flag = 'CALIBRATE_HIGH'
adjustment_factor = 1.1 if 'HIGH' in mode_flag else 1.0
inverse_factor = 0.9 if mode_flag.lower().startswith('calibrate') else 1.0  # Distractor

# Spurious transformation chain (some steps are irrelevant)
shifted = []
for temp, hum, moist in smoothed:
    adjusted_temp = temp * adjustment_factor
    # The following line has no real effect on output (dead computation)
    normalized_index = (hum - 50) / 100  
    adjusted_moist = moist * (1 + (hum - 60) / 100)
    shifted.append((adjusted_temp, hum, adjusted_moist))

# Introduce bit manipulation for 'sensor stability check' (mostly decoy logic)
stability_scores = []
for i, (t, h, m) in enumerate(shifted):
    raw_score = int(t) ^ int(m)  # XOR of truncated values
    parity = bin(raw_score).count('1') % 2
    # Only parity influences next step; most of this is distraction
    stability_scores.append(parity)

# Masking operation with itertools.cycle (complex but partially irrelevant)
mask_pattern = [1, -1]
masked = []
for (t, h, m), mask in zip(shifted, itertools.cycle(mask_pattern)):
    masked.append((t * mask, h, m * mask))  # Only sign flip, not meaningful

# Reconstruct positive values (undo masking - net zero effect, red herring chain)
adjusted_data = []
for t, h, m in masked:
    abs_t, abs_m = abs(t), abs(m)
    adjusted_data.append((abs_t, h, abs_m))

# Real processing begins here — only now we compute yield factors
# Each tuple contributes to yield based on thresholds
yield_factors = []
for temp, hum, moist in adjusted_data:
    base_yield = 100
    if temp > 30:
        base_yield -= 10
    elif temp < 26:
        base_yield -= 5
    if moist < 38:
        base_yield -= 8
    if hum > 70:
        base_yield += 3  # Slight boost
    yield_factors.append(base_yield)

# Final aggregation using weighted sum (key logic)
def process_harvest(data_list):
    total = 0
    weights = [0.8, 1.0, 1.2]  # Increasing importance over time
    for i, entry in enumerate(data_list):
        _, _, moist_val = entry
        weight = weights[min(i, len(weights) - 1)]
        # Actual contribution is based on moisture and fixed offset
        total += (moist_val + 37) * weight
    return int(total)  # Deterministic integer result

# Critical assignment statement
final_yield = process_harvest(adjusted_data)

# Output required format
print(f"Target result: {final_yield}")