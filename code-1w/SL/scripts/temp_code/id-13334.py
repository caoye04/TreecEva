def analyze_sensor_data(raw_readings):
    # Irrelevant data transformation (dead-end function)
    normalized = [x * 0.98 + 2.1 for x in raw_readings if x > 0]
    filtered = [x for x in normalized if x < 100]
    return sum(filtered) / len(filtered) if filtered else 0

# Decoy sensor dataset (never actually used in final computation)
sensor_log = [105, -5, 203, 45, 76, 0, 110, 98, 150, 30, 88]
baseline_offset = 7.2
temp_correction_factor = 0.88

# Core process: thermal cycle simulation
def simulate_cycle(phase_count, efficiency_ratio=1.0):
    history = []
    for i in range(1, phase_count + 1):
        # Complex but irrelevant intermediate calculation
        transient = (i ** 2) * efficiency_ratio
        if i % 3 == 0:
            transient -= efficiency_ratio * 5
        history.append(transient + 1.5)
    return history

# Data registry with multiple red herrings
data_registry = {
    'calibration_v1': {'factor': 0.77, 'active': False},
    'calibration_v2': {'factor': 1.15, 'active': True},
    'diagnostics': {'run_count': 12, 'errors': [None, None]},
    'last_reset': '2023-07-15',
    'yield_profile': [0.8, 0.9, 1.0, 1.2, 1.5]  # Unused field
}

# Another decoy function that simulates analysis but leads nowhere
def evaluate_stability(log_entries):
    cumulative = 0
    for entry in log_entries:
        if isinstance(entry, int) and entry > 50:
            cumulative += entry * 0.01
    return cumulative

eval_result = evaluate_stability(sensor_log)  # Dead-end assignment

# Set operations with misleading relevance
observed_phases = {'init', 'ramp', 'hold', 'cool'}
required_phases = {'init', 'ramp', 'hold', 'cool', 'stabilize'}
missing_phase = required_phases - observed_phases  # {'stabilize'} – unused

# Critical path begins here — real computation chain
heating_cycles = [4, 6, 5, 7, 3]

# Real processing logic buried among distractions
def calculate_thermal_yield(cycles):
    adjustments = {
        3: 0.85,
        4: 0.90,
        5: 1.00,
        6: 0.95,
        7: 0.80
    }
    
    total_weighted = 0
    total_duration = 0
    
    for cycle in cycles:
        duration = cycle * 10  # Each cycle unit = 10 mins
        base_yield = 250 * (cycle / 5)  # Base yield scales with ideal reference
        adjusted_yield = base_yield * adjustments.get(cycle, 0.75)
        total_weighted += adjusted_yield
        total_duration += duration
    
    average_yield = total_weighted / len(cycles)
    
    # Final adjustment using set-derived logic (only one element matters)
    if 'stabilize' not in missing_phase:  # This condition is True, but hard to see
        average_yield *= 1.1
    
    # Secondary correction based on dictionary lookup
    active_cal = None
    for key, val in data_registry.items():
        if isinstance(val, dict) and val.get('active'):
            active_cal = val
            break
    
    if active_cal:
        average_yield *= active_cal['factor']  # factor = 1.15
    
    return round(average_yield, 4)

# Additional distraction: recursive counting (unused)
def count_transients(n):
    if n <= 1:
        return 1
    return count_transients(n - 1) + count_transients(n - 2)

fibonacci_side_effect = count_transients(6)  # Result: 13, never used

# Key execution point
final_yield = calculate_thermal_yield(heating_cycles)

# Output the correct result
print(f"Result: {final_yield}")