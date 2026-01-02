def analyze_phase_transitions(phases):
    entropy_log = {}
    for idx, (temp, pressure) in enumerate(phases):
        entropy = (temp ** 0.5) * (pressure / 100)
        entropy_log[f'step_{idx}'] = round(entropy, 3)
    
    # Distractor: irrelevant transformation
    normalized = [max(0, min(100, t + p % 7)) for t, p in phases]
    adjusted_phases = [(t * 1.1, p * 0.9) for t, p in phases if t > 200]
    
    # Dead code path (never used)
    def decoy_normalization(x):
        return x * 0.95 if x > 50 else x * 1.05
    
    return entropy_log

# Irrelevant auxiliary function
def compute_thermodynamic_potential(temp_seq):
    potential = 0
    for t in temp_seq:
        if t > 300:
            potential += t * 0.01
        elif t > 200:
            potential += t * 0.005
    return round(potential, 4)

# Core logic with distractors
thermal_phases = [
    (250, 980), (310, 1020), (190, 890), (420, 1100),
    (275, 960), (380, 1050), (210, 840)
]

status_flags = [True if t > 300 else False for t, p in thermal_phases]
flag_summary = {i: flag for i, flag in enumerate(status_flags)}

# Unused transformation
compressed = list(zip([t//10 for t, _ in thermal_phases], [p//100 for _, p in thermal_phases]))

# Real computation buried among distractions
phase_codes = []
for i, (t, p) in enumerate(thermal_phases):
    code = (i + 1) * (t % 50) - (p % 30)
    phase_codes.append(code)

# Conditional expression red herring
reference_value = 42.0 if len(thermal_phases) > 5 else 37.5
baseline = sum(t for t, p in thermal_phases) / len(thermal_phases)
offset_correction = reference_value if baseline > 273 else 0

# Key distracting dictionary operations
metrics = {
    'peak': max(t for t, p in thermal_phases),
    'stability': sum(1 for t, p in thermal_phases if 250 <= t <= 350),
    'extremes': [t for t, p in thermal_phases if t < 220 or t > 400]
}

# Another decoy structure
analysis_cache = {}
for tag, vals in metrics.items():
    if isinstance(vals, list):
        analysis_cache[tag] = sum(v ** 0.1 for v in vals)

# Actual relevant but obscured calculation
transition_weights = [
    (t * 0.7) + (p * 0.003) for i, (t, p) in enumerate(thermal_phases)
    if i % 2 == 0
]

# Critical function with multiple layers and distractions
def calculate_equilibrium(phases):
    total_impact = 0
    adjustment_factor = 0.85
    
    for i, (temp, pressure) in enumerate(phases):
        # Meaningful but non-obvious contribution
        base = temp * 0.01
        stress = pressure * 0.0002
        
        # Conditional expression that actually matters
        modifier = 1.25 if i % 3 == 0 else (0.9 if temp > 300 else 1.05)
        
        # Bit manipulation distraction (irrelevant)
        magic = (i << 2) ^ 5
        dummy_shift = magic >> 1
        
        # Real contribution mixed with noise
        contribution = (base + stress) * modifier
        total_impact += contribution
        
        # Dead conditional (looks important)
        if temp > 1000:
            total_impact *= 0.5  # Never executed
    
    # Final adjustment using unused variables to mislead
    unused_entropy = analyze_phase_transitions(phases)  # Called but result ignored
    final_boost = len(metrics['extremes']) * 0.5
    
    return int(round(total_impact + final_boost))

# Trigger execution
equilibrium_score = calculate_equilibrium(thermal_phases)
print(f"Result: {equilibrium_score}")