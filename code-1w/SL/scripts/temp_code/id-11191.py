import math

# Simulated sensor fusion system for environmental monitoring
base_threshold = 42.5
noise_floor = 0.73
sample_size = 128
calibration_offset = -1.2

# Irrelevant calibration data (red herring)
legacy_modes = ['LEGACY_MODE_A', 'LEGACY_MODE_B']
system_flags = {0: 'ACTIVE', 1: 'STANDBY'}

# Real signal data from sensors
raw_readings = [math.sin(i * 0.1) + 0.5 * math.cos(i * 0.3) for i in range(sample_size)]

# Distraction: unused signal transformation chain
transformed_cache = []
for idx in range(len(raw_readings)):
    if idx % 7 == 0:
        transformed_cache.append(math.tanh(raw_readings[idx] * 0.5))

# Decoy function that's never called
def deprecated_analysis(data):
    return sum(x ** 2 for x in data if x > 0.1)

# Signal conditioning with multiple distraction paths
filtered_readings = []
outlier_count = 0
for val in raw_readings:
    adjusted = val + calibration_offset
    if abs(adjusted) > noise_floor * 3:
        outlier_count += 1
        continue  # Skip outliers
    filtered_readings.append(abs(adjusted))

# Distractor: irrelevant statistical moments
moment_2 = sum(x*x for x in filtered_readings) / len(filtered_readings) if filtered_readings else 0
skewness = sum((x - moment_2)**3 for x in filtered_readings) / len(filtered_readings) if filtered_readings else 0

# Real processing path begins here
compression_factor = 2
compressed_chunks = []
for i in range(0, len(filtered_readings), compression_factor):
    chunk = filtered_readings[i:i+compression_factor]
    if len(chunk) == compression_factor:
        compressed_chunks.append(sum(chunk))

# Bit manipulation for data encoding (relevant)
encoded_checksum = 0
for i, chunk_val in enumerate(compressed_chunks):
    rotated = ((i << 3) | (i >> 5)) & 255  # 8-bit rotation
    encoded_checksum ^= int(chunk_val * 10) & rotated

# Set operations for anomaly detection (required python feature)
expected_indices = set(range(50))
actual_indices = set(i for i, v in enumerate(compressed_chunks) if v > 0.3)
anomaly_set = expected_indices - actual_indices
suppressed_count = len(anomaly_set)

# Conditional expression processing tree (required python feature)
processed_signals = [
    val * 1.8 if val < base_threshold * 0.3 else
    val * 1.2 if val < base_threshold * 0.6 else
    val * 0.7
    for val in compressed_chunks[:60]
]

# Unused recursive distraction
def fake_recursive(n):
    if n <= 1:
        return 1
    return fake_recursive(n-1) + fake_recursive(n-2)

# Critical analysis function
def analyze_readings(signals):
    if not signals:
        return -1
    
    # Primary accumulation logic
    total_power = 0
    for i, sig in enumerate(signals):
        weight = math.log(2 + i) if i % 3 == 0 else 1.0
        contribution = sig * weight
        total_power += contribution
    
    # Secondary adjustment using bit operations
    temp_state = int(total_power) & 0xFFFF
    temp_state ^= (temp_state >> 8)
    temp_state &= 0xFF
    
    # Final computation with conditional override
    adjustment_factor = 1.25 if len(signals) > 40 else 0.95
    final_score = total_power * adjustment_factor
    
    # Tertiary filtering based on checksum (this determines answer)
    control_key = encoded_checksum & 0xFF
    if control_key % 7 == 0:
        final_score -= 15.6
    elif control_key % 5 == 0:
        final_score += 8.3
    else:
        final_score += 3.14159
    
    return final_score

# Dead code path - looks important but unused
emergency_protocols = ['SHUTDOWN', 'REBOOT', 'FAILSAFE']
active_protocol = emergency_protocols[0] if suppressed_count > 10 else emergency_protocols[1]

# Key execution point
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Target result: {final_diagnostic}")