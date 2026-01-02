import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [0.8, 1.2, -0.4, 0.9, 1.1, -1.3, 0.7, 0.5]
    scale_factor = 1.75
    adjusted = [round(x * scale_factor, 3) for x in raw_samples]
    return adjusted

# Irrelevant helper: spectral baseline correction (unused)
def correct_baseline(signal):
    mean_val = sum(signal) / len(signal)
    return [x - mean_val for x in signal]

# Redundant transformation chain
def transform_domain(data):
    transformed = []
    for x in data:
        if x > 0:
            transformed.append(math.log(abs(x) + 1) * 2.1)
        else:
            transformed.append(-math.exp(abs(x) / 3))
    return transformed

# Decoy analysis function that looks important but isn't used
def compute_entropy(seq):
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Core data processing with key logic buried
def filter_outliers(signal, threshold=1.1):
    filtered = []
    deviation_log = []
    base_ref = sum(signal) / len(signal)
    for val in signal:
        dev = abs(val - base_ref)
        deviation_log.append(round(dev, 3))
        if dev <= threshold:
            filtered.append(val)
    # Distractor: unused deviation profile
    avg_dev = sum(deviation_log) / len(deviation_log)
    return filtered

# Data enhancement with string-based tagging (uses string method)
def tag_segments(data_list):
    tags = []
    for i, block in enumerate([data_list[i:i+2] for i in range(0, len(data_list), 2)]):
        magnitude = sum(abs(x) for x in block)
        label = "LOW" if magnitude < 1.5 else "HIGH"
        timestamp = f"SEG{i:02d}-XZ"
        tags.append(timestamp + ":" + label.lower())
    return tags  # Not used beyond here

# Critical diagnostic engine
def generate_signature(sequence):
    sig_value = 0
    for i, x in enumerate(sequence):
        sig_value += x * math.sin(i * 0.5) * 1.3
    return round(sig_value, 4)

# Dictionary-based state tracker (uses dict op)
def update_state(current, new_val, mode='diagnostic'):
    current['readings'].append(new_val)
    if mode == 'diagnostic':
        current['flags'].add('D6')
    return current

# Main pipeline with multiple distractions
def analyze_signal(data_package):
    # Setup diagnostic context
    context = {
        'readings': [],
        'flags': set(['INIT', 'SYNC']),
        'version': '2.1a'
    }
    
    # Apply several irrelevant transformations
    shifted_data = [x + 0.01 for x in data_package if x != 0]
    normalized = [x / 1.1 for x in shifted_data]
    
    # String-based metadata generation (distraction)
    meta_tags = tag_segments(normalized)
    tag_summary = ''.join(tag.split(':')[1].upper() for tag in meta_tags)
    
    # Real work begins: filtering and signature gen
    clean_signal = filter_outliers(data_package, threshold=1.05)
    
    # Conditional expression determining path (uses conditional expr)
    primary_input = clean_signal if len(clean_signal) > 4 else data_package
    
    # Compute signature - this is critical
    raw_signature = generate_signature(primary_input)
    
    # Update state (side effect, minor relevance)
    context = update_state(context, raw_signature, mode='diagnostic')
    
    # Dead code path: entropy not used
    # entropy_score = compute_entropy([round(x) for x in primary_input])
    
    # Final computation buried in noise
    adjustment = len(meta_tags) * 0.02
    final_diagnostic = raw_signature - adjustment
    
    # More red herrings
    temp_result = math.cos(final_diagnostic) * 1000
    debug_flag = 'TRACE_ENABLED' if temp_result > 500 else 'NONE'
    
    return final_diagnostic

# Execution flow
if __name__ == "__main__":
    samples = collect_readings()
    processed_data = transform_domain(samples)  # Looks important, but not directly used in final logic
    processed_data = filter_outliers(processed_data, 0.9)  # Intermediate overwrite
    final_diagnostic = analyze_signal(processed_data)
    print(f"Result: {final_diagnostic}")