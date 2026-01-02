import math

# Simulated sensor array data and system health monitoring logic
def preprocess_signal(raw_data, threshold=0.75):
    filtered = [x for x in raw_data if abs(x) > threshold]
    return [round(math.sin(x) * 1.2, 4) for x in filtered] if filtered else [0.0]


def calculate_entropy(values):
    total = 0.0
    for v in values:
        if v != 0:
            total -= v * math.log(abs(v))
    return round(total, 4)


def analyze_phase_shift(signal_stream):
    shift_sum = 0.0
    for i in range(1, len(signal_stream)):
        shift_sum += math.cos(signal_stream[i] - signal_stream[i-1])
    return shift_sum / len(signal_stream) if signal_stream else 0

# Irrelevant helper - decoy function (dead path)
def deprecated_normalization(vec):
    magnitude = sum(x**2 for x in vec) ** 0.5
    return [x / magnitude for x in vec] if magnitude else vec

# Unused transformation chain (distractor)
def apply_fourier_trend(data):
    transformed = []
    for k in range(len(data)):
        comp = 0.0
        for n, val in enumerate(data):
            comp += val * math.cos(2 * math.pi * k * n / len(data))
        transformed.append(comp)
    return transformed

# Core diagnostic engine
def detect_anomalies(metrics, sensitivity=0.9):
    anomalies = []
    baseline = sum(metrics) / len(metrics) if metrics else 0
    for i, m in enumerate(metrics):
        if abs(m - baseline) > (1 - sensitivity) * 2:
            anomalies.append(i)
    return anomalies if anomalies else [0]

def normalize_vector(v):
    norm = sum(x*x for x in v) ** 0.5
    return [x/norm for x in v] if norm > 0 else v

# Signal fusion with conditional weighting
def fuse_signals(primary, secondary, mode='adaptive'):
    if mode == 'strict':
        weight = 0.8
    elif mode == 'relaxed':
        weight = 0.4
    else:
        weight = 0.6 if sum(primary) > 0 else 0.3
    return [weight * p + (1-weight) * s for p, s in zip(primary, secondary)]

# Main processing pipeline
raw_sensor_data = [
    0.1, -1.8, 0.3, 2.1, 0.4, -1.9, 0.2, 2.3, 
    0.05, -2.2, 0.15, 2.0, 0.35, -1.7, 0.25
]

# Step 1: Preprocess raw signals (relevant)
cleaned_signal = preprocess_signal(raw_sensor_data)

# Step 2: Generate multiple derived metrics (some irrelevant)
signal_energy = sum(x**2 for x in cleaned_signal)
distorted_copy = [math.tanh(x * 1.5) for x in cleaned_signal]  # unused distractor
phase_characteristic = analyze_phase_shift(cleaned_signal)
entropy_metric = calculate_entropy(cleaned_signal)

# Decoy analysis branch (never called)
def evaluate_resonance_pattern(seq):
    resonance_score = 0
    for i in range(2, len(seq)):
        if seq[i] * seq[i-1] < 0 and abs(seq[i] - seq[i-2]) > 0.5:
            resonance_score += 1.0
    return resonance_score

# System flags from hypothetical modules (simulated)
system_flags = {
    'overload': False,
    'sync_loss': True,
    'calibration_drift': True,
    'buffer_overflow': False
}

# Weight adjustment based on system state (has impact)
base_weight = 0.5
if system_flags['sync_loss'] and not system_flags['overload']:
    base_weight += 0.2
if system_flags['calibration_drift']:
    base_weight -= 0.1

adjusted_weight = max(0.1, min(0.9, base_weight))

# Generate secondary synthetic signal (used later)
synthetic_reference = [math.cos(i * 0.4) * 0.7 for i in range(len(cleaned_signal))]

# Apply fusion using adaptive mode (relevant)
fused_output = fuse_signals(cleaned_signal, synthetic_reference, mode='adaptive')

# Normalize fused result (relevant)
normalized_signals = normalize_vector(fused_output)

# Auxiliary metric collection (partial use)
aggregated_diagnostics = [
    signal_energy,
    phase_characteristic,
    entropy_metric,
    sum(normalized_signals),
    len(detect_anomalies(normalized_signals, sensitivity=0.85))
]

# Red herring computation (looks important, unused)
theoretical_capacity = 0.0
for i in range(1, 6):
    term = (-1)**i * (0.5 ** (i+1)) / math.factorial(i)
    theoretical_capacity += term

# Final aggregation logic (critical path)
def aggregate_metrics(norm_sig, flags):
    temp_state = [x * 1.3 for x in norm_sig]
    
    # Conditional masking
    mask = 1.0
    if flags['sync_loss']:
        mask *= 0.7
    if flags['calibration_drift']:
        mask *= 0.8
    
    masked_state = [x * mask for x in temp_state]
    
    # Accumulation with decay
    accumulator = 0.0
    decay = 0.95
    for val in masked_state:
        accumulator = accumulator * decay + val * (1 - decay)
    
    # Final adjustment based on list comprehension filtered count
    significant_components = [x for x in normalized_signals if abs(x) > 0.1]
    adjustment_factor = len(significant_components) * 0.05
    
    return round(accumulator + adjustment_factor, 4)

# Execute final statement
final_diagnostic = aggregate_metrics(normalized_signals, system_flags)
print(f"Target result: {final_diagnostic}")