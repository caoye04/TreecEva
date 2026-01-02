import math

# Simulated system metrics with irrelevant and relevant components
def collect_diagnostics():
    cpu_load = [0.78, 0.82, 0.91, 0.85, 0.77]
    mem_usage = [0.65, 0.70, 0.76, 0.72, 0.68]
    disk_io = [120, 135, 110, 140, 130]  # Irrelevant in final calculation
    network_latency = [45, 52, 48, 55, 50]  # Also irrelevant
    return {
        'cpu': cpu_load,
        'memory': mem_usage,
        'disk': disk_io,
        'network': network_latency
    }

def preprocess_data(raw):
    # Normalize CPU and memory only; others are ignored
    normalized_cpu = [round(x ** 0.5, 3) for x in raw['cpu']]
    normalized_mem = [round(math.log(1 + x), 3) for x in raw['memory']]
    
    # Distractor: complex transformation on irrelevant data
    obfuscated_disk = [((x << 2) ^ 0xA) % 100 for x in raw['disk']]
    encrypted_net = list(map(lambda x: (x + 10) * 2, raw['network']))

    # Return all including distractors
    return {
        'processed_cpu': normalized_cpu,
        'processed_mem': normalized_mem,
        'junk_disk_feat': obfuscated_disk,
        'junk_net_enc': encrypted_net
    }

def compute_health_index(data):
    cpu_vals = data['processed_cpu']
    mem_vals = data['processed_mem']
    
    # Real computation path
    avg_cpu = sum(cpu_vals) / len(cpu_vals)
    avg_mem = sum(mem_vals) / len(mem_vals)
    
    # Early return red herring - never triggered in this case
    if avg_cpu > 1.0:
        return 0.0  # Impossible due to sqrt normalization
    
    # Health index formula
    health = (avg_cpu * 0.6) + (avg_mem * 0.4)
    return round(health, 4)

def apply_correction_factor(h):
    # Conditional expression distraction
    factor = 1.05 if h < 0.8 else (0.98 if h > 0.9 else 1.0)
    adjusted = h * factor
    
    # Dead code path - unused correction variants
    def super_complex_correction(x):
        return (x ** 2 + math.sin(x)) / (1 + math.exp(-x))
    
    return adjusted

def evaluate_security_risk(data):
    # Completely independent and irrelevant function
    risk_score = 0
    for val in data['junk_disk_feat']:
        if val > 80:
            risk_score += 1
    return min(risk_score, 5) * 10  # Max 50, not used anywhere

def evaluate_performance(metrics, weights):
    # Core logic
    base_health = compute_health_index(metrics)
    corrected_health = apply_correction_factor(base_health)
    
    # Weighted evaluation using slicing and lambda
    recent_cpu = metrics['processed_cpu'][-3:]  # Last three values
    volatility = sum([(recent_cpu[i] - recent_cpu[i-1])**2 for i in range(1, len(recent_cpu))])
    
    # Distractor: unused advanced volatility model
    advanced_volatility_model = lambda seq: sum([abs(seq[i] - seq[i-2]) for i in range(2, len(seq))])
    
    # Final score calculation
    stability_bonus = 10 if volatility < 0.05 else 5
    final_score = (corrected_health * weights['health'] + stability_bonus) * 100
    
    # Unused variables as distractions
    theoretical_max = 150
    debug_trace = f"Final components: health={corrected_health}, bonus={stability_bonus}"
    
    return int(final_score)

# Main execution flow
raw_system_data = collect_diagnostics()
processed_metrics = preprocess_data(raw_system_data)
evaluation_weights = {
    'health': 7.5,  # Critical weight
    'security': 2.0,  # Unused
    'legacy': 1.0   # Unused
}

# Trigger the key statement
final_score = evaluate_performance(processed_metrics, evaluation_weights)
print(f"Result: {final_score}")