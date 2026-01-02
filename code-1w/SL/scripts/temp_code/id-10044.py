import math

# Simulated system health monitoring metrics
temperature_readings = [72, 68, 73, 75, 69, 70, 74, 71]
humidity_levels = [45, 50, 52, 48, 55, 53, 49, 51]
cpu_usage = [25, 30, 35, 40, 45, 50, 55, 60]
memory_usage = [1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0, 3.3]  # in GB

disk_latency_ms = [12, 15, 11, 14, 13, 16, 10, 17]
network_iops = [200, 210, 195, 220, 205, 190, 215, 225]

# Irrelevant diagnostic logs (distractor data)
system_logs = ['OK', 'WARNING', 'OK', 'OK', 'CRITICAL', 'OK', 'ERROR', 'OK']
uptime_days = [12, 3, 45, 22, 7, 90, 14, 6]

# Benchmark thresholds (used in logic)
default_thresholds = {
    'temp': (65, 75),
    'humidity': (40, 60),
    'cpu': 50,
    'memory': 3.0,
    'latency': 15
}

# Auxiliary function - looks relevant but used minimally
def normalize(value, min_val, max_val):
    if value <= min_val:
        return 0
    if value >= max_val:
        return 1
    return (value - min_val) / (max_val - min_val)

# Decoy function - never called
def analyze_trend(data):
    trend_score = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += 1
        elif data[i] < data[i-1]:
            trend_score -= 1
    return abs(trend_score)

# Unused helper
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Core evaluation function
def evaluate_performance(metrics, benchmark_data):
    score = 0
    penalties = 0
    
    temp_in_range = [1 if default_thresholds['temp'][0] <= t <= default_thresholds['temp'][1] else 0 for t in temperature_readings]
    humidity_ok = all(default_thresholds['humidity'][0] <= h <= default_thresholds['humidity'][1] for h in humidity_levels)
    
    # Key slicing operation on cpu usage
    recent_cpu = cpu_usage[-4:]  # last 4 readings
    high_cpu_count = sum(1 for c in recent_cpu if c > default_thresholds['cpu'])
    
    # Memory trend analysis (only some used)
    increasing_memory = sum(1 for i in range(1, len(memory_usage)) if memory_usage[i] > memory_usage[i-1])
    
    # Latency check with dictionary lookup
    latency_issues = 0
    for lat in disk_latency_ms:
        if lat > default_thresholds['latency']:
            latency_issues += 1
    
    # Simulated weight adjustments (distractor block)
    weights = {
        'temp_stability': 0.2,
        'cpu_burst': 0.15,
        'memory_growth': 0.1,
        'latency_spike': 0.25,
        'network_jitter': 0.3  # unused
    }
    
    # Primary scoring logic
    score += sum(temp_in_range) * 10  # 10 points per stable temp reading
    
    if not humidity_ok:
        penalties += 15
    
    score += (4 - high_cpu_count) * 12  # reward fewer high CPU instances
    
    # Memory penalty only if growing consistently
    if increasing_memory > 5:
        penalties += 10
    
    # Critical latency penalty
    if latency_issues > 2:
        penalties += 25
    
    # Distractor: fake fusion calculation
    synthetic_index = 0
    for i in range(len(cpu_usage)):
        synthetic_index += cpu_usage[i] * (memory_usage[i] / (disk_latency_ms[i] + 1))
    synthetic_index = int(synthetic_index % 100)
    
    # Final adjustment using dictionary-based mapping
    adjustment_map = {0: 5, 1: 3, 2: 0, 3: -2, 4: -5, 5: -8, 6: -10, 7: -15}
    time_index = len(temperature_readings) % 8
    fallback_adjustment = adjustment_map.get(time_index, 0)
    
    # Actual result computation
    raw_result = score - penalties
    final_score = raw_result + fallback_adjustment + synthetic_index // 10
    
    # Dead code path (never reached due to structure)
    if False:
        backup_system = [x * 2 for x in network_iops]
        final_score = sum(backup_system) // 100
    
    return final_score

# Execution point of interest
metrics = {'cpu': cpu_usage, 'mem': memory_usage}
benchmark_data = default_thresholds
final_score = evaluate_performance(metrics, benchmark_data)

# Print result as required
print(f"Result: {final_score}")