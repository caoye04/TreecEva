import math

# Simulated sensor data from a distributed monitoring system
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1, 25.3]
humidity_readings = [45, 47, 50, 44, 52, 48, 46, 51]
packet_loss_log = ['OK', 'OK', 'ERROR', 'OK', 'OK', 'ERROR', 'OK', 'OK']

# Irrelevant utility function (decoy)
lambert_transform = lambda x: math.log(x) if x > 0 else 0

# Distractor variables (unused in final calculation)
baseline_offset = 0.987
redundant_cache = {i: lambert_transform(i+1) for i in range(10)}
system_uptime_hours = 1273
emergency_override_flag = False

# Core signal processing
filtered_temps = list(filter(lambda t: t < 25.5, temperature_readings))
avg_temp = sum(filtered_temps) / len(filtered_temps) if filtered_temps else 0

# Health fingerprint generation (key intermediate step)
def generate_fingerprint(data_stream):
    checksum = 0
    for i, val in enumerate(data_stream):
        checksum += int(val * 10) ^ (i + 1)
    return checksum % 1000

health_signature = generate_fingerprint(humidity_readings)  # This will be used later

# System load computation with red herring path
system_load = 0
for i, status in enumerate(packet_loss_log):
    if status == 'ERROR':
        system_load += 15
    else:
        system_load += 2  # Normal operation penalty

# Dead code path (never executed due to flag)
if emergency_override_flag:
    system_load = max(0, system_load - 100)
    correction_factor = 1.75
    temp_adjustment = []
    for t in temperature_readings:
        temp_adjustment.append(t * correction_factor)

# Unused recursive function (distractor)
def calculate_depth(n):
    if n <= 1:
        return 1
    return calculate_depth(n-1) + calculate_depth(n-2)

# Secondary metric with string manipulation distraction
event_summary = "".join([status[0] for status in packet_loss_log])  # "OKOKEOKK"
error_count = event_summary.count('E')
summary_length = len(event_summary)

# Decoy transformation chain
transformed_summary = event_summary.replace('K', 'X').lower()  # "oxoxeoxx"
parity_flag = summary_length % 2 == 0

# Real processing begins here — multiple assignment distraction
raw_score, weight_factor = health_signature, 3
adjusted_score = raw_score * weight_factor

# Conditional branch with misleading comment
# NOTE: The following block looks important but only affects unused var
if avg_temp > 24.0:
    confidence_level = 'MODERATE'
    diagnostic_trace = [f"Step{i}" for i in range(3)]
else:
    confidence_level = 'HIGH'
    diagnostic_trace = []

# Critical function: combines two key metrics
def process_metrics(sig, load):
    # Bit manipulation red herring
    masked_sig = sig ^ 0b110101
    shifted_load = (load << 2) & 0b11111111
    
    # Actual computation hidden among distractions
    primary = (sig * 7) // 10
    secondary = (load * 2) + 5
    
    # Complex-looking but irrelevant ternary
    fallback = primary if masked_sig > 50 else secondary
    
    # The real answer derivation (non-obvious)
    result = (primary + secondary) - (masked_sig & shifted_load)
    return result

# Key execution point
final_diagnostic = process_metrics(health_signature, system_load)

# Print required output
print(f"Target result: {final_diagnostic}")