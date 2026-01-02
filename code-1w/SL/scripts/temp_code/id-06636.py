import math

def analyze_signal_strength(signal_data, noise_floor):
    # Irrelevant function – dead code path
    peak = max(signal_data)
    normalized = [s / peak for s in signal_data]
    snr = [math.log10(val / noise_floor) for val in normalized]
    return sum(snr)

def preprocess_sensors(raw_readings):
    # Distractor preprocessing with misleading normalization
    offset = 0.87
    adjusted = [(x * 1.05 + offset) % 100 for x in raw_readings]
    filtered = [val for val in adjusted if val > 10]
    return [round(f, 2) for f in filtered]

def transform_coordinates(coords, origin):
    # Unused geometric transformation (red herring)
    dx, dy = coords[0] - origin[0], coords[1] - origin[1]
    distance = math.sqrt(dx**2 + dy**2)
    angle = math.atan2(dy, dx)
    rotated_x = distance * math.cos(angle + math.pi / 4)
    return (rotated_x, distance * math.sin(angle + math.pi / 4))

def calculate_thermal_flux(sensors, matrix):
    # Core logic embedded in noise
    total_flux = 0.0
    temp_offsets = []
    for i, reading in enumerate(sensors):
        # Apply calibration matrix using zip and index
        for j, (sensor_j, coeff) in enumerate(zip(sensors, matrix[i % len(matrix)])):
            if i != j:  # Skip diagonal to simulate sensor crosstalk correction
                reading += sensor_j * coeff * 0.1
        temp_offsets.append(math.sin(reading * 0.01))
    
    # Real accumulation begins here
    base_ref = [1.1, 2.2, 3.3, 4.4]
    aggregate = 0
    for idx, (off, base) in enumerate(zip(temp_offsets, base_ref)):
        if idx % 2 == 0:
            aggregate += off * base
        else:
            aggregate -= off * base
    
    # Decoy conditional that looks important but doesn't affect result
    if aggregate < 0:
        aggregate = abs(aggregate) * 1.5
    else:
        dummy_correction = sum([math.tan(off + 0.1) for off in temp_offsets])  # unused

    # Key calculation
    flux_components = []
    for i in range(len(temp_offsets)):
        comp = temp_offsets[i] * (i + 1) ** 1.5
        flux_components.append(comp)
    
    total_flux = sum(flux_components)
    
    # Additional interference: unrelated bitwise masking
    mask = 0b11110000
    masked_value = int(total_flux * 100) & mask  # distractor
    
    # Final computation
    thermal_gradient = total_flux * 0.75 + 12.5
    
    # Dead assignment – irrelevant
    final_diagnostic = {'status': 'OK', 'checksum': masked_value ^ 0xFF}
    
    return thermal_gradient

# Simulated sensor inputs
raw_sensor_data = [23.4, 56.7, 31.2, 44.8]
sensors = preprocess_sensors(raw_sensor_data)

# Calibration matrix for sensor interference modeling
calibration_matrix = [
    [0.1, 0.3, 0.2, 0.4],
    [0.2, 0.1, 0.3, 0.2],
    [0.3, 0.2, 0.1, 0.3],
    [0.4, 0.1, 0.2, 0.1]
]

# Unused data structures as red herrings
coordinates = [(12.5, 34.2), (56.1, 18.9), (42.7, 67.3)]
origin_point = (0.0, 0.0)
transformed_coords = [transform_coordinates(coord, origin_point) for coord in coordinates]

signal_stream = [0.5, 0.7, 0.6, 0.8, 0.9]
noise_level = 0.05
snr_analysis = analyze_signal_strength(signal_stream, noise_level)

# Actual execution point of interest
thermal_gradient = calculate_thermal_flux(sensors, calibration_matrix)

# Print required output
print(f"Result: {thermal_gradient}")