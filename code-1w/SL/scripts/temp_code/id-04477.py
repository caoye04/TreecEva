from collections import defaultdict, Counter
import math

# Irrelevant helper function (decoy)
def analyze_pressure_levels(data):
    return sum(x ** 2 for x in data if x > 5)

# Misleading precomputed constant (red herring)
BASE_ENERGY_QUOTIENT = 3.14159 * (2 ** 16)

# Simulate sensor readings - irrelevant but looks important
def generate_sensor_array(size):
    result = []
    for i in range(size):
        result.append((i * 7 + 11) % 101)
    return result

# Unused transformation map (dead code path)
sensor_map = {
    k: (k * k + 3 * k + 1) % 100 for k in range(20)
}

# Core logic disguised among distractions
def evaluate_phase_shift(x):
    if x <= 0:
        return 0
    shift = 0
    while x & 1 == 0:
        x >>= 1
        shift += 1
    return shift

# Another decoy function that's never called
def compute_entropy(seq):
    freqs = Counter(seq)
    total = len(seq)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Critical recursive function with distractor parameters
def calculate_thermal_output(level, depth=0, accumulator=None):
    if accumulator is None:
        accumulator = defaultdict(int)
    
    # Distractor: update unused tracking
    accumulator['calls'] += 1
    accumulator['total_depth'] += depth
    
    if level <= 1:
        return 1
    
    # Real computation mixed with noise
    primary = calculate_thermal_output(level - 1, depth + 1, accumulator)
    secondary = calculate_thermal_output(level - 2, depth + 1, accumulator) if level > 2 else 0
    
    # Key calculation embedded here
    raw_value = primary + secondary
    
    # Apply bit manipulation relevant to final answer
    adjusted = raw_value ^ (level << 1)
    
    # More irrelevant operations
    accumulator['max_val'] = max(accumulator['max_val'], adjusted)
    
    return adjusted

# Pre-initialize unrelated list (distractor)
irrelevant_sequence = [evaluate_phase_shift(n) for n in range(15)]

# Fake data processing chain
temp_data = generate_sensor_array(10)
processed = [x for x in temp_data if x % 3 != 0]
summary_stats = {"sum": sum(processed), "len": len(processed)}

# Conditional expression with meaningful outcome buried inside
logic_threshold = 7 if len(irrelevant_sequence) > 10 else 5

# The key statement - answer depends on this execution
temperature_cache = {}
thermal_capacity = calculate_thermal_output(logic_threshold)

# Extra misleading assignment (looks like output but isn't)
final_diagnostics = {
    "score": BASE_ENERGY_QUOTIENT,
    "readings": summary_stats,
    "phase_shifts": irrelevant_sequence[-3:]
}

# Correct output format
print(f"Result: {thermal_capacity}")