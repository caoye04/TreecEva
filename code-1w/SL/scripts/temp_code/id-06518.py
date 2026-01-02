from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (distractor: not all used)
def collect_readings():
    readings = [1.2, 0.9, 1.4, 0.8, 1.1, 1.3, 0.7, 1.0]
    weights = [0.8, 1.1, 0.9, 1.2, 1.0, 0.85, 1.15, 0.95]
    weighted = [r * w for r, w in zip(readings, weights)]
    return weighted

# Irrelevant preprocessing chain
def normalize_signal(signal):
    max_val = max(signal)
    return [s / max_val for s in signal]

def apply_filter(data):
    return [x for x in data if x > 0.5]  # Redundant filtering

# Decoy function - looks important but unused
def compute_robustness_index(seq):
    count = 0
    for i in range(len(seq)):
        if seq[i] > 1.0:
            count += (i ^ 2) & 3  # Bitwise red herring
    return count * 0.77

# Core diagnostic logic
def generate_signature(raw):
    stats = defaultdict(float)
    stats['mean'] = sum(raw) / len(raw)
    stats['variance'] = sum((x - stats['mean'])**2 for x in raw) / len(raw)
    stats['peak'] = max(raw)
    stats['entropy'] = -sum(p * math.log(p) for p in Counter(raw).values() if p > 0) / len(raw)
    return stats

# Another decoy transformation
def augment_data(profile):
    enhanced = profile.copy()
    enhanced['synthetic_marker'] = (profile['mean'] ** 2) % 1.7
    enhanced['flag'] = profile['peak'] > 1.05
    return enhanced

# Main processing with conditional logic and distractors
def analyze_pattern(signature, ref):
    # Distractor variables
    temp_buffer = [0] * 5
    checksum = 0
    for i in range(len(temp_buffer)):
        checksum ^= int(ref['baseline'] * 100) + i  # Misleading computation

    # Relevant branching logic
    threshold = ref['threshold']
    deviation = abs(signature['mean'] - ref['target_mean'])
    quality = 100

    if deviation > threshold:
        quality -= 30
        if signature['variance'] > 0.05:
            quality -= 25
            if signature['peak'] < 1.0:
                quality -= 15
    elif signature['entropy'] < -0.4:
        quality -= 10
        
    # Dead code path (never reached due to logic above)
    if quality == 100 and signature.get('missing_key', 0) > 5:
        quality += 50  # Unreachable

    return quality

# Complex multi-step pipeline with hidden key logic
def process_metrics(sig, base):
    # Intermediate irrelevant transformations
    transformed = {k: v * 1.05 if isinstance(v, float) else v for k, v in sig.items()}
    
    # Conditional expression distraction
    mode_flag = 'strict' if base['mode'] == 'enhanced' else 'basic'
    adjustment = 1.1 if mode_flag == 'strict' else 1.0
    
    # Hidden core calculation: XOR of scaled mean and variance bits
    scaled_mean = int(abs(transformed['mean']) * 100)
    scaled_var = int(abs(transformed['variance']) * 1000)
    diagnostic_code = (scaled_mean ^ scaled_var) >> 2  # Key bit manipulation
    
    # Secondary influence from analyze_pattern (actual relevance)
    health_score = analyze_pattern(transformed, base)
    
    # Final composition with red herring arithmetic
    fake_component = (transformed['peak'] * 1000) % 7
    final_diagnostic = diagnostic_code + health_score - int(fake_component)
    
    # Never-executed branch (dead code)
    if False:
        final_diagnostic *= 2
        final_diagnostic += sum(int(x) for x in str(final_diagnostic))

    return final_diagnostic

# Orchestration with misleading setup
if __name__ == '__main__':
    # Real data source
    raw_input = collect_readings()
    processed = normalize_signal(raw_input)
    filtered = apply_filter(processed)
    
    # Unused complex structure
    decoy_map = defaultdict(lambda: 'N/A')
    decoy_map.update({f'key_{i}': i * 2 for i in range(10)})
    
    # Actual signature generation
    health_signature = generate_signature(filtered)
    
    # Baseline reference (mix of relevant and irrelevant fields)
    baseline_ref = {
        'baseline': 0.95,
        'threshold': 0.15,
        'target_mean': 1.0,
        'mode': 'basic',  # Triggers adjustment = 1.0
        'version': '2.1',
        'active': True
    }
    
    # Critical execution point
    final_diagnostic = process_metrics(health_signature, baseline_ref)
    
    # Output result
    print(f"Target result: {final_diagnostic}")