import math

# Simulated astrophysical subsystem diagnostics
def analyze_orbital_decay(velocity, mass):
    # Irrelevant computation - red herring
    decay_rate = (velocity ** 2) / (mass * 0.007)
    perturbation = math.sin(decay_rate) * 1.5
    return perturbation

# Misleading auxiliary function with dead logic
def compute_inertial_dampening(force, area):
    if force < 0:
        return 0
    dampening_factor = force / (area + 1e-5)
    # Following lines are never reached but look important
    for i in range(3):
        dampening_factor = math.sqrt(dampening_factor + i)
    return dampening_factor

# Core physics model for thermal signature calculation
def calculate_thermal_signature(mass, entropy):
    if mass <= 0:
        return 0.0
    
    # Complex intermediate steps with distractor variables
    base_energy = mass * (299792458 ** 2)  # E = mc^2
    adjusted_entropy = entropy + math.log(mass + 1)
    temp_proxy = base_energy / (adjusted_entropy + 100)

    # Bit manipulation for quantum correction (semi-relevant)
    quantum_offset = (int(temp_proxy) >> 4) ^ 255
    corrected_temp = temp_proxy - quantum_offset

    # Distractor: unused structural integrity check
    structural_integrity = {"nodes": 12, "threshold": 0.85}
    stress_levels = [0.7, 0.75, 0.81, 0.88]
    if any(s > structural_integrity["threshold"] for s in stress_levels):
        pass  # No action taken, just looks important

    # Real computation path
    fluctuation_index = abs(math.cos(corrected_temp))
    thermal_metric = corrected_temp * fluctuation_index

    # Set operations used as data filter (actual relevance)
    valid_ranges = set(range(1000, 8000))
    fallback_modes = {1100, 1200, 1300}
    operational_set = valid_ranges | fallback_modes
    if int(thermal_metric) not in operational_set:
        thermal_metric *= 0.92

    # Final adjustment using dictionary mapping (key step)
    calibration_map = {0: 1.0, 1: 0.98, 2: 0.97, 3: 0.96, 4: 0.95}
    age_factor = 2
    calibration_factor = calibration_map.get(age_factor, 0.9)
    
    final_quotient = thermal_metric * calibration_factor
    
    # Critical assignment point
    thermal_quotient = final_quotient
    return thermal_quotient

# Irrelevant initialization block
electrical_loads = [120, 135, 140, 128]
avg_load = sum(electrical_loads) / len(electrical_loads)
load_variance = sum((x - avg_load) ** 2 for x in electrical_loads) / len(electrical_loads)

# Unused sensor array emulation
sensor_data = {"temp": 45, "pressure": 220, "flux": 98}
sensor_keys = list(sensor_data.keys())
sorted_keys = sorted(sensor_keys, key=lambda x: x[::-1])

# Primary simulation parameters (some are decoys)
effective_mass = 142.5
system_entropy = 37.8
gravity_well = 9.81
magnetic_shear = 0.45
orbital_inclination = 52.3

# Decoy function call that does nothing critical
analyze_orbital_decay(7600, effective_mass)
compute_inertial_dampening(12500, 14.2)

# Dictionary used for configuration (partially relevant)
config_params = {
    "version": "2.1",
    "mode": "diagnostic",
    "debug": False,
    "iterations": 1
}

# Actual computation path begins here
if config_params["mode"] == "diagnostic":
    for i in range(config_params["iterations"]):
        # Nested conditional with minor side-effect
        if effective_mass > 100 and system_entropy > 20:
            # Multiple layers of logic nesting
            if gravity_well < 10:
                adjustment_phase = 1
                if magnetic_shear > 0.4:
                    adjustment_phase += 1
                    # Key statement embedded in nested logic
                    thermal_quotient = calculate_thermal_signature(effective_mass, system_entropy)
                else:
                    thermal_quotient = 0
            else:
                thermal_quotient = -1
        else:
            thermal_quotient = -999
else:
    thermal_quotient = 0

# Output the result as required
print(f"Result: {thermal_quotient}")