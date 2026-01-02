def process_sensor_readings(raw_readings):
    # Irrelevant transformation: normalize timestamps (not used later)
    normalized_times = [t % 86400 for t in raw_readings.get('timestamps', [])]
    
    # Distractor: unused noise filter
    filtered_noise = [val for val in raw_readings.get('signal', []) if val > -50]
    
    # Relevant: extract diagnostic codes
    diagnostics = raw_readings.get('diagnostics', [])
    severity_levels = []
    for code in diagnostics:
        if code.startswith('ERR'):
            severity_levels.append(3)
        elif code.startswith('WARN'):
            severity_levels.append(2)
        elif code.startswith('INFO'):
            severity_levels.append(1)
        else:
            severity_levels.append(0)
    
    return severity_levels


def calculate_efficiency_curve(rpm_values, load_factor=1.0):
    # Dead function: never called in execution path
    efficiency = []
    for rpm in rpm_values:
        if rpm < 1000:
            efficiency.append(0.1 * load_factor)
        elif rpm < 3000:
            efficiency.append(0.6 * load_factor)
        else:
            efficiency.append(0.4 * load_factor)
    return efficiency

# Misleading global computation
baseline_offset = sum([i * 2 for i in range(10)]) // 3  # Result: 30, unused

# Decoy data structure
maintenance_log = {
    'last_service': '2023-10-05',
    'parts_replaced': ['filter', 'gasket'],
    'downtime_hours': 2.5,
    'cost_usd': 1200
}

turbine_data = {
    'sensor_id': 'TURB-7X',
    'readings': [105, 110, 98, 115, 120, 90],
    'status_flags': ['OK', 'OK', 'LOW', 'OK', 'HIGH', 'CRIT'],
    'diagnostics': ['INFO_001', 'ERR_101', 'WARN_205', 'ERR_101', 'INFO_001', 'CRIT_900']
}

threshold_map = {
    'critical': 90,
    'warning': 100,
    'normal': 110
}

# Unused recursive helper (red herring)
def binary_weight_tree(depth, acc=1):
    if depth <= 0:
        return acc
    return binary_weight_tree(depth - 1, acc * 2) + binary_weight_tree(depth - 1, acc * 3)

# Key processing function with distractors
def aggregate_metrics(data, thresholds):
    readings = data['readings']
    flags = data['status_flags']
    codes = data['diagnostics']
    
    # Distractor: irrelevant string processing
    code_parts = [c.split('_') for c in codes]
    indices = {part[0]: idx for idx, part in enumerate(code_parts) if len(part) > 0}
    
    # Real logic begins here
    critical_count = 0
    error_sum = 0
    
    # List comprehension with filtering (relevant)
    high_priority_codes = [c for c in codes if c.startswith('ERR') or c.startswith('CRIT')]
    
    # Enumerate with conditional mutation
    for i, flag in enumerate(flags):
        if flag == 'CRIT':
            critical_count += 1
            error_sum += readings[i] * 2
        elif flag == 'HIGH':
            error_sum += readings[i]
    
    # Bitwise manipulation red herring (unused)
    masked_result = 0
    for val in readings:
        masked_result ^= (val & 0xF) | 0x10
    
    # Real aggregation using multiple concepts
    base_score = sum(readings) // len(readings)
    penalty = critical_count * 100
    
    # Complex condition with short-circuiting and comparisons
    adjustment = len(high_priority_codes) > 2 and len(set(codes)) < 5 \
        and (base_score < thresholds['warning'] or penalty > 0) \
        and not (base_score >= thresholds['normal'])
    
    final_score = base_score - penalty
    
    # Final branching with decoy variable
    temp_debug = final_score + baseline_offset  # Never used
    
    if adjustment:
        final_score -= 50
    
    # Key assignment: this is the answer
    final_diagnostic = abs(final_score) + len(high_priority_codes)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Extract severity from another source (distractor)
raw_input = {
    'timestamps': [1696500000 + i*60 for i in range(5)],
    'signal': [20.1, -30.5, 45.0, -60.2, 10.3],
    'diagnostics': ['INFO_001', 'WARN_205', 'ERR_101', 'WARN_205', 'INFO_001']
}

_ = process_sensor_readings(raw_input)

# Execution point of interest
final_diagnostic = aggregate_metrics(turbine_data, threshold_map)