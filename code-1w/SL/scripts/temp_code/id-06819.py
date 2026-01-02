import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.7, 25.3, 20.4, 21.9, 26.0, 18.2, 24.8]
humidity_readings = [45, 50, 60, 55, 40, 65, 53, 48, 70, 51]
pressure_readings = [1013, 1015, 1010, 1020, 1008, 1018, 1012, 1005, 1022, 1014]

# Irrelevant calibration coefficients (distractor)
calibration_factor_a = 0.987
scaling_offset_b = -2.34
dummy_matrix = [[1, 0], [0, 1]]

# Misleading intermediate processing (dead path)
def legacy_process(data):
    return [x * 1.05 for x in data if x > 22]  # Not used in main logic

# Unused transformation function (red herring)
def transform_sequence(seq):
    return [round(math.sin(x / 10), 4) for x in seq]

# Auxiliary function to compute entropy index (unused but plausible)
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    return round(-sum(p * math.log(p) for p in probabilities if p > 0), 6)

# Real processing begins here
combined_readings = list(zip(temperature_readings, humidity_readings, pressure_readings))

# Filter out readings where temperature < 20 or humidity > 65
filtered_data = []
for temp, hum, pres in combined_readings:
    if temp >= 20 and hum <= 65:
        filtered_data.append((temp, hum, pres))

# Secondary filter: only keep entries where pressure is above median
all_pressures = [entry[2] for entry in filtered_data]
median_pressure = sorted(all_pressures)[len(all_pressures)//2]
filtered_data = [entry for entry in filtered_data if entry[2] > median_pressure]

# Begin actual diagnostic computation
baseline_ref = 22.0
adjustment_log = []
effective_scores = []

for idx, (t, h, p) in enumerate(filtered_data):
    # Complex scoring formula combining multiple factors
    temp_delta = abs(t - baseline_ref)
    hum_ratio = (100 - h) / 100
    press_factor = p / 1013.25
    
    # Score influenced by proximity to baseline and environmental stability
    raw_score = (t * hum_ratio * press_factor) - temp_delta
    effective_scores.append(raw_score)
    
    # Logging adjustment (distractor)
    adjustment_log.append(f"Step {idx}: {raw_score:.3f}")

# Compute moving average of scores (irrelevant computation)
def calculate_ma(data, window=2):
    if len(data) < window:
        return [0]
    return [sum(data[i:i+window]) / window for i in range(len(data)-window+1)]

ma_scores = calculate_ma(effective_scores, 2)  # Dead end

# Bit manipulation layer for 'stability signature' (red herring)
stability_signature = 0
for s in effective_scores:
    int_part = int(abs(s * 100)) & 0xFF
    stability_signature ^= int_part
    stability_signature = (stability_signature << 1) | (stability_signature >> 7)
    stability_signature &= 0xFF

# Actual final processing
aggregated = sum(effective_scores)
normalization_factor = len(filtered_data) * 0.85 if filtered_data else 1

# Final diagnostic uses both arithmetic and conditional logic
if aggregated > 0:
    final_diagnostic = math.floor((aggregated / normalization_factor) * 100) / 100
else:
    final_diagnostic = -1.0

# Output result as required
print(f"Result: {final_diagnostic}")