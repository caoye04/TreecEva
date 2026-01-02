import math

# Simulated sensor data and configuration
def generate_signals():
    base = [i * 0.5 for i in range(20)]
    noise = [0.1 * (i % 3) for i in range(20)]
    return [b + n for b, n in zip(base, noise)]

def filter_outliers(data, limit=5):
    # Irrelevant filtering function (dead code path)
    return [x for x in data if x < limit]

def deprecated_transform(x):
    # Unused transformation (distractor)
    return x ** 2 + 2 * x + 1

def compute_entropy(values):
    # Misleading intermediate calculation (red herring)
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

# Core processing pipeline
raw_data = generate_signals()

# Apply moving average smoothing
smoothed = []
for i in range(2, len(raw_data)):
    avg = (raw_data[i-2] + raw_data[i-1] + raw_data[i]) / 3
    smoothed.append(avg)

# Normalize data using min-max scaling
min_val, max_val = min(smoothed), max(smoothed)
normalized = [(x - min_val) / (max_val - min_val + 1e-8) for x in smoothed]

# Bitmask-based feature extraction (relevant but partially obscured)
feature_flags = 0
for x in normalized[:5]:
    if x > 0.5:
        feature_flags |= (1 << int(x * 10) % 8)

# Create diagnostic map with dummy entries (mix of relevant/irrelevant)
threshold_map = {
    'crit': 0.8,
    'warn': 0.6,
    'info': 0.3,
    'debug': 0.1,
    'spare1': 0.95,  # decoy
    'spare2': 0.05   # decoy
}

# Auxiliary state tracking (mostly irrelevant)
current_mode = 'ACTIVE'
heartbeat_counter = 17
last_sync = (2023, 12, 25)

# Signal classification engine
is_critical = lambda val, thresh: val >= thresh
is_elevated = lambda val, low, high: low <= val < high

# Data categorization with conditional expression
processed_data = []
for val in normalized:
    category = (
        'CRIT' if is_critical(val, threshold_map['crit']) else
        'WARN' if is_elevated(val, threshold_map['warn'], threshold_map['crit']) else
        'NORMAL' if is_elevated(val, threshold_map['info'], threshold_map['warn']) else
        'LOW'
    )
    processed_data.append({'value': val, 'class': category})

# Secondary analysis (looks important but unused)
def analyze_trend(data):
    diffs = [data[i+1]['value'] - data[i]['value'] for i in range(len(data)-1)]
    return sum(1 for d in diffs if d > 0)

trend_score = analyze_trend(processed_data)  # red herring

# Final diagnostic engine (key computation)
def evaluate_stability(flag, dataset):
    active_bits = bin(flag).count('1')
    high_count = sum(1 for d in dataset if d['class'] == 'CRIT')
    medium_count = sum(1 for d in dataset if d['class'] == 'WARN')
    return active_bits * 100 - high_count * 50 + medium_count * 10

def analyze_signal(data, config):
    # Key logic with distractors
    base_score = evaluate_stability(feature_flags, data)
    
    # Decoy adjustment (never applied due to condition)
    adjustment = 0
    system_load = 0.7
    if system_load > 0.9:  # False, so ignored
        adjustment = -25
    
    # Conditional override attempt (fails guard clause)
    override_enable = len([d for d in data if d['class'] == 'LOW']) > 30
    if override_enable:
        return -999  # dead path
        
    # Final computation
    entropy_proxy = compute_entropy([d['value'] for d in data]) * 10
    final_score = base_score + int(entropy_proxy)
    
    # Mask result with bitwise operation (actual answer path)
    mask = 0xFF
    final_score &= mask  # restrict to 8 bits
    
    return final_score

# Execute main logic
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")