def preprocess_data(raw):
    # Irrelevant preprocessing steps (dead code path)
    temp = [x * 0.95 for x in raw if x > 10]
    normalized = [max(0, x - 5) for x in raw]
    return normalized

# Simulated sensor readings (some relevant, some not)
sensor_readings = [23, 45, 12, 67, 89, 34, 78]

# Misleading intermediate aggregation (distractor)
avg_reading = sum(sensor_readings) / len(sensor_readings)
peak_reading = max(sensor_readings)
reading_variance = sum((x - avg_reading) ** 2 for x in sensor_readings)

# Unused transformation chain (red herring)
filtered_readings = [x for x in sensor_readings if x % 2 == 1]
decayed_values = [x * (0.5 ** i) for i, x in enumerate(filtered_readings)]

# Core health metrics (only this matters)
health_metrics = {
    'core_temp': 72,
    'voltage': 3.3,
    'cycles': 1024,
    'flags': 0b1010
}

# System load with bit-level indicators
system_load = {
    'cpu_usage': 78,
    'memory_pressure': 4,
    'io_queue': 15,
    'status_flag': 0b1100
}

# Decoy function that looks important but is never called
def compute_stress_score(metrics):
    score = 0
    score += metrics.get('core_temp', 0) * 1.1
    score ^= int(metrics.get('voltage', 0) * 100)
    score -= metrics.get('cycles', 0) // 256
    return score % 1000

# Real processing function
def analyze_status(metrics, load):
    # Step 1: extract core values
    temp = metrics['core_temp']
    cycles = metrics['cycles']
    flag_combined = metrics['flags'] & load['status_flag']  # bitwise AND of flags
    
    # Step 2: derive base diagnostic
    base_diag = temp + (cycles >> 8)  # cycles / 256
    
    # Step 3: apply flag logic
    if flag_combined & 0b1000:  # check third bit
        base_diag *= 2
    elif flag_combined & 0b0100:
        base_diag += 20
    
    # Step 4: memory pressure adjustment
    mem_adj = load['memory_pressure'] * 5
    base_diag -= mem_adj
    
    # Step 5: cpu/io interaction
    throughput = load['cpu_usage'] + load['io_queue']
    if throughput > 100:
        base_diag -= 15
    else:
        base_diag += 10
    
    # Step 6: final XOR obfuscation (deterministic)
    final_key = 0xAB
    result = base_diag ^ final_key
    
    # Step 7: dictionary-based mapping (lookup only affects specific range)
    correction_map = {185: 200, 195: 190, 205: 210, 215: 220}
    if result in correction_map:
        result = correction_map[result]
    
    # Step 8: final adjustment based on voltage side-channel (unused field!)
    # Note: 'voltage' is in metrics but intentionally not used here — distraction
    return result

# Execute main logic
processed = preprocess_data(sensor_readings)  # irrelevant call
snapshot = {'readings': processed, 'timestamp': 12345}  # decoy structure

# Critical execution point
final_diagnostic = analyze_status(health_metrics, system_load)

# Output result
print(f"Target result: {final_diagnostic}")