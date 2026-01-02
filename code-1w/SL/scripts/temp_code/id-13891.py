import math

# Simulated sensor data from a distributed monitoring system
temperature_readings = [23.5, 24.1, 22.7, 25.3, 26.0, 24.8, 23.9]
humidity_levels = [45, 47, 50, 43, 40, 48, 51]
pressure_data = [1013, 1015, 1012, 1010, 1008, 1014, 1016]

# Irrelevant calibration offset (distractor)
calibration_offset = sum([abs(t - 24) for t in temperature_readings]) / len(temperature_readings)

# System status flags (some are decoys)
STATUS_ACTIVE = 0b1000
STATUS_STANDBY = 0b0100
STATUS_ERROR = 0b0010
STATUS_DIAGNOSTIC = 0b0001

system_flags = [STATUS_ACTIVE, STATUS_STANDBY, STATUS_ACTIVE, STATUS_ACTIVE]
active_count = sum(1 for flag in system_flags if flag & STATUS_ACTIVE)

# Misleading health score calculation (not used in final result)
health_score = 0
for i, temp in enumerate(temperature_readings):
    if temp < 23 or temp > 25:
        health_score += max(0, 100 - abs(temp - 24) * 5)
    else:
        health_score += 95
health_score = health_score / len(temperature_readings)

# Core diagnostic logic
baseline_reference = 24.0
variance_pool = []

for i, (t, h) in enumerate(zip(temperature_readings, humidity_levels)):
    normalized_temp = (t - baseline_reference) ** 2
    humidity_factor = 1 + (h - 45) / 100
    adjusted_variance = normalized_temp * humidity_factor
    variance_pool.append(adjusted_variance)

# Compute entropy-like measure from variance distribution
total_entropy = 0.0
for v in variance_pool:
    if v > 0:
        total_entropy -= v * math.log(v)

# Pressure trend analysis (unused red herring)
pressure_trend = 0
for i in range(1, len(pressure_data)):
    pressure_trend += (pressure_data[i] - pressure_data[i-1]) ** 2
average_pressure_shift = math.sqrt(pressure_trend) if pressure_trend > 0 else 0

# System load simulation with bit manipulation
system_load = 0
for i in range(len(variance_pool)):
    shift_amount = i % 4
    system_load ^= int(variance_pool[i] * 10) << shift_amount
    system_load &= 0xFFFF  # Keep within 16-bit

# Health signature via tuple unpacking and filtering
diagnostic_pairs = [(v, i) for i, v in enumerate(variance_pool) if v > 0.5]
filtered_indices = {i for v, i in diagnostic_pairs}
health_signature = tuple(
    int.from_bytes(f'X{i}'.encode(), 'little') if i in filtered_indices else 0
    for i in range(4)
)

# Decoy function - appears important but unused
def compute_stability_index(data):
    mean_val = sum(data) / len(data)
    var = sum((x - mean_val) ** 2 for x in data) / len(data)
    return 1 / (1 + var)

# Key processing function with conditional expression and list comprehension
def process_metrics(signature: tuple, load: int):
    # Extract components using destructuring
    s0, s1, s2, s3 = signature
    
    # Composite weight calculation
    weights = [s0 + 1, s1 + 2, s2 + 3, s3 + 4]
    weighted_sum = sum(w * (load >> i) for i, w in enumerate(weights))
    
    # Nonlinear transformation chain
    intermediate = abs(weighted_sum) % 1000
    intermediate = (intermediate ^ 0xAAAA) & 0xFFFF
    intermediate = (intermediate * 3) // 7
    
    # Conditional adjustment based on bit population count
    popcount = bin(intermediate).count('1')
    adjustment = 100 if popcount > 8 else 50
    
    # Final aggregation using list comprehension and enumeration
    history_buffer = [intermediate]
    for _ in range(2):
        new_val = sum(
            (v ^ (i * adjustment)) % 97 
            for i, v in enumerate(history_buffer)
        )
        history_buffer.append(new_val)
    
    # Real-time correction factor (this determines the output)
    correction = sum(
        math.sin(math.radians(load % 180)) 
        for _ in range(3)
    )
    
    # Final diagnostic value
    final_value = history_buffer[-1] + int(correction * 100)
    
    # Dead code path - never executed due to logic
    if final_value < 0 and False:
        final_value = abs(final_value) ^ 0xFF
        
    return final_value

# Execute critical statement
current_diagnostic = 42  # Placeholder overwritten below
final_diagnostic = process_metrics(health_signature, system_load)

# Print result as required
print(f"Target result: {final_diagnostic}")