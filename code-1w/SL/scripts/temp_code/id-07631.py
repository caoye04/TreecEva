from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800]
cpu_loads = [0.78, 0.82, 0.91, 0.88, 0.95]
memory_usage = [0.65, 0.67, 0.71, 0.73, 0.76]
disk_reads = [230, 215, 240, 235, 250]
disk_writes = [120, 125, 130, 140, 145]

# Irrelevant sensor data (distractor)
temperature_readings = [23.4, 24.1, 22.9, 25.0, 24.5]  # °C
fan_speeds = [1200, 1250, 1180, 1300, 1280]  # RPM
voltage_levels = [3.31, 3.29, 3.32, 3.30, 3.31]  # V

# System thresholds and weights
system_thresholds = {
    'cpu_critical': 0.90,
    'memory_warning': 0.70,
    'load_weight': 0.6,
    'memory_weight': 0.4
}

# Legacy configuration (dead code path - distractor)
old_config = {
    'sampling_rate': 5,
    'buffer_size': 1024,
    'compression': 'lz4'
}

def analyze_temp_trend(readings):
    """Distractor function - not used in main logic"""
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return {'average': avg, 'variance': variance, 'alerts': 0}

def calculate_entropy(data):
    """Unused mathematical distraction"""
    total = sum(data)
    probabilities = [x / total for x in data if x > 0]
    return -sum(p * math.log2(p) for p in probabilities)

# Compute irrelevant metrics
temp_analysis = analyze_temp_trend(temperature_readings)
entropy_disk_reads = calculate_entropy(disk_reads)
entropy_disk_writes = calculate_entropy(disk_writes)

# Simulate network packets (irrelevant data structure)
network_packets = []
for i in range(len(timestamps)):
    pkt = {
        'ts': timestamps[i],
        'seq': i * 100,
        'size': 1500,
        'checksum': hex(i ^ 0xABCD),
        'flags': 'ACK' if i % 2 == 0 else 'SYN'
    }
    network_packets.append(pkt)

# Build log entries with relevant performance data
log_entries = []
for idx, (ts, cpu, mem) in enumerate(zip(timestamps, cpu_loads, memory_usage)):
    entry = {
        'timestamp': ts,
        'metrics': {
            'cpu': cpu,
            'memory': mem
        },
        'sequence': idx,
        'anomaly_score': 0.0
    }
    
    # Calculate temporary anomaly score (will be overridden)
    if cpu > system_thresholds['cpu_critical']:
        entry['anomaly_score'] = 0.8
    elif mem > system_thresholds['memory_warning']:
        entry['anomaly_score'] = 0.4
    else:
        entry['anomaly_score'] = 0.1
        
    # Add irrelevant field
    entry['sensor_id'] = f"SYS-{idx:03d}-VM"
    log_entries.append(entry)

# Distractor: unused aggregation
total_data_volume = sum(disk_reads) + sum(disk_writes)
avg_fan_speed = sum(fan_speeds) / len(fan_speeds)

# Real processing begins here
def evaluate_stability_trend(entries):
    """Assess stability based on consecutive threshold breaches"""
    cpu_breaches = 0
    mem_warnings = 0
    for e in entries:
        if e['metrics']['cpu'] > 0.85:
            cpu_breaches += 1
        if e['metrics']['memory'] > 0.70:
            mem_warnings += 1
    return cpu_breaches >= 3, mem_warnings >= 2

# Secondary metric calculation
growth_rate = (memory_usage[-1] - memory_usage[0]) / len(memory_usage)
system_aging_factor = math.exp(growth_rate * 10)

# Core diagnostic processor
def process_metrics(log_data, thresholds):
    # Extract time-series data
    cpu_list = [entry['metrics']['cpu'] for entry in log_data]
    mem_list = [entry['metrics']['memory'] for entry in log_data]
    
    # Initialize counters
    critical_count = 0
    warning_count = 0
    
    # Primary evaluation loop
    for i, cpu_val in enumerate(cpu_list):
        mem_val = mem_list[i]
        
        # Weighted risk score
        risk_score = (cpu_val * thresholds['load_weight'] + 
                     mem_val * thresholds['memory_weight'])
        
        if risk_score > 0.85:
            critical_count += 1
        elif risk_score > 0.75:
            warning_count += 1
    
    # Determine stability from separate function
    severe_cpu, elevated_mem = evaluate_stability_trend(log_data)
    
    # Apply complex diagnostic rules
    base_score = critical_count * 100 + warning_count * 10
    
    if severe_cpu and elevated_mem:
        base_score += 50
    elif severe_cpu:
        base_score += 20
    
    # Final adjustment using system aging
    adjusted_score = base_score * system_aging_factor
    
    # Additional distractor computation (unused)
    temporal_variance = sum(
        (cpu_list[i+1] - cpu_list[i])**2 
        for i in range(len(cpu_list)-1)
    )
    
    # Red herring normalization
    normalized = adjusted_score / (1 + math.log(1 + entropy_disk_reads))
    
    # Final diagnostic is rounded integer
    return int(round(normalized))

# Execute main processing step
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")