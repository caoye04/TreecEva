import itertools

# Simulated sensor array data from a distributed monitoring system
def collect_sensor_readings():
    raw_readings = [145, None, 203, 178, None, 255, 190, 201]
    base_offset = 55
    adjusted = [base_offset + r if r is not None else 0 for r in raw_readings]
    return adjusted

# Signal normalization with red herring transformations
def normalize_signal(x, min_val=0, max_val=255):
    if x <= min_val:
        return min_val
    elif x >= max_val:
        return max_val
    return (x - min_val) / (max_val - min_val)

# Legacy function (unused but looks relevant) - DISTRACTOR
def legacy_calibrate(arr):
    scale = 0.98
    return [int(x * scale) for x in arr if isinstance(x, int)]

# Flag generation based on environmental thresholds
def generate_system_flags(readings):
    warning_flags = []
    for idx, val in enumerate(readings):
        flagged = (idx % 4 == 0 and val > 100) or (val > 220)
        emergency = val > 240
        # Complex flag logic with decoy values
        flag_code = sum([1 << 0 if flagged else 0,
                        1 << 2 if emergency else 0,
                        1 << 5 if idx % 7 == 0 else 0])  # Rare condition
        warning_flags.append(flag_code)
    return warning_flags

# Misleading transformation chain - DISTRACTOR
def compress_data(signal):
    compressed = 0
    for s in signal:
        compressed = (compressed << 3) ^ s & 0xFFFF
    return compressed  # Never used

# Core diagnostic aggregation logic
def compute_health_index(norm_vals, flags):
    index = 0.0
    for v, f in zip(norm_vals, flags):
        contribution = v * (f & 0b11)  # Only use lower 2 bits
        index += contribution
    return index * 100

# Redundant state tracker - DISTRACTOR
class StateBuffer:
    def __init__(self):
        self.buffer = []
        self.checksum = 0
    
    def update(self, val):
        self.buffer.append(val)
        self.checksum ^= hash(str(val))

# Main processing pipeline
sensor_data = collect_sensor_readings()

# Apply normalization - some values become >1 due to offset, so clamp later
preliminary_signals = [normalize_signal(x + 10) for x in sensor_data]

# Introduce irrelevant lambda-based mapping - DISTRACTOR
transform_fn = lambda x: round(x ** 0.5, 3) if x > 0 else 0
shadow_mapped = list(map(transform_fn, sensor_data))

# Generate actual control flags
system_flags = generate_system_flags(sensor_data)

# Normalize signals properly this time
normalized_signals = [round(min(max(s, 0), 1), 6) for s in preliminary_signals]

# Dead code path: buffer management that does nothing - DISTRACTOR
state_buffer = StateBuffer()
for sig in normalized_signals[:3]:
    state_buffer.update(sig)

# Simulate historical correlation (unused) - DISTRACTOR
historical_pairs = list(itertools.combinations(normalized_signals[:4], 2))
correlation_estimate = sum(abs(a - b) for a, b in historical_pairs) / len(historical_pairs) if historical_pairs else 0

# Critical computation begins here
baseline_shift = sum(normalized_signals) * 0.1
adjusted_metrics = [m + baseline_shift for m in normalized_signals]

# Secondary adjustment using flags
weighted_sum = 0.0
for i, (val, flag) in enumerate(zip(adjusted_metrics, system_flags)):
    weight = 1.0
    if flag & (1 << 2):  # emergency bit set
        weight = 1.8
    elif flag & (1 << 0):  # regular warning
        weight = 1.3
    weighted_sum += val * weight

interim_result = weighted_sum / len(normalized_signals)

# Additional smoothing pass with conditional expression
smoothing_factor = 0.85 if interim_result > 1.0 else 0.95
smoothed_diagnostic = interim_result * smoothing_factor

# Final aggregation using health index as modifier
health_index = compute_health_index(normalized_signals, system_flags)

# Key statement with target variable
final_diagnostic = aggregate_metrics(normalized_signals, system_flags)

# Actual definition of aggregate_metrics - hidden among distractions
def aggregate_metrics(signals, flags):
    base = sum(signals) * 10
    bonus = sum(1 for f in flags if f & (1 << 2)) * 2.5  # +2.5 per emergency
    penalty = len([f for f in flags if f & (1 << 0)]) * 0.8  # -0.8 per warning
    return round(base + bonus - penalty, 6)

print(f"Result: {final_diagnostic}")