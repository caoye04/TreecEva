import math

# Irrelevant constants for distraction
electrical_resistivity = 0.017  # Ohm*meters (copper)
quantum_number = 7
baseline_frequency = 440.0  # A4 tuning

# Distractor function - never called
def compute_orbital_decay(altitude, drag_coeff):
    return (altitude ** 2) / (drag_coeff + 1e-5)

# Unused data structure
diagnostics_log = {
    'voltage_spikes': [0.0] * 100,
    'thermal_events': [],
    'fault_codes': set()
}

# Core simulation parameters
initial_temperature = 293.15  # Kelvin (20°C)
time_phase = 3
reference_pressure = 101.325  # kPa

# Complex conditional expressions and intermediate distractors
efficiency_ratio = 0.85 if time_phase > 2 else (0.65 if time_phase == 1 else 0.45)
modulation_index = 1.2 * efficiency_ratio

# Bit manipulation red herring
bit_encoded_mode = (time_phase << 3) | 7
bit_filtered = bit_encoded_mode & 0b11111

# Dead computation path
if bit_filtered > 10:
    modulation_index *= 0.9
elif bit_filtered < 5:
    modulation_index /= 0.8
else:
    pass  # No-op branch

# Real calculation chain begins
phase_weight = {
    1: 0.3,
    2: 0.6,
    3: 0.9
}.get(time_phase, 0.75)

# Simulated sensor array with slicing distraction
sensor_readings = [i * 0.1 + math.sin(i) for i in range(50)]
slice_window = sensor_readings[10:20:2]  # Unused slice
offset_correction = sum([x ** 2 for x in slice_window[:3]]) if len(slice_window) > 2 else 0.0

# Logical operations and short-circuit evaluation
valid_signal = (len(sensor_readings) > 0) and (reference_pressure > 0) or (initial_temperature > 0)
emergency_override = False and (quantum_number % 2 == 1)

# Conditional expression affecting downstream calc
pressure_factor = reference_pressure / 100.0 if valid_signal else 1.0

# Primary physics-based calculation
def calculate_thermal_response(phase, efficiency):
    base_conductivity = 0.026
    temperature_rise = initial_temperature * (1.1 ** phase)
    
    # Nested conditionals with early returns
    if phase <= 0:
        return 0.0
    if efficiency < 0.4:
        return base_conductivity * 10
    
    # Main formula
    dynamic_loss = (temperature_rise * pressure_factor * 0.01)
    adjusted_efficiency = efficiency * (1 + math.log(phase + 1))
    
    # Multiple abstraction layers
    def integrate_response(loss, adj_eff, weight):
        raw_integral = (loss * adj_eff) / (weight + 1e-6)
        if raw_integral < 0.5:
            return raw_integral ** 2
        else:
            return math.sqrt(raw_integral) * weight
    
    intermediate_result = integrate_response(dynamic_loss, adjusted_efficiency, phase_weight)
    
    # Final transformation using slicing-like logic (indexing)
    components = [base_conductivity, dynamic_loss, adjusted_efficiency, intermediate_result]
    selected = components[1:]  # Slice distraction
    fused = sum(selected) * 0.25
    
    return fused * 1000  # Scale to larger integer range

# Execution point of interest
temperature_margin = 50.0
thermal_capacity = calculate_thermal_response(time_phase, efficiency_ratio)

# Irrelevant follow-up calculations
if thermal_capacity > 100:
    temperature_margin += thermal_capacity * 0.05
else:
    temperature_margin -= 10.5

# Unused recursive red herring
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Output the target result
print(f"Result: {thermal_capacity}")