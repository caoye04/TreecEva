import math

# Simulated system performance analyzer with distractors
def analyze_component_health(reading, threshold_map):
    # Irrelevant health check with decoy logic
    if reading < threshold_map['low']:
        return 'critical'
    elif reading > threshold_map['high']:
        return 'optimal'
    else:
        return 'stable'

# Dead function - never called but looks important
def legacy_calibrate(values, factor=1.05):
    adjusted = []
    for v in values:
        if v > 100:
            adjusted.append(v * factor - 10)
        else:
            adjusted.append(v + 5)
    return [x * 0.9 for x in adjusted]

# Unused complex transformation
def fourier_approximation(sequence):
    result = 0
    for k in range(len(sequence)):
        angle = 2 * math.pi * k / len(sequence)
        result += sequence[k] * (math.cos(angle) - math.sin(angle))
    return round(result, 3)

# Core metric processor - actually used
def compute_derived_metrics(raw_data):
    temp_series = raw_data.get('temperatures', [])
    cycle_counts = raw_data.get('cycles', [])
    
    # Distractor variables
    avg_temp = sum(temp_series) / len(temp_series) if temp_series else 0
    max_cycle = max(cycle_counts) if cycle_counts else 0
    decay_factor = 0.87
    penalty_rate = 0.03 * avg_temp
    
    # Real computation embedded within noise
    base_score = 0
    for i, t in enumerate(temp_series):
        if i % 2 == 0 and t < 75:
            base_score += 12
        elif t >= 85:
            base_score -= 5
    
    # This part is irrelevant
    diagnostics = {}
    for idx in range(3):
        key = f'diag_{idx}'
        diagnostics[key] = (idx + 1) * math.pow(1.5, idx)
    
    # Actual signal: harmonic adjustment based on cycle stability
    variation = 0
    for j in range(1, len(cycle_counts)):
        variation += abs(cycle_counts[j] - cycle_counts[j-1])
    stability_bonus = 100 / (1 + variation * 0.02) if variation > 0 else 100
    
    return {
        'base': base_score,
        'stability': stability_bonus,
        'phantom_metric': sum(diagnostics.values())  # unused
    }

# Bit manipulation red herring
def obfuscate_key(n):
    n = ((n << 3) & 0xffffffff) | (n >> 29)
    n ^= 0xdeadbeef
    n = (n * 0x6d4d + 0x10) & 0xffffffff
    return n % 1000

# Main evaluation function - this is where the answer comes from
def evaluate_performance(log, config):
    # Massive distraction block
    security_flags = {
        'encrypted': True,
        'checksum': 0xa1b2c3d4,
        'version': '2.1.9',
        'nonce': obfuscate_key(len(log['cycles']))
    }
    
    # Nested conditional decoys
    if security_flags['version'].startswith('2'):
        if security_flags['encrypted']:
            for _ in range(2):
                security_flags['checksum'] ^= 0xfeed
    
    # Real work hidden in middle
    derived = compute_derived_metrics(log)
    
    # Multiple assignment distraction
    base, stability, phantom = derived['base'], derived['stability'], derived['phantom_metric']
    
    # Critical path: score computed here
    raw_score = base * config['weight_a'] + stability * config['weight_b']
    
    # Red herring transformations
    normalized = (raw_score - 50) * 1.8 + 32  # looks like temperature conversion
    capped = min(normalized, 95.5)
    adjusted = math.floor(capped * 100) / 100
    
    # Final computation - this is what matters
    final_modifier = config['threshold'] > 70 and len(log['temperatures']) > 5
    final_score = int(raw_score + (5 if final_modifier else -10))
    
    # Dead code path
    if final_score < 0:
        fallback = 0
        for bit in range(8):
            fallback |= (1 << bit)
        final_score = fallback
        
    return final_score

# Global decoy state
system_globals = {
    'uptime': 86400,
    'users_active': 127,
    'peak_load': 98.7,
    'last_reset': '2023-09-01'
}

# Execution begins here
if __name__ == '__main__':
    # Input data setup
    metrics_log = {
        'temperatures': [68, 72, 70, 88, 76, 69],
        'cycles': [100, 102, 101, 105, 103, 104],
        'timestamp': '2023-09-05T10:30:00Z'
    }
    
    baseline_config = {
        'weight_a': 2.5,
        'weight_b': 0.75,
        'threshold': 72
    }
    
    # Trigger the actual computation
    final_score = evaluate_performance(metrics_log, baseline_config)
    
    # Print required output
    print(f"Result: {final_score}")