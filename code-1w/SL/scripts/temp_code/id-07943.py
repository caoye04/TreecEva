import math

# Simulated sensor data processing with diagnostic evaluation
def collect_samples():
    raw_signals = [0.8, -1.2, 3.5, 2.1, -0.4, 4.4, 1.9, -2.3]
    baseline_offset = 1.1
    adjusted = [sig + baseline_offset for sig in raw_signals]
    return adjusted

# Irrelevant auxiliary function (distractor)
def compute_entropy(data):
    entropy = 0.0
    for x in data:
        if x > 0:
            entropy -= x * math.log(x)
    return round(entropy, 4)

# Data filtering with red herring transformations
def filter_noise(signal_list):
    filtered = []
    threshold = 1.5
    suppression_factor = 0.8
    temp_stats = {'count': 0, 'sum_sq': 0}  # Unused tracking (distractor)

    for val in signal_list:
        temp_stats['count'] += 1
        temp_stats['sum_sq'] += val ** 2
        if abs(val) >= threshold:
            processed_val = val * suppression_factor if val < 0 else val
            filtered.append(round(processed_val, 3))
    # Dead code path (never executed due to logic above)
    if len(filtered) > 100:
        normalized = [x / max(filtered) for x in filtered]
        return normalized
    return filtered

# Misleading transformation chain (partially used)
def apply_envelope(signal):
    enveloped = []
    phase_accumulator = 0.0
    frequency_mod = 0.3

    for i, s in enumerate(signal):
        carrier = math.sin(phase_accumulator)
        modulated = s * carrier
        enveloped.append(round(modulated, 3))
        phase_accumulator += frequency_mod + (i % 3) * 0.05

    # This block is unreachable (red herring control flow)
    if False:
        reversed_env = enveloped[::-1]
        return [abs(x) for x in reversed_env]

    return enveloped

# Core analysis with subtle conditional logic
def evaluate_coherence(data):
    if not data:
        return 0.0
    squared_sum = sum(x ** 2 for x in data)
    linear_sum = sum(data)
    n = len(data)
    mean_val = linear_sum / n
    variance = sum((x - mean_val) ** 2 for x in data) / n
    if variance == 0:
        return 0.0
    # Composite metric combining energy and stability
    energy_factor = math.sqrt(squared_sum) / n
    stability_ratio = abs(mean_val) / (math.sqrt(variance) + 1e-6)
    return round(energy_factor * stability_ratio, 4)

# Decoy function using string methods (irrelevant to final result)
def generate_report_code(timestamp_str):
    code_base = "DRX-"
    clean_ts = timestamp_str.replace(':', '').replace('-', '')
    checksum = sum(ord(c) for c in clean_ts) % 97
    report_id = f"{code_base}{checksum}-{clean_ts[-6:]}.rep"
    return report_id.upper().strip()  # String method chain (distractor)

# Main processing pipeline
processed_data = []
def main_pipeline():
    global processed_data
    samples = collect_samples()
    
    # Apply noise filter (relevant)
    cleaned = filter_noise(samples)
    
    # Apply envelope modulation (relevant only for non-negative values)
    modulated = apply_envelope(cleaned)
    
    # Extract positive components for diagnostic focus
    positive_components = [x for x in modulated if x > 0]  # List comprehension
    
    # Simulate hardware gain stage (misleading intermediate)
    amplified = [val * 1.75 for val in positive_components]
    clipped = [min(x, 3.0) for x in amplified]  # Not actually used later
    
    # Final relevant transformation
    processed_data = [round(math.cos(x), 3) for x in positive_components]

# Diagnostic engine with tuple unpacking and branching
def analyze_signal(readings):
    if len(readings) == 0:
        return -1.0
    
    # Tuple unpacking and destructuring (required concept)
    first, *middle, last = readings if len(readings) > 2 else (readings[0],) + (0,) * (len(readings) == 1) + (readings[-1],)
    
    # Compute multiple candidate metrics (only one used)
    avg = sum(readings) / len(readings)
    peak = max(readings)
    coherence_score = evaluate_coherence(readings)
    
    # Conditional logic with red herring branches
    adjustment = 0.0
    if first > 0.5:
        adjustment += 0.1
        if peak < 0.8:
            adjustment *= 0.5
    elif len(middle) > 3:
        adjustment -= 0.05
    else:
        temp_var = first * last  # Computed but unused
        adjustment = round(math.tanh(temp_var), 3)

    # Final decision based on hidden rule (non-obvious)
    if abs(avg) > 0.3 and coherence_score > 0.4:
        result = coherence_score * 1000
    elif peak > 0.9:
        result = peak * 500
    else:
        result = avg * 200
    
    # Bit manipulation decoy (no effect)
    binary_tag = 0b1010 ^ 0b1100 & 0b1111
    tag_shift = binary_tag << 2
    
    return int(round(result))

# Execute main workflow
main_pipeline()

# Key statement: what is the value of final_diagnostic after this?
final_diagnostic = analyze_signal(processed_data)
print(f"Target result: {final_diagnostic}")