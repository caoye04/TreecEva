import math

# Simulated sensor data processing with embedded diagnostics
def collect_samples():
    raw_data = [i * 0.5 + math.sin(i / 3) for i in range(15)]
    calibration_offset = 2.718
    adjusted = [x + calibration_offset for x in raw_data]
    return adjusted

# Irrelevant helper - dead code path
# def deprecated_filter(x):
#     return [val for val in x if val > 3]

def transform(x):
    return x ** 0.5 if x >= 0 else 0

# Misleading intermediate transformation chain
temp_correction = 1.05
scaling_factor = 0.95
legacy_buffer = []
for i in range(10):
    legacy_buffer.append(temp_correction * scaling_factor * i)

# Real processing begins here
processed_samples = []
sample_weights = [0.1, 0.2, 0.4, 0.2, 0.1]

samples = collect_samples()

# Apply moving average smoothing (relevant)
for i in range(4, len(samples)):
    window = samples[i-4:i+1]
    smoothed = sum(w * v for w, v in zip(sample_weights, window))
    processed_samples.append(smoothed)

# Decoy statistical analysis (irrelevant)
mean_fake = sum(samples) / len(samples)
variance_fake = sum((x - mean_fake) ** 2 for x in samples) / len(samples)
entropy_fake = -sum(math.log(abs(x) + 1e-8) for x in samples[:5])

# Unused complex lambda web
validate_sample = lambda x: True if abs(x) > 1e-3 else False
refine = lambda f: lambda x: f(x) * 1.1
pipeline = refine(transform)

# Red herring: buffer overflow simulation (unused)
circular_buffer = [0] * 8
buffer_index = 0
for k in range(20):
    circular_buffer[buffer_index] = k * 0.1
    buffer_index = (buffer_index + 1) % 8

# Core diagnostic logic (critical path)
def compute_metric(a, b, idx):
    diff = abs(b - a)
    penalty = math.log(1 + idx)
    return diff - penalty if diff > penalty else 0

# Generate feature vector
features = []
for j in range(1, len(processed_samples)):
    metric_val = compute_metric(processed_samples[j-1], processed_samples[j], j)
    features.append(metric_val)

# Secondary transformation using lambda (relevant)
compress = lambda lst: sum(math.sqrt(x) for x in lst if x > 0)
feature_score = compress(features)

# Higher-level analysis
baseline = 5.5
adjustment_curve = [math.exp(-i * 0.2) for i in range(6)]
dynamic_weight = sum(adjustment_curve) / len(adjustment_curve)

# Auxiliary decoy function (never called)
def old_diagnostic(seq):
    total = 0
    for x in seq:
        if x % 2 == 0:
            total += x * 1.5
    return total // 2

# Another red herring: unused bit manipulation
flag_register = 0b101010
flag_register ^= 0b111100
flag_register &= ~0b001000
flag_value = bin(flag_register).count('1')

# Actual analysis function (uses lambda indirectly)
def analyze_signal(data):
    if not data:
        return 0.0
    
    # Critical nested logic
    magnitude = sum(abs(x) for x in data)
    normalized = magnitude / len(data)
    
    # Complex derived threshold
    threshold = math.sqrt(sum(x*x for x in data[:3])) / 3 if len(data) >= 3 else 1.0
    
    # Key conditional gate
    if normalized > threshold:
        growth_rate = (data[-1] - data[0]) / len(data)
        adjustment = (lambda x: math.tanh(x))(growth_rate * 0.1)
        base_metric = normalized * 100
        final_component = base_metric + (adjustment * 25)
    else:
        final_component = normalized * 80
    
    # Final computation
    stability_factor = math.cos(len(data) * 0.1)
    return final_component * stability_factor

# Execution point of interest
final_diagnostic = analyze_signal(processed_samples)
print(f"Target result: {final_diagnostic}")