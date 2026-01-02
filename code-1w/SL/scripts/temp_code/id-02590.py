import math

# Simulated sensor array diagnostics with noise filtering and data transformation
raw_readings = [3.2, 1.8, 4.5, 0.9, 2.7, 5.1, 3.6, 2.4, 4.0, 1.2]
baseline_offset = 1.5
calibration_factor = 0.85

# Irrelevant auxiliary variables (distractors)
heartbeat_pattern = [72, 75, 68, 78, 81]
dummy_checksum = sum(heartbeat_pattern) % 17
temporal_weights = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
scaling_exponent = 1.2

# Real processing path begins
adjusted_readings = [x - baseline_offset for x in raw_readings]

# Apply non-linear correction using calibration factor and exponent
nonlinear_correction = lambda val: round(val * calibration_factor ** scaling_exponent, 4)
corrected_readings = list(map(nonlinear_correction, adjusted_readings))

# Filter out negative values (invalid sensor states)
filtered_metrics = [x for x in corrected_readings if x > 0]

# Window-based transformation: take every second element starting from index 1
transformed_metrics = filtered_metrics[1::2]  # slicing operation

# Decoy function – looks important but unused
def compute_thermal_gradient(data):
    return sum(d ** 1.1 for d in data if d > 2) / (len(data) + 1)

# Another decoy: dead code path
if len(raw_readings) > 20:
    transformed_metrics.append(999.9)

# Critical aggregation logic
aggregation_kernel = lambda x, y: x * 0.7 + y * 0.3

def rolling_reduce(data, func):
    result = data[0]
    for i in range(1, len(data)):
        result = func(result, data[i])
    return round(result, 4)

# Secondary decoy: complex but unused structure
class DiagnosticBuffer:
    def __init__(self, size):
        self.data = [0.0] * size
    def push(self, val):
        self.data.pop(0)
        self.data.append(val)

buffer = DiagnosticBuffer(5)
buffer.push(sum(corrected_readings))  # irrelevant usage

# Real aggregation
intermediate_sum = sum(transformed_metrics)
intermediate_avg = intermediate_sum / len(transformed_metrics)
scaled_intermediate = intermediate_avg * 1.4

# Final diagnostic computed via rolling reduction
final_diagnostic = rolling_reduce(transformed_metrics, aggregation_kernel)

# Misleading print statements (distraction)
print(f"Raw count: {len(raw_readings)}")
print(f"Filtered metrics count: {len(filtered_metrics)}")
print(f"Transformed metrics: {transformed_metrics}")
print(f"Intermediate average: {intermediate_avg:.4f}")
print(f"Scaling check: {scaled_intermediate:.4f}")

# Key output
print(f"Target result: {final_diagnostic}")