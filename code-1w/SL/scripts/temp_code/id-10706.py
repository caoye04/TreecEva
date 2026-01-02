def analyze_readings(data):
    # Irrelevant signal processing
    filtered = [x for x in data if x > 0]
    baseline = sum(filtered) / len(filtered)
    adjusted = [abs(x - baseline) * 1.5 for x in filtered]
    return [a for a in adjusted if a < 100]

# Distractor: Unused function
def deprecated_calibrate(x):
    return (x + 32) * 5/9

# Real processing chain starts here
def generate_sequence(seed):
    seq = []
    a, b = 1, seed % 7
    for _ in range(6):
        seq.append(a)
        a, b = b, (a + b) % 13
    return seq

def compute_weights(values):
    # Uses slicing and lambda
    rev = values[::-1]
    weight_fn = lambda x: x ** 0.5 if x > 0 else 0
    return [weight_fn(r) for r in rev]

def validate_entry(record):
    # String method distraction
    if isinstance(record, str):
        parts = record.strip().split(',')
        return len(parts) == 4
    return False

# Core logic with multiple concepts
def process_metrics(sequence, config):
    temp_result = 0
    scale_factor = config['factor']
    
    # Bit manipulation red herring
    mask = 0b1111
    masked_values = [v & mask for v in sequence]
    
    # Actual relevant path
    for i in range(len(sequence)):
        if i % 2 == 0:
            temp_result += sequence[i] * scale_factor
        else:
            temp_result -= int(sequence[i] / config['divisor'])
    
    # Decoy conditional branch
    if temp_result > 1000:
        temp_result = temp_result >> 2
    
    # Another irrelevant transformation
    checksum = 0
    for c in str(temp_result):
        if c.isdigit():
            checksum += int(c)
    
    # Final adjustment using lambda and slicing
    history = [temp_result, checksum, temp_result % 19]
    modifier = list(map(lambda x: (x + 1) // 2, history[1:]))
    
    final_value = history[0] + modifier[0] * modifier[1]
    
    return final_value

# Main execution with distractions
import math

# Fake sensor array (unused)
raw_signals = [-5, 0, 12, 45, None, 23]
sanitized = [r for r in raw_signals if r is not None and r >= 0]

# Real input generation
seed_value = 29
health_sequence = generate_sequence(seed_value)

# Configuration map with misleading keys
threshold_map = {
    'threshold': 4.7,
    'grace_period': 300,
    'factor': 7,
    'divisor': 3,
    'retry_limit': 5
}

intermediate_scores = compute_weights(health_sequence)

# Unused diagnostic flag
diagnostic_mode_enabled = False

# Key computation
final_diagnostic = process_metrics(health_sequence, threshold_map)

# Output required result
print(f"Result: {final_diagnostic}")