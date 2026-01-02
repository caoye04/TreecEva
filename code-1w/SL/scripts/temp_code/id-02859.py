import math

# Simulated sensor data processing with embedded logic chain
def collect_samples():
    raw = [i * 0.5 for i in range(20)]
    offset = 3.4
    adjusted = [x + offset for x in raw]
    return adjusted

# Irrelevant helper - distractor
def normalize(s):  
    return s.upper().replace(' ', '_')

# Signal conditioning - relevant path
def filter_noise(data):
    filtered = []
    for x in data:
        if abs(x - 5.0) > 1.2:
            filtered.append(x * 0.9)
        else:
            filtered.append(x * 1.1)
    return filtered

# Decoy function - never called, red herring
def decrypt_buffer(buf):
    return sum([ord(c) % 7 for c in buf]) * 13

# Data transformation with case conversion (string method)
def encode_status(code):
    base = f"ERR_{int(code * 2)}"
    return base.lower().capitalize()  # String method used

# Bit manipulation mixed with modular arithmetic
def generate_checksum(values):
    chk = 0
    for i, v in enumerate(values):
        shifted = int(abs(v)) ^ (i % 5)
        chk ^= (shifted + i) % 17
    return chk * 1.05

# Secondary irrelevant computation chain
def compute_thermal_index(seq):
    total = 0
    for val in seq:
        temp = val ** 2 - 2 * val + 5
        if temp > 10:
            total += math.log(temp)
    return total // 1  # Useless aggregation

# Core analysis function - depends on multiple concepts
def analyze_signal(data_chunk):
    magnitude = sum([abs(x) for x in data_chunk])
    threshold = 45.0
    active_peaks = 0
    for val in data_chunk:
        if val > threshold or val < -threshold:
            active_peaks += 1
    # Introduce string-derived conditional (uses string method indirectly)
    status_tag = encode_status(magnitude)
    impact_level = 1 if 'ERR' in status_tag else 0
    
    # Modular arithmetic and bit operations combined
    raw_checksum = generate_checksum(data_chunk)
    mod_factor = int(raw_checksum) % 8
    
    # Critical logic step: nested dependency
    if mod_factor > 4:
        adjustment = (mod_factor ^ 3) * impact_level
    else:
        adjustment = max(active_peaks, len(data_chunk) // 4)
    
    # Distractor variables
    dummy_flag = False
    temp_cache = {}
    for k in range(5):
        temp_cache[k] = k ** 3 - 2 * k
    
    # Final computation - this is the answer path
    diagnostic_score = magnitude / (adjustment + 1)
    final_diagnostic = int(diagnostic_score * 10) / 10.0
    
    # Dead code path - misleading
    if dummy_flag:
        final_diagnostic *= -1
    
    return final_diagnostic

# Unused variable - red herring
system_config = {
    'version': '2.1a',
    'mode': 'diagnostic',
    'debug_keys': ['K9X', 'L2M', 'Z7N']
}

# Main execution flow
samples = collect_samples()
processed_data = filter_noise(samples)

# Irrelevant side computation
thermal_metric = compute_thermal_index(processed_data)
status_msg = normalize("system ready")

# Key statement
final_diagnostic = analyze_signal(processed_data)

# Output result as required
print(f"Target result: {final_diagnostic}")