import math

# Irrelevant helper function (decoy)
def compute_buffer_size(packet_rate, overhead):
    return (packet_rate * 128 + overhead) // 7

# Misleading data transformation (dead path)
def transform_coordinates(x, y, z):
    radius = math.sqrt(x**2 + y**2)
    angle = math.atan2(y, x)
    return radius * 1.618, angle * 360 / (2 * math.pi)

# Unused but plausible-looking utility
def normalize_signal(strength, baseline=1.0):
    if strength < 0:
        return 0
    return (strength / baseline) ** 0.5

# Core physics model with distractors
def calculate_thermal_output(elevation, speed):
    # Irrelevant intermediate variables (distractors)
    buffer_zone = 0.0
    signal_strength = 987.6
    calibration_offset = math.sin(math.pi / 6)  # Red herring

    # Real computation begins
    mach = speed / 343.0  # Speed of sound in air
    dynamic_pressure = 0.5 * 1.225 * (speed ** 2)
    
    # Atmospheric density variation with altitude (simplified)
    if elevation < 11000:
        temperature = 288.15 - 0.0065 * elevation
    else:
        temperature = 216.65  # Stratosphere
    
    # Heat flux approximation based on Mach number and pressure
    if mach > 5:
        heating_factor = 0.5 * dynamic_pressure * (mach ** 0.8)
    else:
        heating_factor = 0.3 * dynamic_pressure * (mach ** 0.5)
    
    # Secondary correction using conditional expression (required feature)
    efficiency = 0.89 if elevation > 15000 else 0.72
    
    # Complex composite calculation
    base_energy = heating_factor * efficiency
    
    # Bit manipulation as obfuscation (not actually affecting result)
    decoy_flag = 0b101010
    decoy_flag ^= 0b111111  # Flip bits – irrelevant
    decoy_flag >>= 2       # Shift – still unused
    
    # Tuple unpacking for parallel atmospheric values (suggested paradigm)
    (density, temp_ratio) = (1.225 * math.exp(-elevation/8500), temperature / 288.15)
    
    # Final capacity includes minor logarithmic adjustment
    adjusted_energy = base_energy * math.log(1 + temp_ratio * 2.5)
    
    # Distractor: unused complex expression
    spectral_index = math.acos(temp_ratio) if temp_ratio <= 1 else 0
    buffer_zone += spectral_index  # Dead assignment
    
    # Key assignment: this is the target variable
    thermal_capacity = int(adjusted_energy) + 1000
    
    # More red herrings
    _ = [normalize_signal(i) for i in range(5)]
    dummy_coords = transform_coordinates(3000, 4000, elevation)
    
    return thermal_capacity

# Simulated telemetry input
altitude = 18500  # meters
velocity = 2200   # m/s

# Dead variable assignments (misleading state)
current_mode = "CRUISE"
system_status = {"active": True, "redundancy": 2}
packet_rate = 147
total_bandwidth = compute_buffer_size(packet_rate, 512)  # Irrelevant call

# Critical execution point
thermal_capacity = calculate_thermal_output(altitude, velocity)

# Output result as required
print(f"Result: {thermal_capacity}")