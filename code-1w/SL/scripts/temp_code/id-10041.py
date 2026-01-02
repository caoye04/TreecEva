from collections import defaultdict
import math

# Irrelevant helper function (decoy)
def analyze_turbine_efficiency(rpm, load):
    efficiency = 0.0
    if rpm > 5000:
        efficiency = (load * 0.75) / rpm
    else:
        efficiency = (load * 0.5) / (rpm + 100)
    return round(efficiency * 100, 2)

# Unused data structure (red herring)
fuel_consumption_map = {
    'idle': 0.3,
    'cruise': 1.2,
    'boost': 2.8,
    'overclock': 4.5
}

def process_combustion_cycle(temperature_log):
    # Distracting transformation with string methods
    temp_flags = []
    for t in temperature_log:
        status = ('high' if t > 850 else 'normal') if t > 700 else 'low'
        temp_flags.append(f"temp_{status.upper()}")
    
    # Meaningless aggregation
    flag_count = defaultdict(int)
    for flag in temp_flags:
        flag_count[flag] += 1
    
    # This computation looks important but isn't used later
    avg_length = sum(len(f) for f in temp_flags) / len(temp_flags) if temp_flags else 0
    return len(temp_flags) > 5  # Only this matters, rest are distractors

# Simulate sensor noise (dead code path)
def apply_kalman_filter(signal, noise_level=0.1):
    filtered = []
    estimate = signal[0] if signal else 0
    for s in signal:
        residual = s - estimate
        estimate += noise_level * residual
        filtered.append(round(estimate, 3))
    return filtered  # Never called

# Core logic buried among distractions
def evaluate_stress_factor(load_pattern):
    peak_load = max(load_pattern)
    base_score = 0
    
    # Multiple layers of conditionals
    if peak_load > 90:
        base_score = 4
    elif peak_load > 75:
        base_score = 3
    elif peak_load > 60:
        base_score = 2
    else:
        base_score = 1
    
    # Redundant calculation
    normalized_load = [round((x - min(load_pattern)) / (max(load_pattern) - min(load_pattern) + 1e-5), 2) for x in load_pattern]
    complexity_index = sum(1 for x in normalized_load if x > 0.5)
    
    # Decoy metric
    entropy = 0.0
    for p in normalized_load:
        if p > 0:
            entropy -= p * math.log(p)
    
    # Final score depends only on two factors
    adjustment = 1 if complexity_index > 3 else 0.5
    return base_score * adjustment

# Primary calculation obscured by context
def calculate_thermal_rating(status):
    # Key input variables
    raw_temperatures = [720, 780, 805, 860, 880, 910, 895]
    load_sequence = [65, 70, 77, 82, 91, 95, 88]
    
    # Distractor: complex string-based state tracking
    system_states = [f"state_{chr(97+i)}" for i in range(len(raw_temperatures))]
    active_modes = [s.replace('state_', '').upper() for s in system_states if 'e' in s]
    mode_summary = ''.join([m[0] for m in active_modes])
    
    # Real logic starts here — non-obvious due to surrounding noise
    high_temp_events = sum(1 for t in raw_temperatures if t > 850)
    
    # Conditional expression (required python feature)
    baseline_capacity = 1200 if high_temp_events < 3 else 950
    
    # Critical call buried in middle
    stress_test_passed = process_combustion_cycle(raw_temperatures)
    stress_factor = evaluate_stress_factor(load_sequence)
    
    # Bit manipulation decoy (looks relevant but isn't)
    diagnostic_code = 0
    for val in load_sequence[-3:]:
        diagnostic_code ^= int(val) & 0xFF
    
    # Main formula hidden among irrelevant operations
    reliability_modifier = 0.9 if diagnostic_code % 7 == 0 else 1.0
    
    # Actual determining logic (only few steps matter)
    if stress_test_passed and stress_factor >= 3:
        performance_bonus = 150
    else:
        performance_bonus = 0
    
    # Final answer computed here
    thermal_capacity = baseline_capacity + performance_bonus
    thermal_capacity *= reliability_modifier  # Slight reduction if needed
    
    # Dead code — never reached
    if thermal_capacity < 0:
        reset_system_counters()
        
    return int(round(thermal_capacity))

# Unused function (distractor)
def reset_system_counters():
    global fuel_consumption_map
    fuel_consumption_map = defaultdict(float)
    return True

# Simulation data
engine_status = {
    'rpm': 6200,
    'mode': 'performance',
    'version': 'v2.1-alpha',
    'flags': ['overheat_risk', 'high_load']
}

# Execute main logic
thermal_capacity = calculate_thermal_rating(engine_status)
print(f"Result: {thermal_capacity}")