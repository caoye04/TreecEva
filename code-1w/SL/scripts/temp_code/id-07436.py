from collections import defaultdict, Counter
import math

# Irrelevant helper functions (dead code paths)
def deprecated_normalization(x):
    return sum(i**2 for i in x) ** 0.5

def unused_checksum(data):
    return sum(data) % 256

def obsolete_mapping(value):
    return ((value << 3) ^ 0xAA) & 0xFF

# Core simulation parameters (some are decoys)
initial_pressure = 101.3
ambient_temperature_celsius = 25
reference_humidity = 60
noise_factor = 0.07  # unused in final calculation

# Distractor data structures
telemetry_log = defaultdict(lambda: 'N/A')
telemetry_log['sensor_01'] = 'OK'
telemetry_log['sensor_02'] = 'ERR'
telemetry_log['sensor_03'] = 'OK'

diagnostic_codes = [101, 110, 101, 111, 101]
frequency_weights = {x: diagnostic_codes.count(x) for x in set(diagnostic_codes)}

# Simulated sensor array with irrelevant transformations
raw_signals = [2.1, 3.4, 1.8, 4.0, 2.7]
filtered_signals = [round(s * 1.05, 2) for s in raw_signals if s > 2.0]  # distractor
signal_power = sum(fs**2 for fs in filtered_signals)  # misleading intermediate

# State representation with red herrings
equilibrium_state = {
    'phase': 'liquid',
    'density_g_cm3': 0.98,
    'molecular_complexity': 3,
    'bond_count': 12,
    'temperature_k': ambient_temperature_celsius + 273.15,
    'activation_threshold': 4.7
}

# Decoy function that looks relevant but isn't called in critical path
def evaluate_phase_stability(state):
    if state['phase'] == 'gas':
        return math.exp(-state['density_g_cm3'])
    else:
        return math.log(state['density_g_cm3'] + 1)

# Key transformation function with embedded logic and distractions
def transform_molecular_data(data):
    complexity = data['molecular_complexity']
    bonds = data['bond_count']
    
    # Distractor computation
    hypothetical_energy = complexity ** 3 - bonds * 2.1
    
    # Relevant transformation mixed with noise
    adjusted_bonds = bonds + (1 if complexity >= 3 else 0)
    entropy_component = math.log(adjusted_bonds) if adjusted_bonds > 0 else 0
    
    # Conditional expression (Python idiom)
    stability_factor = 1.8 if data['phase'] == 'liquid' else 0.9
    
    # Return tuple - destructuring later
    return (complexity * 0.4, entropy_component * stability_factor)

# Secondary processing with list comprehension distraction
def process_redundant_array(values):
    squared_chain = [v**2 for v in values]
    chained_sum = sum(squared_chain)
    return [math.sqrt(x + 0.1) for x in squared_chain]  # dead end

# Main calculation buried among distractions
def calculate_thermal_properties(state):
    temp_k = state['temperature_k']
    density = state['density_g_cm3']
    
    # Extract from tuple unpacking
    comp_factor, entropic_term = transform_molecular_data(state)
    
    # Multiple arithmetic steps with plausible but unused intermediates
    base_capacity = temp_k * 0.00418  # specific heat approximation
    density_adjustment = (density / 0.85) ** 1.2
    
    # Critical path includes conditional expression
    phase_multiplier = 1.4 if state['phase'] == 'liquid' else 0.75
    
    # Composite formula with multiple concepts
    thermal_index = base_capacity * density_adjustment * phase_multiplier
    
    # Final adjustment using entropic term from earlier
    final_result = thermal_index + (entropic_term * 0.3)
    
    # Red herring: create a complex counter that does nothing
    signal_counter = Counter(['A']*int(density*10) + ['B']*int(temp_k % 10))
    dummy_correction = len(signal_counter) * 0.01  # not used
    
    return final_result

# Misleading pre-computations
baseline_metric = initial_pressure * 0.02897  # gas constant red herring
intermediate_fusion = math.atan2(baseline_metric, ambient_temperature_celsius)

# Key execution point
thermal_capacity = calculate_thermal_properties(equilibrium_state)

# Output required format
print(f"Result: {thermal_capacity}")