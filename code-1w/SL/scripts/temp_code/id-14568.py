import math

# Sensor simulation system for environmental monitoring (distractor module)
def generate_synthetic_data(size):
    return [math.sin(i * 0.1) + 0.5 for i in range(size)]

# Irrelevant utility: string-based status formatter (dead code path)
def format_status(code, name):
    status_map = {'OK': 200, 'WARN': 301, 'ERR': 500}
    prefix = f'SYS-{code}'
    label = name.upper().replace(' ', '_')
    return f'{prefix}:{label}::{status_map.get("OK", 0)}'

# Unused signal processing helper (decoy function)
def apply_filter(signal, kernel_size=3):
    smoothed = []
    for i in range(len(signal)):
        window = signal[max(0, i-kernel_size//2):min(len(signal), i+kernel_size//2+1)]
        smoothed.append(sum(window)/len(window))
    return smoothed

# Core metric transformer – only partially relevant
# Preprocesses raw metrics using exponential smoothing factor
# This function is used, but contains red herring operations

def preprocess_metric(value, alpha=0.3):
    if value < 0:
        temp_offset = -0.1 * value
    else:
        temp_offset = 0.05 * value
    
    # Distracting transformation chain
    adjusted = abs(value) ** 0.5 + temp_offset
    enhanced = adjusted * (1 + math.sin(math.pi / 4))
    refined = round(enhanced, 3)
    
    # Real transformation branch
    if refined > 10:
        return refined / 2.5
    elif refined > 5:
        return refined * 0.8
    else:
        return refined + 1.2

# Auxiliary calculator for fake subsystem health (irrelevant)
def compute_health_score(metrics):
    base = sum(m ** 0.7 for m in metrics[:5])
    penalty = len([m for m in metrics if m < 0]) * 0.3
    return round(base - penalty, 2)

# Misleading data structure – looks important but unused
system_snapshot = {
    'timestamp': 1719865234,
    'readings_count': 0,
    'calibration': {
        'offset_x': 0.002,
        'offset_y': -0.001,
        'active': True,
        'level': 3
    },
    'flags': ['NOMINAL', 'SYNCED', 'LOCKED']
}

# Simulated raw sensor readings – actual input source
raw_readings = [12.4, 8.7, 15.2, 6.3, 9.8, 11.0, 13.5]

# Step 1: Filter out low values (<7) – relevant operation
filtered_readings = [x for x in raw_readings if x >= 7]

# Step 2: Apply preprocessing to each reading (core logic)
processed_metrics = []
for val in filtered_readings:
    processed = preprocess_metric(val)
    processed_metrics.append(processed)

# Fake diagnostic logger (side-effect decoy)
class DiagnosticLogger:
    def __init__(self):
        self.entries = []
    
    def log(self, msg):
        self.entries.append(f'[LOG] {msg}')

logger = DiagnosticLogger()
logger.log("System boot")
logger.log("Preprocessing complete")

# Phantom normalization (unused result)
normalized = [p / max(processed_metrics) for p in processed_metrics if max(processed_metrics) > 0]

# Real analysis function: computes weighted combinatoric score
# Uses both arithmetic and logical branching with list comprehension

def analyze_readings(metrics):
    n = len(metrics)
    if n == 0:
        return 0
    
    # Combinatoric weight: number of unique pairs
    pair_count = n * (n - 1) // 2 if n > 1 else 1
    
    # Statistical moment calculation (distraction)
    mean_val = sum(metrics) / n
    variance = sum((x - mean_val) ** 2 for x in metrics) / n
    
    # Primary decision logic – depends on thresholds
    high_count = len([m for m in metrics if m > 6.0])  # Always true
    mid_count = len([m for m in metrics if 4.0 <= m <= 6.0])
    
    # Actual formula: combines pair count and dominant metric
    dominant = max(metrics)
    
    # Red herring: complex trigonometric adjustment (neutralized)
    adjustment = math.cos(math.pi / (dominant + 1))
    adjusted_pairs = pair_count * (1 + adjustment * 0.1)
    
    # Final computation: uses only pair_count and dominant
    score = int(dominant * adjusted_pairs)
    
    # Key conditional that affects final output
    threshold_reference = 45
    if score > threshold_reference:
        score -= 5
    elif score == threshold_reference:
        score += 10
    else:
        score += 3
    
    return score

# Execution point of interest
final_diagnostic = analyze_readings(processed_metrics)

# Print target result
print(f"Target result: {final_diagnostic}")