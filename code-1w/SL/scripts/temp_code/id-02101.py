import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw = [127, 255, 193, 64, 80, 200]
    processed = []
    for val in raw:
        if val > 128:
            processed.append(val // 2)
        else:
            processed.append(val)
    return processed

# Irrelevant auxiliary function (decoy)
def compute_checksum(data):
    checksum = 0
    for d in data:
        checksum ^= d
    return checksum * 3

# Data transformation involving bit manipulation and filtering
def transform_signal(signal):
    shifted = [(x << 1) & 255 for x in signal]
    filtered = [x for x in shifted if x % 17 != 0]
    return [x ^ 90 for x in filtered]  #扰乱模式

# Core pattern analyzer (critical path)
def count_oscillations(seq):
    if len(seq) < 3:
        return len(seq)
    count = 0
    for i in range(1, len(seq) - 1):
        if seq[i-1] < seq[i] > seq[i+1] or seq[i-1] > seq[i] < seq[i+1]:
            count += 1
    return count + len(seq) // 4

# String-based metadata tagging (uses string methods - required feature)
def generate_tag(iterations, mode):
    base = f"diag_{mode}_run{iterations}"
    return base.upper().replace('_', '-') + ".log"

# Misleading peak detection (red herring)
def detect_peaks(data):
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(i)
    scale_factor = 2.5
    return [p * scale_factor for p in peaks]

# Main analysis function combining multiple concepts
def analyze_pattern(data, limit):
    # Modular arithmetic and set operations
    mod_values = {x % 13 for x in data if x > 50}
    temp = []
    for i, x in enumerate(data):
        if i % 2 == 0:
            temp.append(int(math.sin(math.pi * i / 6) * 100) + x)
        else:
            temp.append(x - (i ** 2 % 7))
    
    # Conditional expression mix
    adjusted = [v + 10 if v < limit else v - 5 for v in temp]
    
    # Decoy computation with unused result
    shadow_copy = adjusted[:]
    for j in range(len(shadow_copy)):
        shadow_copy[j] = (shadow_copy[j] ^ 255) & 127
    
    # Critical calculation path
    base_score = sum(adjusted) // len(adjusted) if adjusted else 0
    oscillation_count = count_oscillations(adjusted)
    set_enrichment = len(mod_values) * 17
    
    # Final composition using distractor-influenced logic
    final_value = base_score + oscillation_count * 3 - set_enrichment
    
    # Dead code branch (never executed - misleading)
    debug_mode = False
    if debug_mode and len(data) > 100:
        extra = compute_checksum(data)
        final_value += extra // 100
    
    return final_value

# Orchestration with irrelevant setup
if __name__ == "__main__":
    readings = collect_readings()
    signal = transform_signal(readings)
    
    # Unused variables and decoy operations
    metadata_tag = generate_tag(5, "calibration")
    peaks_list = detect_peaks(signal)
    dummy_set = {x * 2 for x in signal if x < 100}
    
    threshold = 85
    final_diagnostic = analyze_pattern(transformed_data=signal, threshold=threshold)
    print(f"Result: {final_diagnostic}")