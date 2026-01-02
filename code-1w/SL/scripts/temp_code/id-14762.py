import math

# Simulated system metrics (some relevant, some red herrings)
def collect_diagnostics():
    cpu_load = [0.78, 0.82, 0.75, 0.91, 0.88]
    memory_usage = [0.65, 0.71, 0.77, 0.83, 0.80]
    disk_io = [120, 150, 90, 200, 180]  # irrelevant
    network_latency = [45, 67, 52, 58, 73]  # partially misleading
    temperature_c = [67, 70, 72, 75, 73]  # decoy
    fan_speed_rpm = 2500  # irrelevant constant
    return {
        'cpu': cpu_load,
        'memory': memory_usage,
        'disk': disk_io,
        'latency': network_latency,
        'temp': temperature_c,
        'fan': fan_speed_rpm
    }

def preprocess_data(raw):
    # Normalize CPU and memory only; others are processed but unused
    normalized_cpu = [min(1.0, load * 1.2) for load in raw['cpu']]
    normalized_mem = [min(1.0, usage * 1.1) for usage in raw['memory']]
    
    # Distractor transformations
    smoothed_latency = [max(10, x - 5) for x in raw['latency']]
    adjusted_temp = [min(80, t + 2) for t in raw['temp']]
    
    # Create composite fake indicators
    risk_factor = sum([1 for t in adjusted_temp if t > 75]) * 0.1
    stability_score = 100 - len([x for x in smoothed_latency if x > 60])

    return {
        'processed_cpu': normalized_cpu,
        'processed_mem': normalized_mem,
        'risk': risk_factor,
        'stability': stability_score,
        'decoy_array': adjusted_temp  # never used
    }

def calculate_health_components(data):
    cpu_avg = sum(data['processed_cpu']) / len(data['processed_cpu'])
    mem_avg = sum(data['processed_mem']) / len(data['processed_mem'])
    
    # Fake components with plausible names
    efficiency_metric = cpu_avg * (1 - mem_avg)  # looks meaningful
    thermal_risk = data['risk'] * 0.5  # not actually used
    system_stability = data['stability'] / 100  # ignored later

    # Hidden correct path: harmonic mean of cpu and mem
    if cpu_avg + mem_avg == 0:
        health_base = 0
    else:
        health_base = 2 * cpu_avg * mem_avg / (cpu_avg + mem_avg)
    
    # Red herring branches
    if health_base > 1.0:
        health_base = 1.0
    elif health_base < 0:
        health_base = 0.1

    return {
        'core_health': health_base,
        'efficiency': efficiency_metric,
        'thermal': thermal_risk,
        'stability_val': system_stability
    }

def apply_weight_adjustments(components, base_weights):
    # Dynamic weight adjustment logic with dead branches
    temp_weights = base_weights.copy()
    
    core = components['core_health']
    eff = components['efficiency']
    
    if eff > 0.5:
        temp_weights['health'] += 0.1
        temp_weights['efficiency'] -= 0.1
    else:
        temp_weights['health'] -= 0.05  # this branch taken
    
    # Nonsensical corrections
    if components['thermal'] > 0.3:
        temp_weights['health'] *= 0.9
    
    # Irrelevant clamping
    for k in temp_weights:
        temp_weights[k] = max(0.05, min(0.9, temp_weights[k]))
    
    # Return adjusted but only one will be used
    return temp_weights

def evaluate_performance(metrics, weights):
    # Only core_health is used in final score
    health = metrics['core_health']
    
    # Distractor: unused calculations
    total_risk = metrics['thermal'] + (1 - metrics['stability_val'])
    performance_index = health * 100 + metrics['efficiency'] * 10
    
    # Final score is simply a scaled version of health
    final_score = int((1 - health) * 500)  # key result
    
    # Dead code path that looks important
    if final_score > 250:
        final_score -= 50
    elif final_score < 100:
        final_score += 20
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    raw_metrics = collect_diagnostics()
    cleaned = preprocess_data(raw_metrics)
    components = calculate_health_components(cleaned)
    
    # Base weights (only health matters in the end)
    weights = {'health': 0.6, 'efficiency': 0.25, 'thermal': 0.1, 'stability': 0.05}
    adjusted_weights = apply_weight_adjustments(components, weights)
    
    # Critical statement
    final_score = evaluate_performance(components, adjusted_weights)
    
    print(f"Result: {final_score}")