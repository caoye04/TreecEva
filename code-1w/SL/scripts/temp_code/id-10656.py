from collections import defaultdict
import math

# Simulated system telemetry (irrelevant data)
telemetry_log = [
    {'timestamp': 1001, 'temp': 45.2, 'voltage': 3.7},
    {'timestamp': 1002, 'temp': 46.1, 'voltage': 3.6},
    {'timestamp': 1003, 'temp': 44.8, 'voltage': 3.8}
]

total_power_usage = 0
for log in telemetry_log:
    total_power_usage += log['voltage'] * 0.5  # Irrelevant calculation

# Sensor calibration offset (red herring)
calibration_factor = 0.987
sensor_drift = sum([log['temp'] for log in telemetry_log]) * (1 - calibration_factor)

# Core performance evaluation logic
metrics = {
    'latency': 120,
    'throughput': 850,
    'consistency': 92,
    'error_rate': 4,
    'jitter': 18
}

weights = defaultdict(float, {
    'latency': 0.3,
    'throughput': 0.25,
    'consistency': 0.2,
    'error_rate': -0.15,  # Penalty weight
    'jitter': -0.1
})

# Decoy normalization function (never called)
def normalize(value, max_val):
    return value / max_val if max_val != 0 else 0

# Auxiliary transformation (distractor)
transformed_metrics = [
    (k, v ** 0.5 if v > 0 else 0) for k, v in metrics.items()
]

# False alternative scoring method (unused)
alternative_score = 0
for val in metrics.values():
    if val > 50:
        alternative_score += math.log(val)

# Real processing pipeline
def adjust_for_latency(value, base_latency=100):
    return value * (base_latency / (value + 10)) if value else 0

def apply_penalty(score, rate, severity=2):
    return score - (rate ** 1.5) / 10 * severity

def calculate_performance(metrs, wts):
    base_score = 0
    adjusted_metrics = {}
    
    # Step 1: Adjust latency
    adj_latency = adjust_for_latency(metrs['latency'])
    adjusted_metrics['latency'] = adj_latency
    
    # Step 2: Boost throughput with diminishing returns
    throughput_mod = metrs['throughput'] * (1 - 1 / (1 + metrs['throughput']/1000))
    adjusted_metrics['throughput'] = throughput_mod
    
    # Step 3: Consistency bonus
    consistency_bonus = metrs['consistency'] * 0.1
    adjusted_metrics['consistency'] = metrs['consistency'] + consistency_bonus
    
    # Step 4: Apply penalties
    penalty_impact = apply_penalty(0, metrs['error_rate'], severity=3) + apply_penalty(0, metrs['jitter'], severity=1)
    
    # Step 5: Aggregate base components
    for key in ['latency', 'throughput', 'consistency']:
        if key in wts:
            base_score += adjusted_metrics[key] * wts[key]
    
    # Step 6: Add penalty contributions
    base_score += metrs['error_rate'] * wts['error_rate']
    base_score += metrs['jitter'] * wts['jitter']
    
    # Step 7: Final nonlinear adjustment
    final_adjusted = base_score * (1.1 - 0.05 * abs(penalty_impact))
    
    # Dead code branch (never executes due to logic)
    if False and 'debug' in metrs:
        print('Debug mode active')  # Unreachable
    
    # Misleading intermediate (looks important but unused)
    synthetic_index = sum([v**2 for v in adjusted_metrics.values()]) ** 0.5
    
    return round(final_adjusted, 4)

# Trigger computation
final_score = calculate_performance(metrics, weights)

# Additional red herring: Bit manipulation on irrelevant data
bit_fiddling = 0
for i in range(5):
    bit_fiddling ^= (i << 2) | (i >> 1)

# Output result as required
print(f"Result: {final_score}")