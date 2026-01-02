def analyze_readings(readings):
    total = 0
    count = 0
    for val in readings:
        if val > 0 and val % 2 == 1:
            total += val ** 0.5
            count += 1
    return total / count if count else 0

# Simulated sensor data from environmental monitoring system
temperature_readings = [36, 49, 64, 81, 100]
humidity_flags = [True, False, True, False]
pressure_sequence = [1013, 1009, 1015, 1020, 1005]

# Auxiliary computation - computes average fluctuation (distraction)
avg_fluctuation = 0
for i in range(1, len(pressure_sequence)):
    avg_fluctuation += abs(pressure_sequence[i] - pressure_sequence[i-1])
avg_fluctuation /= len(pressure_sequence) - 1

# Bitwise calibration mask based on device status
device_status = 0b1101
mask_offset = (device_status & 0b111) ^ 0b101
adjusted_mask = (device_status << 1) | 0b1

# Primary health metric processing
def process_metrics(data, limit):
    raw_score = 0
    penalty = 0
    
    # Process each datum with conditional transformation
    for x in data:
        if x > limit:
            temp_val = int(x / 2)
            if temp_val % 2 == 0:
                raw_score += temp_val >> 1
            else:
                raw_score += temp_val << 1
        else:
            raw_score += x + (x & 3)  # Add bitwise adjustment
    
    # Spurious secondary loop - looks important but unused in result
    diagnostic_trace = []
    for _ in range(3):
        diagnostic_trace.append(f"Trace-{raw_score % 7}")
    
    # String-based validation (uses string method)
    status_str = "normal" if raw_score < 150 else "elevated"
    normalized_status = status_str.strip().upper()
    
    # Final penalty application
    if len(normalized_status) > 5:
        penalty = 10
    
    # Critical variable assignment
    final_diagnostic = raw_score - penalty
    
    # Red herring: irrelevant tuple unpacking
    backup_codes = ['ERR0', 'WARN1', 'OK2']
    a, b, c = backup_codes  # unused afterward
    
    return final_diagnostic

# Data preparation
processed_temps = [int(t ** 0.5) for t in temperature_readings]
extended_data = processed_temps + [x // 100 for x in pressure_sequence]

# Threshold logic based on humidity pattern
threshold = 6
if sum(humidity_flags) >= 2:
    threshold += 2

# Execute main analysis
health_data = extended_data
final_diagnostic = process_metrics(health_data, threshold)

# Output result
print(f"Result: {final_diagnostic}")