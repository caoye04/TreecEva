import math

# Simulated sensor data and system flags
temperature_readings = [23.5, 24.1, 25.0, 26.3, 22.7, 27.8, 28.0, 24.5]
pressure_levels = {"p1": 101.3, "p2": 102.1, "p3": 98.7, "p4": 100.5}

# Irrelevant auxiliary data (distraction)
aux_data = {'calibration': [1.01, 0.99, 1.02], 'offsets': (0.5, 0.3, 0.7), 'mode': 'test'}
baseline_stats = {'mean_temp': 25.0, 'std_dev': 1.8}

# System health logs with timestamps and status codes
health_logs = [
    {'time': 100, 'code': 200, 'temp': 23.5},
    {'time': 105, 'code': 201, 'temp': 24.1},
    {'time': 110, 'code': 500, 'temp': 27.8},
    {'time': 115, 'code': 200, 'temp': 22.7},
    {'time': 120, 'code': 404, 'temp': 28.0},
    {'time': 125, 'code': 200, 'temp': 24.5}
]

# System flags indicating various states (bitmask-style)
system_flags = 0b1101  # Meaning: Ready | Active | !Fault | Optimized

# Decoy function – never called (dead code path)
def legacy_calibrate(data):
    return [x * 0.98 for x in data]

# Auxiliary transformation (partially relevant, partially distracting)
normalized_temps = [round(t - baseline_stats['mean_temp'], 2) for t in temperature_readings]
high_pressure_zones = {k: v for k, v in pressure_levels.items() if v > 100.0}

def detect_anomalies(logs):
    anomalies = []
    for entry in logs:
        if entry['code'] >= 400:
            anomalies.append(entry['time'])
    return set(anomalies)

# Misleading intermediate calculation (looks important but unused later)
avg_normalized_temp = sum(normalized_temps) / len(normalized_temps)

# Complex flag interpretation with bit checks
is_ready = bool(system_flags & 0b1000)
is_active = bool(system_flags & 0b0100)
has_fault = not bool(system_flags & 0b0010)  # Inverted logic
is_optimized = bool(system_flags & 0b0001)

# Red herring: spurious data transformation
transformed_logs = [
    {**entry, 'alert': entry['code'] != 200} for entry in health_logs
]

# Another decoy function (unused)
def compute_entropy(values):
    total = 0
    for v in values:
        if v > 0:
            total -= v * math.log(v)
    return total

# Core analysis logic with nested conditions and data structure interactions
def analyze_system_state(logs, flags):
    # Step 1: Extract successful operations
    success_count = 0
    temp_sum = 0.0
    critical_events = 0
    recent_codes = []
    
    for log in logs:
        code = log['code']
        temp = log['temp']
        
        if code == 200:
            success_count += 1
            temp_sum += temp
        elif code >= 500:
            critical_events += 1
        
        if log['time'] >= 110:
            recent_codes.append(code)
    
    # Step 2: Compute average from filtered data
    avg_temp_during_success = temp_sum / success_count if success_count > 0 else 0.0
    
    # Step 3: Analyze recent behavior
    recent_issue_ratio = len([c for c in recent_codes if c != 200]) / len(recent_codes) if recent_codes else 0
    
    # Step 4: Derive diagnostic score using multiple factors
    base_score = success_count * 10
    penalty = critical_events * 25 + int(recent_issue_ratio * 100)
    
    # Step 5: Apply flag-based modifiers
    modifier = 1.0
    if is_ready:
        modifier *= 1.1
    if not has_fault:
        modifier *= 1.05
    if is_optimized:
        modifier *= 1.2
    
    # Step 6: Final computation
    raw_diagnostic = base_score - penalty
    adjusted_diagnostic = raw_diagnostic * modifier
    
    # Step 7: Round to nearest integer (key step)
    final_diagnostic = int(round(adjusted_diagnostic))
    
    # Irrelevant post-processing (distractor)
    binary_rep = bin(final_diagnostic)
    hex_rep = hex(final_diagnostic)
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_system_state(health_logs, system_flags)

# Print result as required
print(f"Target result: {final_diagnostic}")