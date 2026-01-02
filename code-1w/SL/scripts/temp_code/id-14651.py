import math

# Simulated sensor data processing with red herrings and distractions
def preprocess_signal(raw):    
    filtered = [x for x in raw if x > -50]  # Irrelevant filtering
    normalized = [abs(val) ** 0.5 for val in filtered]  # Distractor computation
    return [val * 1.05 for val in raw]  # Only this line matters

# Dead function - never called but looks important
def legacy_calibrate(x):
    return (x + 32) * 5 / 9

# Decoy transformation chain
def encrypt_sequence(seq):
    encrypted = []
    for i, s in enumerate(seq):
        if isinstance(s, str):
            shifted = ''.join(chr((ord(c) - ord('a') + i) % 26 + ord('a')) for c in s)
            encrypted.append(shifted)
    return encrypted

# Real transformation logic hidden among noise
def transform_readings(data_str, key=3):
    parts = data_str.split(',')
    values = [float(p.strip()) for p in parts]
    adjusted = [v * key + 1 for v in values]
    squared_offsets = [math.sin(x) ** 2 + math.cos(x) ** 2 for x in adjusted]  # Always 1.0 - red herring
    return [a * 2 for a in adjusted]  # Actual meaningful output

# Auxiliary function with misleading intermediate results
def compute_entropy(arr):
    total = sum(arr)
    if total == 0:
        return 0
    probs = [x / total for x in arr]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 3)

# Core analysis logic buried in complexity
def analyze_pattern(signal, limit):
    magnitude = sum(abs(x) for x in signal)
    if magnitude < limit:
        category = 'LOW'
    elif magnitude < limit * 3:
        category = 'MEDIUM'
    else:
        category = 'HIGH'
    
    # Critical branching based on string property
    tag = 'SYS_OK' if len(category) % 2 == 1 else 'SYS_FAIL'
    
    # Multiple layers of conditional expressions
    base_score = magnitude if tag == 'SYS_OK' else magnitude / 2
    adjustment = 10 if 'M' in category else (-5 if base_score > 100 else 0)
    final_score = base_score + adjustment
    
    # Final decision path
    diagnostic_code = 404 if 'FAIL' in tag else (200 if final_score > 80 else 100)
    
    # This is the actual answer variable
    final_diagnostic = int(final_score) if diagnostic_code == 200 else diagnostic_code
    
    return final_diagnostic

# Irrelevant global constants
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
ACTIVE_MODULES = ['sensor', 'network', 'storage']

# Unused data structures
lookup_table = {i: chr(ord('A') + i % 26) for i in range(50)}
shadow_stack = []

# Main execution flow
if __name__ == '__main__':
    raw_sensor_input = "12.0, 8.5, 15.2, 7.3, 9.8"
    
    # Distraction: multiple preprocessing steps
    cleaned = preprocess_signal([10, -60, 20, -80, 30])  # Unused result
    temp_buffer = [x * 0.1 for x in range(100)]  # Dead code path
    
    # Key data transformation
    transformed_data = transform_readings(raw_sensor_input, key=3)
    
    # More distractions
    dummy_text = "encrypt,decode,verify"
    tokens = dummy_text.upper().replace(',', '|').split('|')
    processed_tokens = [t[::-1] for t in tokens if len(t) > 4]  # Meaningless
    
    # Entropy calculation on wrong data
    fake_entropy = compute_entropy([1, 2, 3, 4])
    
    # Threshold determined via string logic
    threshold_str = 'dynamic_limit'
    threshold = sum(ord(c) for c in threshold_str) % 100  # Evaluates to 97
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Output result
    print(f"Result: {final_diagnostic}")