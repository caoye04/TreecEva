import math

# Simulated sensor array data from environmental monitoring system
def collect_sensor_data():
    raw_readings = [127, 255, 192, 64, 96, 159, 223, 31]
    offset = 128
    adjusted = [r ^ offset for r in raw_readings]  # Apply XOR calibration
    return adjusted

# Signal processing with red herring transformations
def process_signals(data):
    processed = []
    temp_cache = {}
    
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed = int(math.sqrt(val) * 10) if val > 0 else 0
            processed.append(transformed)
            # Dead code path - never accessed due to logic
            if transformed > 1000:
                temp_cache[i] = transformed ** 2
        else:
            shifted = val >> 2
            processed.append(shifted)
            
    # Distractor: irrelevant list comprehension with no side effects
    _ = [x * x for x in range(len(processed)) if x % 3 == 0]
    
    # Another decoy operation
    checksum = sum(data) & 0xFF
    checksum = (checksum << 4) | (checksum >> 4)  # Bit rotation (unused)

    # Actual relevant transformation
    normalized = [p / 2.5 for p in processed]
    return normalized

# Misleading diagnostic chain with early exits
def quick_diagnostic(signal):
    if len(signal) == 0:
        return -1
    if max(signal) < 10:
        return 0
    if sum(signal) % 7 == 0:  # Red herring condition
        return 1
    return None  # This function appears important but is unused

# Core analysis logic — only this matters
# But buried among distractions
def analyze_readings(readings):
    base_score = 0
    weights = [0.8, 1.2, 0.9, 1.1, 1.0, 0.7, 1.3, 0.6]
    
    # Relevant weighted accumulation
    for i, (idx, reading) in enumerate(zip(range(len(readings)), readings)):
        if idx % 2 == 0:
            base_score += reading * weights[idx]
        else:
            base_score -= reading * 0.5

    # Decoy dictionary with plausible-sounding metrics
    diagnostics = {
        'stability': sum(readings) / len(readings),
        'variance': sum((x - 5) ** 2 for x in readings),
        'entropy': 0.0,
        'peak_noise': max(readings) - min(readings)
    }
    
    # Irrelevant recursive function defined inside (never called)
    def trace_anomaly(path, level):
        if level == 0:
            return path
        return trace_anomaly(path + [level], level - 1)
    
    # Real answer computation — obscured by context
    adjustment = 0
    for r in readings[::2]:
        adjustment += int(r) // 3
    
    final_diagnostic = int(base_score - adjustment * 1.5)
    
    # Multiple prints to distract — only last one matters
    print(f"Diagnostics: {diagnostics}")
    print(f"Adjustment factor: {adjustment}")
    print(f"Base score: {base_score}")
    
    return final_diagnostic

# Unused helper — looks important
def validate_calibration(seq):
    return all(x >= 0 for x in seq) and len(seq) == 8

# Global decoy variables
system_state = {'status': 'nominal', 'mode': 'diagnostic', 'override': True}
last_result = None
audit_log = []

# Main execution flow
if __name__ == "__main__":
    # Collect and process sensor data
    raw = collect_sensor_data()
    processed_signals = process_signals(raw)
    
    # Perform final analysis
    final_diagnostic = analyze_readings(processed_signals)
    
    # Output target result
    print(f"Result: {final_diagnostic}")