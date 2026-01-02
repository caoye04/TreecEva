import math

# Simulated sensor array diagnostics with noise filtering and pattern analysis
def collect_sensor_readings():
    raw_readings = [127, 255, 192, 64, 31, 88, 150, 200]
    calibrated = [r * 0.78 for r in raw_readings]
    filtered = [f for f in calibrated if f > 50]  # Remove low-noise artifacts
    return filtered

# Irrelevant auxiliary function – dead code path
def deprecated_normalization(x):
    return (x - min(x)) / (max(x) - min(x)) if max(x) != min(x) else [0.5] * len(x)

# Noise injection simulation – irrelevant to final result
def generate_synthetic_noise(seed=42):
    noise = []
    for i in range(10):
        val = (seed * i + 17) % 101
        noise.append(val)
    return noise

# Signal transformation: applies scaling and bit-based masking
def transform_signal(readings):
    shifted = []
    for val in readings:
        temp = int(val)
        masked = temp & 0b111111  # Keep only lower 6 bits
        adjusted = (masked ^ 21) + 3  # XOR obfuscation + offset
        shifted.append(adjusted)
    return shifted

# Secondary transformation chain
def encode_sequence(data):
    encoded = []
    for d in data:
        if d % 2 == 0:
            encoded.append(d // 2)
        else:
            encoded.append(d * 3 + 1)
    return encoded

# Misleading complexity: checksum that is never used
def compute_legacy_checksum(arr):
    checksum = 0
    for i, v in enumerate(arr):
        checksum += v * (i + 1)
    checksum = checksum % 97
    return checksum

# Core analysis function — only this affects final answer
def analyze_pattern(seq):
    total_power = 0
    decay_factor = 1.0
    
    for item in seq:
        contribution = item * decay_factor
        total_power += contribution
        decay_factor *= 0.9  # Exponential decay over sequence
    
    # Final adjustment using bitwise blend
    magnitude = int(total_power)
    flag_mask = 0b101010
    blended = magnitude ^ flag_mask  # XOR with fixed pattern
    return blended + 5

# Unused diagnostic tree — red herring
def run_diagnostics():
    status_flags = {"level": "nominal", "alert": False}
    history = []
    for step in range(5):
        history.append({"step": step, "active": True})
    return status_flags

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect real sensor data
    sensor_data = collect_sensor_readings()
    
    # Step 2: Transform signal using bit operations
    processed_signal = transform_signal(sensor_data)
    
    # Step 3: Apply encoding sequence (transforms values)
    transformed_data = encode_sequence(processed_signal)
    
    # Step 4: Compute irrelevant legacy checksum (dead computation)
    unused_checksum = compute_legacy_checksum(transformed_data)
    
    # Step 5: Generate synthetic noise (never used)
    noise_profile = generate_synthetic_noise()
    
    # Step 6: Run diagnostics (unused side effect)
    diagnostics = run_diagnostics()
    
    # Step 7: Analyze the transformed data pattern (critical path)
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Output result
    print(f"Result: {final_diagnostic}")