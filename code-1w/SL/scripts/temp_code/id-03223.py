import math

# Simulated sensor array diagnostics with embedded logic chain
def analyze_sensor_node(node_id, readings):
    if len(readings) < 5:
        return 0
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return math.sqrt(variance) if avg > 0 else -math.sqrt(abs(variance))

# Irrelevant helper - dead path (never called in execution)
def deprecated_calibrate(x):
    return (x * 0.92 + 3.7) % 1.0

# Data transformation pipeline stage 1
def generate_signature(sequence):
    base_sig = [math.sin(x / 10.0) * 100 for x in sequence]
    filtered = [val for val in base_sig if abs(val) > 10]
    return filtered[:10]

# Misleading normalization function (used only on decoy data)
def normalize_intensities(data):
    max_val = max(data)
    min_val = min(data)
    if max_val == min_val:
        return [0.5] * len(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Unused but plausible-looking diagnostic mode
DECOY_MODE = True
def compute_entropy(values):
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    probs = [count / len(values) for count in counts.values()]
    return -sum(p * math.log2(p) for p in probs if p > 0)

# Core processing logic
threshold_map = {
    't1': 42.5,
    't2': -15.3,
    't3': 88.0
}

sensor_data = {
    101: [12, 15, 14, 18, 16, 13],
    102: [9, 11, 10, 10, 12],
    103: [20, 25, 23, 21, 24, 22, 26],
    104: [5],  # insufficient data
    105: [30, 33, 31, 32]
}

# Secondary transformation - appears important but used only partially
def apply_correction(signal, factor=0.85):
    return [x * factor for x in signal if x > 0]

# Complex multi-stage calibration sequence
raw_sequence = list(range(5, 105, 7))  # [5, 12, 19, ... , 96]
calibration_sequence = generate_signature(raw_sequence)

# Apply corrections to subset (only first 5 elements)
calibration_sequence = apply_correction(calibration_sequence[:5], 1.1)

# Diagnostic node analysis (real computation branch)
sensor_diagnostics = {}
for nid, data in sensor_data.items():
    score = analyze_sensor_node(nid, data)
    sensor_diagnostics[nid] = round(score, 3)

# Red herring: entropy calculation on irrelevant data
entropy_probe = compute_entropy([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

# Actual key logic hidden among distractions
def evaluate_stability(diagnostics, config):
    active_nodes = [v for v in diagnostics.values() if v != 0]
    if not active_nodes:
        return 0.0
    net_drift = sum(active_nodes)
    node_count = len(active_nodes)
    adjustment = config['t1'] * 0.1 - config['t2'] * 0.05
    return net_drift + adjustment

# Another decoy structure
class DiagnosticBuffer:
    def __init__(self):
        self.buffer = []
        self.limit = 100

    def push(self, val):
        if len(self.buffer) < self.limit:
            self.buffer.append(val)

# Unused instance (distraction)
db = DiagnosticBuffer()

# Main metric processor - depends on multiple prior results
def process_metrics(metrics, config):
    if not metrics:
        return -999
    
    # Real signal extraction
    magnitude = sum(abs(m) for m in metrics)
    scale_factor = math.cos(len(metrics) * 0.1)
    
    # Critical dependency on evaluate_stability
    stability_score = evaluate_stability(sensor_diagnostics, config)
    
    # Final composition with nonlinear transformation
    raw_output = magnitude * scale_factor + stability_score
    
    # Final adjustment based on threshold logic
    if raw_output > config['t3']:
        return raw_output * 0.75
    elif raw_output < -config['t3']:
        return raw_output * 1.25
    else:
        return raw_output + 10.5

# Execution point of interest
final_diagnostic = process_metrics(calibration_sequence, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")