from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_streams = [
    [142, 138, 141, 144, 139, 143, 140],
    [255, 251, 253, 256, 252, 254, 250],
    [98, 95, 99, 97, 96, 100, 94],
    [310, 308, 312, 309, 311, 307, 313]
]

# Irrelevant baseline references (distractor)
baseline_profiles = {
    'A': [1.0, 0.8, 1.2],
    'B': [0.9, 1.1, 0.85],
    'C': [1.05, 0.95, 1.0]
}

# System health thresholds (used later)
system_thresholds = {
    'critical': 250,
    'warning': 200,
    'stable': 150
}

# Noise filter parameters (mostly unused - red herring)
filter_config = {
    'window_size': 3,
    'attenuation': 0.95,
    'iterations': 5
}

# Decoy function - looks important but not used in main logic
def apply_noise_reduction(signal):
    smoothed = []
    for i in range(len(signal)):
        neighbors = signal[max(0, i-1):min(len(signal), i+2)]
        smoothed.append(sum(neighbors) / len(neighbors))
    return [int(x * 0.98) for x in smoothed]

# Auxiliary transformation (partially relevant)
def normalize_stream(stream):
    mean_val = sum(stream) / len(stream)
    return [int(math.sqrt(abs(x - mean_val + 1))) for x in stream]

# Diagnostic processor with multiple pathways
def analyze_pattern(sequence):
    counts = defaultdict(int)
    for i, val in enumerate(sequence):
        if val > 100:
            counts['high'] += 1
        elif val > 50:
            counts['medium'] += 1
        else:
            counts['low'] += 1
    
    # Complex conditional scoring (some branches irrelevant)
    score = 0
    if counts['high'] >= 3:
        score += 10
    if counts['medium'] in (2, 3):
        score += 5
    if len(sequence) % 2 == 1:
        score += 2
    
    # Unused scoring branch (dead code path)
    if False:  # Simulates deprecated logic
        for k, v in counts.items():
            score += len(k) // v if v else 0
    
    return score

# Core processing with distractors
def process_metrics(data_blocks, thresholds):
    diagnostics = []
    
    # Real processing begins here
    for idx, block in enumerate(data_blocks):
        # Normalize each telemetry block
        processed_block = normalize_stream(block)
        
        # Compute summary stats (some are decoys)
        block_max = max(processed_block)
        block_min = min(processed_block)
        block_range = block_max - block_min
        block_avg = sum(processed_block) / len(processed_block)
        
        # Irrelevant transformation chain
        temp_adjustments = []
        for val in processed_block:
            adjusted = val
            if adjusted > 15:
                adjusted = (adjusted >> 2) ^ 3  # Bit manipulation red herring
            temp_adjustments.append(adjusted * 1.05)
        
        # Actual decision logic embedded in noise
        severity_level = 'stable'
        if block_max > thresholds['critical']:
            severity_level = 'critical'
        elif block_max > thresholds['warning']:
            severity_level = 'warning'
        
        # Analyze pattern using secondary metric
        pattern_score = analyze_pattern(processed_block)
        
        # Combine metrics (only some contribute)
        base_risk = 0
        if severity_level == 'critical':
            base_risk = 100
        elif severity_level == 'warning':
            base_risk = 50
        else:
            base_risk = 10
        
        # Final diagnostic calculation - only this matters
        final_risk = base_risk + (pattern_score * 2)  # Key formula
        diagnostics.append(final_risk)
    
    # Aggregate result
    aggregate_diagnostic = sum(diagnostics) // len(diagnostics)
    
    # Distractor: complex set operation with no impact
    unique_values = set()
    for d in data_blocks:
        unique_values.update(d)
    rare_values = {x for x in unique_values if Counter(unique_values)[x] == 1}
    adjustment_factor = len(rare_values) % 7
    
    # This variable is never used (misleading)
    calibration_offset = adjustment_factor * 3.14
    
    # Critical: Final computation that determines answer
    final_diagnostic = aggregate_diagnostic + 17  # Offset applied at end
    return final_diagnostic

# Secondary unused analysis (heavy distraction)
def compute_spectral_signature(matrix):
    signature = []
    for row in matrix:
        transformed = []
        for i, val in enumerate(row):
            transformed.append(val ^ (i * 7) & 255)
        fft_sim = [sum(transformed[i::4]) for i in range(4)]
        signature.extend(fft_sim)
    return [s % 100 for s in signature]

# Prepare log data from telemetry
log_data = []
for series in telemetry_streams:
    shifted = [(x - 50) for x in series]  # Preprocessing step
    log_data.append(shifted)

# Main execution point
final_diagnostic = process_metrics(log_data, system_thresholds)

# Output result as required
print(f"Result: {final_diagnostic}")