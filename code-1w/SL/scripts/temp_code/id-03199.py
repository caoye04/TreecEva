import math

# System configuration parameters (some are red herrings)
base_frequency = 2400
voltage_level = 1.2
temperature_coefficient = 0.87
overclock_mode = False
cooling_factor = 0.91

# Irrelevant sensor simulation data
temperature_readings = [32.1, 34.5, 33.8, 31.9, 35.2]
humidity_levels = [45, 47, 46, 50, 48]

# Unused function - decoy for thermal modeling
def compute_thermal_headroom(temp_data, hum_data):
    avg_temp = sum(temp_data) / len(temp_data)
    avg_hum = sum(hum_data) / len(hum_data)
    return (100 - avg_temp) * (1 - avg_hum / 100)

# Misleading power calculation with dead variables
idle_power = 15.5
peak_power = 95.0
estimated_savings = idle_power * 0.3 if cooling_factor > 0.9 else idle_power * 0.15
projected_efficiency_gain = None  # Unused placeholder

# Core logic inputs (only logic_core and pipeline_depth matter)
logic_core = 7
pipeline_depth = 4
redundancy_factor = 2  # Looks important but unused in final path
error_correction = True  # Distractor flag

# Decoy transformation chain
transformed_core = (logic_core + 3) * 0.5
adjusted_depth = pipeline_depth ** 2 - 1
placeholder_metric = transformed_core / adjusted_depth

# Real computation begins here
legacy_mode = False
scaling_modifier = 1.15 if legacy_mode else 1.0

# Conditional expression determining operational mode
mode_multiplier = 0.85 if voltage_level < 1.1 or temperature_coefficient < 0.85 else 1.0

# Auxiliary irrelevant formula simulating cache impact
cache_size_kb = 256
cache_associativity = 8
effective_cache_ratio = (cache_size_kb / 64) ** (1 / cache_associativity)

# Real efficiency formula embedded among distractions
def calculate_efficiency(core_count, depth):
    # Step 1: Base computation
    raw_score = core_count * (depth ** 2)
    
    # Step 2: Apply scaling modifier (depends on legacy_mode)
    scaled_score = raw_score * scaling_modifier
    
    # Step 3: Mode penalty/bonus
    adjusted_score = scaled_score * mode_multiplier
    
    # Step 4: Modular adjustment based on redundancy (but redundancy_factor not used)
    mod_adjusted = adjusted_score % (core_count + 1)
    
    # Step 5: Add constant offset derived from base_frequency (only last digit matters)
    frequency_digit = base_frequency % 10
    final_raw = mod_adjusted + frequency_digit
    
    # Step 6: Apply logarithmic compression if over threshold
    if final_raw > 20:
        final_raw = math.log(final_raw) * 10
    
    # Step 7: Round to nearest integer
    return int(round(final_raw))

# Spurious intermediate calculations (dead code paths)
candidate_configs = []
for i in range(3):
    candidate_configs.append({
        'id': i,
        'score': (logic_core * 2 + i) % 7,
        'valid': False
    })

# Another decoy function that is never called
def analyze_pipeline_stages(stages):
    total_risk = 0
    for s in range(stages):
        total_risk += s * (s + 1) / (temperature_coefficient + s)
    return total_risk / stages if stages > 0 else 0

# Critical statement: this is where the answer is determined
throughput = calculate_efficiency(logic_core, pipeline_depth)

# Output result as required
print(f"Target result: {throughput}")