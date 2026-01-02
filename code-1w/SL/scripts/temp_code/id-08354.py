import math

# Irrelevant helper function (decoy)
def compute_entropy(values):
    total = 0
    for v in values:
        if v > 0:
            total -= v * math.log(v)
    return total

# Unused data structure (red herring)
legacy_system_weights = {
    'latency': 0.1,
    'throughput': 0.3,
    'jitter': 0.05,
    'bandwidth': 0.2
}

# Simulated sensor readings (mostly irrelevant)
sensor_log = [
    {'time': 1, 'temp': 22.1, 'vibration': 3.4},
    {'time': 2, 'temp': 23.5, 'vibration': 3.7},
    {'time': 3, 'temp': 21.9, 'vibration': 2.9}
]

# Core performance metrics (some are used, others distract)
metrics = {
    'response_time_avg': 150,
    'error_rate': 0.02,
    'concurrent_users': 1024,
    'cache_hit_ratio': 0.88,
    'peak_memory_mb': 512,
    'disk_io_ops': 200,  # Distractor
    'network_latency_ms': 45  # Not directly used
}

# Benchmark configuration with mixed relevance
benchmark_data = {
    'base_threshold': 100,
    'user_scale_factor': 1.05,
    'penalty_rate': 0.1,
    'grace_multiplier': 1.2,
    'decay_constant': 0.9,
    'target_throughput': 1000
}

# Auxiliary calculation using unused variables (misleading path)
temp_fluctuation = 0
for entry in sensor_log:
    temp_fluctuation += entry['temp']
temp_fluctuation /= len(sensor_log)
adjusted_vibration = sum(e['vibration'] for e in sensor_log) / len(sensor_log)

# Fake transformation (dead code path)
transformed_weights = {}
for k, v in legacy_system_weights.items():
    transformed_weights[k + '_norm'] = v ** 0.5

# Real logic begins here — subtle and buried among noise
def assess_response_efficiency(rt, threshold):
    if rt < threshold:
        return 100
    elif rt < threshold * 1.5:
        return 75
    elif rt < threshold * 2:
        return 50
    else:
        return 25

# Hidden dependency: uses only specific fields
def calculate_user_load_score(users):
    if users >= 2048:
        return 100
    elif users >= 1024:
        return 85  # This executes
    elif users >= 512:
        return 60
    else:
        return 30

# Cache efficiency scoring
def evaluate_cache_health(hit_ratio):
    return int(hit_ratio * 100)

# Composite evaluation (only this matters)
def evaluate_performance(met, config):
    base = config['base_threshold']
    rt = met['response_time_avg']
    
    # Step 1: Response efficiency
    score1 = assess_response_efficiency(rt, base)
    
    # Step 2: User load handling
    score2 = calculate_user_load_score(met['concurrent_users'])
    
    # Step 3: Cache effectiveness
    score3 = evaluate_cache_health(met['cache_hit_ratio'])
    
    # Step 4: Apply graceful degradation model
    raw_total = score1 + score2 + score3
    decayed = raw_total * config['decay_constant']
    
    # Step 5: Final adjustment using grace multiplier (only applied if error rate acceptable)
    if met['error_rate'] <= 0.05:
        decayed *= config['grace_multiplier']  # Triggers
    
    # Step 6: Normalize to integer score
    final = int(decayed)
    
    # Irrelevant rounding artifact (distractor)
    floating_artifact = round(decayed, 3)
    
    # Dead code branch (never reached due to structure)
    if met.get('disk_io_ops', 0) > 300:
        final += 10
    
    return final

# Execution point of interest
final_score = evaluate_performance(metrics, benchmark_data)

# Output required format
print(f"Result: {final_score}")