import math

# Simulated sensor data processing with diagnostic validation
def collect_telemetry():
    raw_readings = [i * 0.7 + math.sin(i * 0.3) for i in range(50)]
    offset = 42
    scale_factor = 1.05
    calibrated = [(x + offset) * scale_factor for x in raw_readings]
    return calibrated

def apply_mask(signal, mask_type='xor'):
    # Irrelevant masking operation (not used in final path)
    masked = []
    key = 0b101010
    for i, val in enumerate(signal):
        int_val = int(abs(val * 10)) & 0xFF
        if mask_type == 'xor':
            int_val ^= key
        elif mask_type == 'and':
            int_val &= key
        masked.append(int_val * 0.1)
    return masked  # Dead end: this output is not used

def preprocess(data):
    # Filtering out negative values and normalizing
    cleaned = [x for x in data if x > 0]
    mean_val = sum(cleaned) / len(cleaned)
    normalized = [(x - mean_val) / mean_val for x in cleaned]
    
    # Distractor: complex but unused transformation chain
    shadow_buffer = [abs(x) ** 0.5 for x in normalized if x < 0.5]
    temp_set = {round(x, 2) for x in shadow_buffer}
    checksum = sum([hash(str(x)) % 100 for x in temp_set]) % 1000  # Unused
    
    # Actual relevant filtering
    filtered = [x for x in normalized if abs(x) < 1.5]
    return filtered

def encrypt_key(base, salt=17):
    # Misleading cryptographic-looking function
    rotated = ((base << 3) & 0xFF) | (base >> 5)
    return (rotated ^ salt) % 128

def decode_signature(sig):
    # Unused complex decoding logic (red herring)
    parts = [int(sig[i:i+2], 16) for i in range(0, len(sig), 2)]
    decrypted = []
    for p in parts:
        p = (p ^ 0x5A) % 256
        p = (p >> 2) | ((p & 0x03) << 6)
        decrypted.append(p)
    return decrypted  # Never called

def validate_integrity(arr, key):
    # Checksum that appears important but is bypassed
    xor_check = 0
    for x in arr:
        xor_check ^= int(abs(x) * 100) % 256
    return (xor_check + key) % 256 == 127  # Not actually enforced

def analyze_signal(signal, system_key):
    # Core analysis logic buried in distractions
    magnitude = sum([abs(x) for x in signal])
    peak = max(signal, default=0)
    entropy_proxy = 0.0
    for x in signal:
        if x != 0:
            entropy_proxy -= x * math.log(abs(x)+1e-8)
    
    # Critical computation path
    score_a = magnitude * 100
    score_b = abs(peak) * 500
    score_c = entropy_proxy * 20
    
    # Decoy variables and operations
    decoy_set = {score_a % 10, score_b % 10, score_c % 10, system_key % 10}
    if len(decoy_set) > 3:
        score_b += 17  # Slight modification based on irrelevant condition
    
    # Final diagnostic is combination of real signal metrics
    final_diagnostic = int(score_a + score_b + score_c - 150)
    
    # Multiple print statements to distract
    debug_info = f"Signal length: {len(signal)}, Key fragment: {system_key & 0xF}"
    metadata_log = "Processing complete" + debug_info  # Unused
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    telemetry = collect_telemetry()
    
    # Apply filter chain
    processed = preprocess(telemetry)
    
    # Generate system key through bit manipulation
    base_key = len(telemetry) ^ 123
    enhanced_key = encrypt_key(base_key, salt=29)
    system_key = (enhanced_key + 64) & 0x7F
    
    # Validate (but don't act on result)
    _ = validate_integrity(processed, system_key)  # Result ignored
    
    # Filter again with meaningful impact
    filtered_data = [x for x in processed if x > -0.75]
    
    # CORE EXECUTION POINT
    final_diagnostic = analyze_signal(filtered_data, system_key)
    
    # Print only the target result
    print(f"Result: {final_diagnostic}")