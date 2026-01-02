def analyze_component(x, y, z):
    # Irrelevant trigonometric distraction
    import math
    noise = math.sin(x) + math.cos(y) * z
    if x < 0:
        return 0
    temp = (x ^ y) & z
    return temp if temp > 5 else temp * 2

# Dead function - never called
def deprecated_metric(a, b):
    return (a + b) // 2

# Unused constants - red herrings
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30.5
DEBUG_MODE = True

# Simulated system metrics with mixed types
current_state = {
    'cpu_load': 78,
    'memory_usage': 45,
    'disk_iops': 120,
    'network_latency_ms': 23,
    'thermal_throttle': False
}

# Additional irrelevant data structure
diagnostic_log = [
    {'event': 'boot', 'code': 0},
    {'event': 'check', 'code': 1},
    {'event': 'error', 'code': -99}  # decoy error code
]

# Core processing function with conditional expressions
status_flag = 'active' if current_state['cpu_load'] < 80 else 'throttled'

# Misleading accumulation
running_total = 0
for i in range(5):
    running_total += i * current_state['disk_iops'] // 10
    if running_total > 100:
        break

# Distractor: unused dictionary operations
shadow_copy = current_state.copy()
shadow_copy.update({'cached': True})
shadow_copy.pop('thermal_throttle', None)

# Benchmark data that actually matters
benchmark_data = [
    {'module': 'A', 'result': 85, 'weight': 0.4},
    {'module': 'B', 'result': 92, 'weight': 0.3},
    {'module': 'C', 'result': 78, 'weight': 0.3}
]

# Real logic buried among distractions
def calculate_weighted_average(data):
    total = 0.0
    weight_sum = 0.0
    for entry in data:
        total += entry['result'] * entry['weight']
        weight_sum += entry['weight']
    return total / weight_sum if weight_sum > 0 else 0

# Bit manipulation decoy chain
bit_probe = 0xABC
bit_probe ^= 0x123
bit_probe &= ~0xFF0
probe_result = bit_probe << 2

# Conditional expression mix
adjustment_factor = 1.1 if status_flag == 'active' else 0.9

# Secondary metric - looks important but isn't final
interim_score = calculate_weighted_average(benchmark_data)

# Red herring: early exit check that doesn't trigger
if interim_score < 50:
    final_score = -1
else:
    # Key computation path
    normalized = interim_score / 100.0
    bonus = 5 if normalized >= 0.85 else 0
    
    # Final calculation using dictionary lookup and conditional expression
    performance_tier = 'high' if normalized > 0.8 else 'medium' if normalized > 0.6 else 'low'
    tier_multiplier = {'high': 1.2, 'medium': 1.0, 'low': 0.8}.get(performance_tier, 1.0)
    
    # The actual answer derivation
    raw_value = normalized * tier_multiplier * 100 + bonus
    
    # Additional distraction: unused transformation
    inverted_curve = [100 - x['result'] for x in benchmark_data if x['result'] < 80]
    
    # Final score assignment - this is the target
    final_score = int(raw_value * 10 + 0.5) / 10.0  # Round to 1 decimal place

# Execution point of interest
calculate_performance = calculate_weighted_average
final_score = calculate_performance(benchmark_data)

# But wait - we reassign it later in a less obvious block
if 'network_latency_ms' in current_state:
    base = calculate_performance(benchmark_data)
    adjusted = base * adjustment_factor
    final_score = round(adjusted + analyze_component(7, 3, 2), 1)

print(f"Target result: {final_score}")