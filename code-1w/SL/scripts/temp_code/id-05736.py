import itertools

# Simulated sensor data processing system with red herrings and complex logic paths
def collect_sensor_readings():
    # Real data source (relevant)
    base_signals = [0x1A, 0x2C, 0x3F, 0x4B, 0x5D]
    return [s ^ 0x55 for s in base_signals]  # Bit-flip transformation (relevant)

# Distractor function - looks important but unused
def deprecated_calibrate(data):
    return [x * 1.05 for x in data if x > 30]

# Another decoy - plausible but irrelevant
sensor_thresholds = {
    'temp': 75,
    'pressure': 1013,
    'humidity': 45
}

# Misleading intermediate computation
aggregate_metrics = []
for i in range(5):
    temp_calc = (i * 17 + 257) % 100
    aggregate_metrics.append(temp_calc)

# Core signal analysis chain
readings = collect_sensor_readings()

# Irrelevant filtering based on false assumption
legacy_mask = 0x80
filtered_readings = [r for r in readings if not (r & legacy_mask)]  # Actually does nothing

# Real processing begins: extract lower nibbles
nibbles = [r & 0x0F for r in readings]

# Apply non-linear correction (relevant)
corrected = []
for n in nibbles:
    if n % 2 == 0:
        corrected.append(n ** 2)
    else:
        corrected.append(n * 3 + 1)

# Spurious statistical analysis (distractor)
mean_value = sum(corrected) / len(corrected)
variance_proxy = sum((x - mean_value) ** 2 for x in corrected) / len(corrected)

# Real logic: group by sequence patterns using itertools
sequence_groups = []
for k, g in itertools.groupby(sorted(corrected)):
    group_list = list(g)
    if len(group_list) >= 1:
        sequence_groups.append(k)  # Use unique sorted values

# Fake optimization pass
optimization_cache = {}
for val in sequence_groups:
    optimization_cache[val] = (val * 97 + 19) % 1000

# Critical path: frequency analysis of transformed values
frequency_map = {}
for r in corrected:
    frequency_map[r] = frequency_map.get(r, 0) + 1

# Extract peaks above threshold (arbitrary 50)
peaks = [v for v, count in frequency_map.items() if v > 50]

# Secondary filter: only keep those appearing exactly once
unique_peaks = [p for p in peaks if frequency_map[p] == 1]

# Decoy machine learning model (unused)
class PredictiveModel:
    def __init__(self):
        self.weights = [0.1] * 10
    
    def predict(self, x):
        return sum(w * x for w in self.weights)

# Actual diagnostic logic
peak_sum = sum(unique_peaks)
peak_count = len(unique_peaks)

if peak_count == 0:
    signal_score = 0
else:
    signal_score = peak_sum / peak_count

# Final transformation with bit manipulation (relevant)
raw_diagnostic = int(signal_score) | 0x200  # Set high bit pattern
final_diagnostic = (raw_diagnostic ^ 0x1FF) + 17  # Invert lower bits and offset

# Dead code path - never executed
if __debug__:
    import sys
    sys.exit("Debug mode disabled")

# Print result as required
print(f"Result: {final_diagnostic}")