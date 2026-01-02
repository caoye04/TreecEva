from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and metadata
data_packet = [
    {'id': 'A7', 'readings': [1.2, 3.4, -2.1, 5.6], 'active': True, 'mode': 'diag'},
    {'id': 'B3', 'readings': [0.0, -1.1, 4.4, 2.3], 'active': False, 'mode': 'norm'},
    {'id': 'C9', 'readings': [2.2, 1.8, 3.3, 4.7], 'active': True, 'mode': 'diag'},
    {'id': 'D2', 'readings': [-0.5, 0.5, 1.0, -1.0], 'active': True, 'mode': 'calib'}
]

# Irrelevant calibration map (distractor)
calibration_map = defaultdict(lambda: 0.95)
for i in range(10):
    calibration_map[i] = round(math.sin(i) * 0.1, 2)

# Misleading preprocessing step (partially unused)
def legacy_normalize(vec):
    norm = sum(abs(x) for x in vec) or 1
    return [round(x / norm * 100, 1) for x in vec]

# Auxiliary function that looks important but is only used once
def detect_spikes(readings, threshold=3.0):
    return len([r for r in readings if abs(r) > threshold])

# Core transformation pipeline
preprocessed = []
spike_count = 0
total_energy = 0.0

for packet in data_packet:
    if not packet['active']:
        continue
    raw = packet['readings']
    
    # Real processing begins
    filtered = [x for x in raw if x >= -1.5]  # Remove extreme negatives
    energy = sum(x**2 for x in filtered)
    total_energy += energy
    
    # Distractor: spike detection on unfiltered data (unused result)
    _ = detect_spikes(raw)
    
    # Another distractor: frequency analysis on indices
    freq_analysis = Counter([int(abs(x)) % 4 for x in filtered])
    dominant_freq = max(freq_analysis, key=freq_analysis.get)
    
    # Meaningful transformation
    transformed = [math.log(abs(x) + 1) * (1 + dominant_freq) for x in filtered]
    preprocessed.append({
        'src_id': packet['id'],
        'values': transformed,
        'energy': energy,
        'flag': packet['mode'] == 'diag'
    })

# Dead code path - never executed due to logic above
orphaned_data = []
for x in range(5):
    orphaned_data.append({'temp': x * 0.1, 'status': 'orphan'})

# Simulate historical baseline (irrelevant)
historical_baseline = list(map(lambda x: round(math.exp(-x/10), 2), range(5)))

# Actual signal processor: combines multiple concepts
processed_data = []
buffer_shift = 1.5

for entry in preprocessed:
    shifted_vals = [v + buffer_shift for v in entry['values']]
    capped_vals = [min(v, 3.0) for v in shifted_vals]  # Cap at 3.0
    entropy = 0.0
    for v in capped_vals:
        if v > 0:
            entropy -= v * math.log(v) if v > 1e-5 else 0
    
    # Include auxiliary metrics (some irrelevant)
    metrics = {
        'entropy': round(entropy, 3),
        'magnitude': sum(capped_vals),
        'peak': max(capped_vals),
        'count': len(capped_vals),
        'diagnostic_weight': entry['energy'] * (2 if entry['flag'] else 1)
    }
    processed_data.append(metrics)

# Fake fusion algorithm (looks complex but unused output)
def fuse_signals(data_list):
    fused = defaultdict(float)
    for i, d in enumerate(data_list):
        fused['score'] += d['magnitude'] * (0.8 ** i)
        fused['complexity'] += d['entropy']
    return dict(fused)

_ = fuse_signals(processed_data)  # Result ignored

# Critical analysis function
def analyze_signal(signal_list):
    base = 0
    adjustment = 0.0
    
    for sig in signal_list:
        # Key computation branch
        if sig['diagnostic_weight'] > 15:  # Only C9 and A7 meet this
            base += int(sig['peak'] * 10)
            adjustment += sig['entropy'] * sig['count']
    
    # Secondary influence
    valid_count = sum(1 for s in signal_list if s['diagnostic_weight'] > 10)
    
    # Final formula: deterministic but obscured by distractions
    result = base * valid_count + round(adjustment)
    
    # Red herring: XOR with hash of string (constant)
    fake_key = 0
    for c in 'security_override':
        fake_key ^= ord(c)
    
    # Final answer is NOT affected by fake_key (misleading)
    final_value = result  # No XOR applied
    
    return int(final_value)

# Execution point of interest
final_diagnostic = analyze_signal(processed_data)
print(f"Target result: {final_diagnostic}")