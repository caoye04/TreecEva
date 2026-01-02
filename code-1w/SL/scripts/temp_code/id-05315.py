import math

# System calibration constants (irrelevant to final result)
CALIBRATION_FACTOR = 0.987
REFERENCE_VOLTAGE = 3.3
MAX_BUFFER_SIZE = 1024

# Sensor input data (real and decoy)
sensor_readings = [23.5, 24.1, 22.9, 25.0, 26.3, 24.8, 23.0]
ambient_offsets = [0.1, -0.2, 0.05, 0.3, -0.15, 0.0, 0.1]

# Distractor: unused sensor fusion
fusion_weights = [0.8, 1.2, 0.9, 1.1, 0.85, 0.95, 1.0]
weighted_fusion = [a * w for a, w in zip(sensor_readings, fusion_weights)]  # Dead computation

# Conduction matrix from material layers (relevant)
conduction_matrix = [
    [1.0, 0.5, 0.2],
    [0.5, 1.8, 0.6],
    [0.2, 0.6, 2.0]
]

# Ambient thermal profile (relevant)
ambient_profile = [22.0, 28.0, 35.0]

# Auxiliary state variables (mix of relevant and irrelevant)
current_draw_mA = 128.4
signal_strength = -74  # dBm, unused
packet_counter = 0

# Decoy function: signal processing (never called)
def process_signal_frame(frame):
    fft_buffer = [math.sin(f / 10) for f in frame]
    return [abs(x) * CALIBRATION_FACTOR for x in fft_buffer]

# Real calculation function
def calculate_thermal_flux(matrix, profile):
    flux_vector = []
    for i, row in enumerate(matrix):
        component = sum(row[j] * profile[j] for j in range(len(profile)))
        flux_vector.append(component)
    
    # Secondary transformation
    normalized = [val / (i + 1) for i, val in enumerate(flux_vector)]
    
    # Aggregate using min/max logic (key step)
    peak = max(normalized)
    trough = min(normalized)
    return round((peak - trough) * 1000, 4)

# Simulated data logger (distractor loop)
log_entries = []
for idx, temp in enumerate(sensor_readings):
    status_flag = 'NORM' if 22 <= temp <= 25 else 'ELEV'
    entry = f"T{idx}:{temp:.1f}{status_flag}"
    log_entries.append(entry)
    packet_counter += 1  # Incremented but unused

# Background task: cache pre-allocation (irrelevant)
prealloc_cache = []
for _ in range(MAX_BUFFER_SIZE // 32):
    prealloc_cache.append([0] * 32)

# Critical execution point
thermal_gradient = calculate_thermal_flux(conduction_matrix, ambient_profile)

# Additional red herring: voltage-based adjustment (not applied)
battery_level = REFERENCE_VOLTAGE * 0.94
voltage_ratio = battery_level / REFERENCE_VOLTAGE
adjustment_factor = math.log(voltage_ratio + 1) if voltage_ratio > 0 else 0

# Output the target result
print(f"Result: {thermal_gradient}")