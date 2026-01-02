def analyze_system_state(mode, threshold=0.75):
    if mode == 'high_power':
        return lambda x: x * 1.8 + 2
    elif mode == 'economy':
        return lambda x: x * 0.9 - 1
    else:
        return lambda x: x

# Irrelevant sensor simulation (distractor)
sensor_log = ['temp_OK', 'voltage_stable', 'fan_normal']
sensor_flags = {entry: len(entry) for entry in sensor_log if 'n' in entry}

# System calibration constants (some are decoys)
base_efficiency = 42.5
legacy_offset = -3.14159
dummy_matrix = [[i*j + 0.1 for j in range(3)] for i in range(3)]

# Conditional expression with red herring variables
system_mode = 'high_power' if base_efficiency > 40 else 'economy'
override_flag = False

# Bit manipulation decoy (unused path)
crypto_key = 0b110101
encoded_signal = crypto_key ^ 0b101100 & 0b111000

# Real computation begins here
system_load = 7

# Distractor: unused recursive function
def calculate_entropy(n):
    if n <= 1:
        return 1
    return n * calculate_entropy(n-1)

# Unused set operation (misleading data structure)
available_channels = {1, 2, 3, 5, 8, 13}
failed_channels = {x for x in available_channels if x % 2 == 0}
redundant_capacity = len(available_channels.difference(failed_channels))

# Dictionary-based adjustment map (partially relevant)
efficiency_map = {
    'high_power': lambda x: x * 1.2,
    'economy': lambda x: x * 0.85,
    'turbo': lambda x: x * 1.5
}

# Conditional expression using string method as control flow
mode_suffix = system_mode[-5:].upper() if system_mode != 'unknown' else 'BASE'
modifier_factor = 1.1 if mode_suffix.endswith('POWER') else 0.9

# Main transformation chain
adjusted_base = base_efficiency * modifier_factor

# Function that appears complex but has simple core logic
def adjust_thermal_rating(efficiency, load):
    # Nested conditional branches (3 levels)
    if efficiency > 40:
        if load > 5:
            rating = efficiency * 2.1
            if 'high' in system_mode:
                # Key assignment happens here
                capacity = int(rating) + (load ** 2)
                
                # Dead code path (never executed due to prior condition)
                if efficiency < 30:
                    capacity -= 1000  # Decoy adjustment
                
                # Irrelevant string transformation
                debug_tag = f"CAP_{str(capacity)}".replace('_', '-')
                log_entry = debug_tag.lower().split('p')
                
                return capacity
        else:
            return int(efficiency)
    else:
        return efficiency * 0.5

# Critical statement
thermal_capacity = adjust_thermal_rating(base_efficiency, system_load)

# Final output
Result: thermal_capacity