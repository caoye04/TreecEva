import math

# Irrelevant helper function (decoy)
def compute_entropy(data):
    return sum(-x * math.log2(x) for x in data if x > 0)

# Unused transformation (dead code path)
def transform_legacy(signal):
    return [int(s ** 1.5) for s in signal if s % 2 == 0]

# Core signal processor with distractors
def preprocess_signal(raw_signal, noise_floor=0.1, gain=2.3):
    amplified = [gain * sample for sample in raw_signal]
    filtered = [sample for sample in amplified if abs(sample) > noise_floor]
    normalized = [sample / max(filtered) for sample in filtered]
    return normalized

# Bit manipulation red herring
def obfuscate_key(index, base=7):
    shifted = (index << 3) & 0xFF
    return shifted ^ (base * 5)

# Real processing function buried in noise
def extract_features(data_stream):
    features = {}
    features['peak'] = max(data_stream)
    features['trough'] = min(data_stream)
    features['midpoint'] = (features['peak'] + features['trough']) / 2
    # Distractor computation
    features['entropy_proxy'] = sum(math.sin(x) ** 2 for x in data_stream)
    return features

# Conditional logic with misleading branches
def classify_regime(value, mode='strict'):
    if mode == 'strict':
        if value > 0.8:
            return 'HIGH'
        elif value > 0.5:
            return 'MEDIUM'
        else:
            return 'LOW'
    else:
        # Dead branch (never reached)
        return 'UNKNOWN'

# Data restructuring with zip and enumerate (required Python feature)
def align_channels(primary, secondary):
    if len(primary) != len(secondary):
        padded_len = max(len(primary), len(secondary))
        primary += [0] * (padded_len - len(primary))
        secondary += [0] * (padded_len - len(secondary))
    
    aligned = []
    for i, (p, s) in enumerate(zip(primary, secondary)):
        aligned.append({
            'idx': i,
            'primary_val': p,
            'secondary_val': s,
            'combined': p * 0.7 + s * 0.3
        })
    return aligned

# Real work happens here — complex but focused
def generate_threshold_map(keys, base_offset=1.1):
    # Uses lambda and list comprehension (required features)
    mapper = lambda k: round(math.log(k + 2) * base_offset, 4)
    return {k: mapper(k) for k in keys}

# Main analysis with nested logic and distractors
def analyze_signal(data_blocks, thresholds):
    results = []
    for block in data_blocks:
        feat = extract_features(block)
        decision_key = feat['midpoint']
        regime = classify_regime(decision_key)
        
        # Real logic intermixed with irrelevant steps
        score = 0
        if regime == 'HIGH':
            score += 100
        elif regime == 'MEDIUM':
            score += 50
        else:
            score += 10
        
        # Decoy accumulation (never used)
        dummy_accumulator = 0
        for i in range(len(block)):
            dummy_accumulator += math.tanh(block[i])

        # Actual contribution
        adjustment = thresholds.get(len(block), 0.5)
        score = int(score * adjustment)
        results.append(score)
    
    # Final aggregation
    total_impact = sum(results)
    
    # Misleading final check (irrelevant)
    if total_impact > 1000:
        compliance_status = 'APPROVED'
    else:
        compliance_status = 'PENDING'
    
    # This is the actual answer variable
    final_diagnostic = total_impact + 13
    return final_diagnostic

# --- Execution begins ---

# Simulated sensor input (real data)
raw_input_signal = [0.12, 0.35, 0.08, 0.91, 0.67, 0.44, 0.21]

# Irrelevant key generation (distractor)
security_keys = [obfuscate_key(i) for i in range(5)]

# Real preprocessing
processed_signal = preprocess_signal(raw_input_signal)

# Feature extraction on processed data
signal_features = extract_features(processed_signal)

# Create multi-channel alignment (partly relevant)
channel_a = processed_signal[:4]
channel_b = [x * 0.5 for x in processed_signal[3:]]
aligned_frames = align_channels(channel_a, channel_b)

# Extract blocks for analysis
block_1 = [f['combined'] for f in aligned_frames if f['idx'] % 2 == 0]
block_2 = [f['primary_val'] for f in aligned_frames]
data_segments = [block_1, block_2]

# Generate real control map
config_indices = [3, 4, 5]
threshold_map = generate_threshold_map(config_indices, base_offset=1.8)

# Critical execution point
final_diagnostic = analyze_signal(data_segments, threshold_map)

print(f"Result: {final_diagnostic}")