import math

# Simulated system performance metrics with noise
def generate_diagnostics():
    return {
        'latency_ms': 142.5,
        'throughput_ops': 8900,
        'error_rate': 0.0034,
        'cpu_load': 0.78,
        'memory_mb': 4210
    }

# Irrelevant helper: converts MB to GB (unused later)
def mb_to_gb(mb):
    return mb / 1024.0

# Dead function: looks useful but never called
def analyze_stability(logs):
    critical_failures = 0
    for entry in logs:
        if 'CRITICAL' in entry and 'timeout' in entry:
            critical_failures += 1
    return critical_failures > 5

# Decoy metric transformation (never used)
temp_offset = 27.3
temp_reading = [round(math.sin(i * 0.5) * 10 + temp_offset, 2) for i in range(5)]
adjusted_temps = [t for t in temp_reading if t > 25]

# Baseline configuration (used)
baseline = {
    'latency_ms': 150.0,
    'throughput_ops': 8000,
    'error_rate': 0.005,
    'cpu_load': 0.80
}

# Real processing begins
metrics = generate_diagnostics()

# Bit manipulation red herring
flag_register = 0b110101
mask = 0b1111
masked_flags = flag_register & mask
is_valid_mode = (masked_flags ^ 0b1010) == 0b0111

# Set operations with distraction
expected_keys = {'latency_ms', 'throughput_ops', 'error_rate', 'cpu_load', 'disk_io'}
actual_keys = set(metrics.keys())
missing = expected_keys - actual_keys
extra = actual_keys - expected_keys
has_all_required = 'disk_io' not in missing  # False, but not critical

# Conditional expression with misleading branch
degraded = metrics['latency_ms'] > baseline['latency_ms']
boost_applied = True if degraded else False
if boost_applied:
    metrics['throughput_ops'] *= 1.1  # minor compensation

# Slicing operation on irrelevant data
history = list(range(100, 200, 2))
history_slice = history[10:15]  # [120, 122, 124, 126, 128]
peak_window = max(history_slice) if len(history_slice) > 0 else 0

# Core logic hidden among distractions
def compute_efficiency_ratio(m, b):
    latency_factor = b['latency_ms'] / m['latency_ms']
    throughput_factor = m['throughput_ops'] / b['throughput_ops']
    error_penalty = 1 - (m['error_rate'] / b['error_rate'])
    load_bonus = 0.9 if m['cpu_load'] < b['cpu_load'] else 0.95
    return (latency_factor * throughput_factor + error_penalty) * load_bonus

# Secondary scoring with decoy
consistency_check = all(
    isinstance(v, (int, float)) and v >= 0 
    for v in metrics.values()
)

# Unused recursive red herring
def calculate_depth(n):
    if n <= 1:
        return 1
    return calculate_depth(n-1) + calculate_depth(n-2)

fib_result = calculate_depth(6)  # 13, unused

# Main evaluation function
def evaluate_performance(met, base):
    # Step 1: efficiency score
    efficiency = compute_efficiency_ratio(met, base)
    
    # Step 2: compliance check (boolean logic)
    compliant_latency = met['latency_ms'] <= base['latency_ms']
    compliant_error = met['error_rate'] <= base['error_rate']
    meets_standard = compliant_latency and compliant_error
    
    # Step 3: conditional adjustment using ternary
core_score = efficiency * 100
    adjustment = 15 if meets_standard else -10
    
    # Step 4: final composition
    raw_final = core_score + adjustment
    
    # Step 5: apply bit-conditioned modifier (distractor logic)
    modifier_flag = (masked_flags & 0b1001) == 0b1001  # False
    if modifier_flag and 'disk_io' not in met:
        raw_final *= 1.05
    
    # Step 6: round to nearest integer
    return int(round(raw_final))

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)

# Output result
print(f"Result: {final_score}")