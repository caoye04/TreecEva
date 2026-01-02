from collections import defaultdict, Counter

# Simulated sensor grid data with noise and redundant diagnostics
data_stream = [
    (1, 23.5, 'active'), (2, 24.1, 'idle'), (3, 19.8, 'active'),
    (1, 22.7, 'active'), (4, 30.0, 'overload'), (2, 25.3, 'active'),
    (5, 18.9, 'idle'), (3, 20.1, 'active'), (1, 24.0, 'overload'),
    (6, 27.5, 'active'), (4, 29.8, 'overload'), (2, 26.0, 'active')
]

# Irrelevant statistical counters (distractor)
stale_counter = defaultdict(int)
mode_frequency = Counter()
for _, temp, mode in data_stream:
    stale_counter[int(temp)] += 1
    mode_frequency[mode] += 1

# Misleading pre-processing: appears important but unused later
baseline_shift = sum(t for _, t, _ in data_stream) / len(data_stream)
scaled_readings = [t - baseline_shift for _, t, _ in data_stream]
outlier_flags = [abs(sr) > 2 for sr in scaled_readings]

# Core logic disguised among red herrings
sensor_cache = {}
status_weights = {'active': 1, 'idle': 0, 'overload': -2}

# Simulated hardware thresholds (some irrelevant)
thresh_A = 20.0
thresh_B = 25.0
thresh_C = 28.0  # Unused threshold - red herring

# Primary filtering based on dynamic criteria
recent_ids = set()
working_data = []
for sid, temp, status in data_stream:
    if status == 'overload' and temp > thresh_B:
        continue  # Drop overload states above threshold B
    if sid not in recent_ids:
        working_data.append((sid, temp, status))
        recent_ids.add(sid)

# Secondary transformation with distraction
transformed = []
rolling_adjustment = 0
for i, (sid, temp, status) in enumerate(working_data):
    if i % 2 == 0:
        rolling_adjustment += 0.5
    adjusted_temp = temp + rolling_adjustment
    transformed.append((sid, adjusted_temp, status_weights[status]))

# Dead code path - simulates fault detection but unused
if any(w < 0 for _, _, w in transformed):
    fault_signature = [sid for sid, _, w in transformed if w < 0]
    correction_factor = -sum(w for _, _, w in transformed if w < 0)
else:
    fault_signature = []
    correction_factor = 0

# Actual filtering happens here — subtle and buried
filtered_data = [t for sid, t, w in transformed if w != 0 and t > thresh_A]

# Recursive processing function (core relevant logic)
def integrate_sample(values, index=0):
    if index >= len(values):
        return 0
    if values[index] < thresh_B:
        return values[index] + integrate_sample(values, index + 1) * 0.9
    else:
        return integrate_sample(values, index + 1)

# Auxiliary decoy function — looks important but never called
def legacy_calibrate(seq):
    total = 0
    for x in seq:
        total = (total * 1.1 + x) % 100
    return round(total, 3)

# Another unused utility (distraction)
class DiagnosticBuffer:
    def __init__(self):
        self.buffer = []
        self.limit = 5
    
    def append(self, val):
        self.buffer.append(val)
    
    def get_peak(self):
        return max(self.buffer) if self.buffer else 0

# Critical processing chain
rolling_integral = integrate_sample(filtered_data)

# Hash-based integrity check (irrelevant computation)
data_hash = sum((hash(str(d)) % 1000) for d in filtered_data) % 100

# Final computation buried in semantics
def process_readings(readings):
    if not readings:
        return 0.0
    sorted_vals = sorted(readings)
    mid_index = len(sorted_vals) // 2
    median_val = sorted_vals[mid_index] if len(sorted_vals) % 2 else (
        sorted_vals[mid_index - 1] + sorted_vals[mid_index]
    ) / 2
    return round(median_val * rolling_integral / (1 + data_hash / 10), 6)

# Key execution point
final_diagnostic = process_readings(filtered_data)

print(f"Result: {final_diagnostic}")