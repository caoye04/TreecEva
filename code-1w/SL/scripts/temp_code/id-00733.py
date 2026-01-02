import math

# Irrelevant helper function (dead code path)
def legacy_calculate(x):
    return (x ** 2 + 3 * x + 1) % 100

# Unused mathematical constant
euler_correction = math.exp(1) * 0.57721

# Distractor variables
temp_buffer = [0] * 100
rolling_sum = 0
offset_hint = 23

# Core processing components
def bitwise_transform(value, key):
    return (value ^ key) & 0xFF

def normalize_signal(x):
    return max(-1.0, min(1.0, x / 100.0))

# Lambda for dynamic threshold filtering
threshold_filter = lambda readings, t: [r for r in readings if abs(r) > t]

# Simulated sensor data with embedded pattern
data_stream = [
    42, 88, -15, 67, 23, 91, 7, 55,  
    104, 39, 72, 29, 83, 18, 66, 5
]

# Misleading transformation chain (partially unused)
transformed_cache = []
for val in data_stream:
    step1 = bitwise_transform(val, offset_hint)
    step2 = (step1 + 17) % 256
    step3 = int(math.sqrt(step2) * 3)
    transformed_cache.append(step3)

# Decoy accumulator
shadow_accumulator = 0
for x in transformed_cache:
    shadow_accumulator += x ^ 0xAA

# Real processing pipeline
def decode_sequence(seq):
    result = 0
    for i, v in enumerate(seq):
        if i % 3 == 0:
            result += v * (i + 1)
    return result

def encrypt_payload(payload, seed):
    # Heavily distractive bit manipulation
    masked = 0
    for shift in range(8):
        masked |= ((seed >> shift) & 1) << (7 - shift)
    return (payload ^ masked) & 0xFFFF

# Orchestration function
def process_pipeline(signal):
    # Step 1: Filter relevant components
    filtered = threshold_filter(signal, 20)
    
    # Step 2: Apply arithmetic modulation
    modulated = []
    for idx, val in enumerate(filtered):
        mod_val = val
        if idx % 2 == 0:
            mod_val = int(mod_val * 1.5)
        else:
            mod_val = int(mod_val * 0.8)
        modulated.append(abs(mod_val))
    
    # Step 3: Accumulate with conditional skip
    accumulation = 0
    for num in modulated:
        if num == 0:
            continue
        log_component = int(math.log(num + 1, 2))
        accumulation += log_component
    
    # Step 4: Decode using index-weighted sum
    decoded_value = decode_sequence(modulated)
    
    # Step 5: Final transformation (only this output matters)
    final_raw = accumulation ^ decoded_value
    final_encrypted = encrypt_payload(final_raw, 42)
    
    # Critical assignment point
    final_output = final_encrypted - 100
    
    # Red herring: irrelevant normalization
    normalized_output = normalize_signal(final_output)
    
    return final_output

# Execution
final_output = process_pipeline(data_stream)
print(f"Target result: {final_output}")