import math

def analyze_phase_shift(signal):
    # Irrelevant complex signal processing (red herring)
    fft_components = [math.sin(x / 3.0) + math.cos(x * 2.1) for x in range(10)]
    magnitude = sum([abs(c) for c in fft_components])
    return magnitude * 0.75

def validate_checksum(data):
    # Unused validation function (dead code path)
    checksum = 0
    for d in data:
        checksum ^= d % 256
    return checksum == 42

def transform_sequence(seq):
    # Distractor transformation with partial relevance
    shifted = [(x << 1) ^ 0xA5 for x in seq]
    filtered = [x for x in shifted if x > 100]
    return [x % 89 for x in filtered]

def compute_entropy(values):
    # Seemingly important but ultimately unused metric
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    return -sum(p * math.log(p) for p in probs if p > 0)

def evaluate_stability(readings):
    # Complex but partially irrelevant stability logic
    trend = sum(readings[i+1] - readings[i] for i in range(len(readings)-1))
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings)
    return abs(trend) < 5 and variance < 200

def process_metrics(signature, threshold):
    # Core logic buried within distractions
    a = signature[0] ^ signature[3]
    b = (signature[1] + signature[2]) >> 2
    temp_val = (a * 3) + (b // 2)
    
    # Conditional expression with meaningful outcome
    adjustment = 17 if temp_val > threshold else 9
    
    # List comprehension that filters relevant diagnostic codes
    codes = [i * 2 + adjustment for i in range(7) if (i + temp_val) % 3 == 0]
    
    # Set operations to obscure key calculation
    unique_codes = set(codes)
    modifiers = {x + 5 for x in unique_codes if x % 2 == 1}
    final_set = unique_codes | modifiers  # Union adds distraction
    
    # Key computation hidden among noise
    base_score = sum(final_set) // len(final_set)
    
    # Secondary check that looks important but doesn't affect result
    consistency = all(base_score % i == 0 for i in range(2, 5))
    
    # Final adjustment using integer division and rounding
    scaling_factor = 3 if consistency else 5
    intermediate = (base_score * scaling_factor + 4) // 5
    
    # The real answer is computed here
    final_diagnostic = int(round(intermediate * 1.25))
    
    # Dead assignment - no effect
    final_diagnostic += 0  # No-op to mislead
    
    return final_diagnostic

# Main execution block with mixed signals
if __name__ == '__main__':
    # Real input data
    sensor_flux = [12, 19, 25, 34]
    config_mode = 'diagnostic'
    
    # Heavily distracting initializations
    calibration_data = [i**2 % 191 for i in range(15)]
    health_signature = [
        sensor_flux[0] ^ 0x5A,
        sensor_flux[1] + 7,
        sensor_flux[2] * 2,
        sensor_flux[3] ^ 0x3C
    ]
    
    # Looks like normalization but actually modifies inputs meaningfully
    normalized = [max(1, int(x * 0.95)) for x in health_signature]
    health_signature = normalized  # Update with slightly modified values
    
    # Irrelevant string processing (distraction)
    status_tags = "sys:ok mode:deep_scan variant:alpha".split()
    flags = {tag.split(':')[0]: tag.split(':')[1] for tag in status_tags}
    
    # Unused nested structure
    diagnostics_tree = {
        'level1': {
            'sublevel': [
                {'metric': 'phase', 'value': analyze_phase_shift(list(range(8)))},
                {'metric': 'entropy', 'value': compute_entropy(calibration_data)}
            ],
            'valid': evaluate_stability(calibration_data[:8])
        }
    }
    
    # Actual threshold used in main logic
    baseline_threshold = 40
    
    # Key statement - target of the question
    final_diagnostic = process_metrics(health_signature, baseline_threshold)
    
    # Print required output
    print(f"Result: {final_diagnostic}")