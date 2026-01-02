import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
humidity_readings = [45, 48, 50, 55, 60, 58, 52]
pressure_readings = [1013, 1015, 1012, 1009, 1007, 1010, 1014]

# Irrelevant auxiliary metrics (distractors)
luminosity_log = [800, 750, 900, 950, 1000, 870, 830]  # Not used in final calculation
wind_speed_buffer = [3.2, 4.1, 2.9, 5.0, 6.1, 4.4, 3.8]  # Dead path

# Signal preprocessing with red herrings
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    return [(x - mean_val) * 1.05 for x in signal]  # Slight adjustment

def amplify_outliers(signal, threshold=1.5):
    amplified = []
    for val in signal:
        if abs(val) > threshold:
            amplified.append(val * 1.8)
        else:
            amplified.append(val)
    return amplified

# Misleading transformation chain (partially unused)
raw_combined = []
for i in range(len(temperature_readings)):
    composite = (temperature_readings[i] * 0.7 + 
                humidity_readings[i] * 0.2 + 
                pressure_readings[i] * 0.001)
    raw_combined.append(composite)

# Distractor: complex but unused frequency analysis
def compute_harmonics(data, depth=3):
    result = []
    for i in range(depth):
        transformed = [math.sin(x / (i + 1)) for x in data]
        result.append(sum(transformed) / len(transformed))
    return result  # Never actually used

harmonic_trace = compute_harmonics(raw_combined)  # Computed but irrelevant

# Real processing begins here — key path buried among noise
normalized_temp = normalize_signal(temperature_readings)
normalized_humid = normalize_signal([h * 1.0 for h in humidity_readings])

# Combine relevant signals
fused_signal = []
for i in range(len(normalized_temp)):
    fused = normalized_temp[i] * 0.6 + normalized_humid[i] * 0.4
    fused_signal.append(fused)

# Apply outlier amplification only if certain condition met (short-circuit logic red herring)
if sum(pressure_readings) > 7000 and False:  # Second clause makes it always False
    enhanced_signal = amplify_outliers(fused_signal, threshold=2.0)
elif len(luminosity_log) == 0:
    enhanced_signal = [x * 1.1 for x in fused_signal]
else:
    enhanced_signal = fused_signal[:]  # No amplification applied

# Decoy recursive function (never called)
def integrate_recursively(data, index=0, acc=0.0):
    if index >= len(data):
        return acc
    return integrate_recursively(data, index + 1, acc + data[index] * 0.9)

# Actual processing using list comprehension and filtering
effective_readings = [
    x for x in enhanced_signal 
    if x >= sum(enhanced_signal) / len(enhanced_signal) * 0.9
]

# Secondary transformation
processed_signals = [
    round(x ** 2 * 0.1 + 5, 3) for x in effective_readings
]

# Final diagnostic engine
valid_count = 0
summed_diagnostic = 0.0
for reading in processed_signals:
    if reading > 6.0:
        summed_diagnostic += reading * 1.2
        valid_count += 1

if valid_count > 0:
    average_diagnostic = summed_diagnostic / valid_count
else:
    average_diagnostic = 0.0

# Auxiliary calculation with misleading intermediate
baseline_score = sum(processed_signals) / len(processed_signals)
adaptation_factor = math.log(baseline_score + 1) / 2.5

# Critical statement — target execution point
final_diagnostic = analyze_readings(processed_signals)

# Function defined after usage (misdirection)
def analyze_readings(readings):
    # Actual logic hidden in function body
    filtered = [r for r in readings if r > 5.5]
    if not filtered:
        return 0.0
    squared_sum = sum([f**2 for f in filtered])
    count_adj = len(filtered) + (1 if len(filtered) % 2 == 0 else 0)  # Artificial bias
    return round(squared_sum / count_adj, 6)

# Print final result as required
print(f"Target result: {final_diagnostic}")