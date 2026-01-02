from collections import defaultdict
import math

# Simulated sensor data processing for a distributed system health monitor
def collect_telemetry(nodes):
    raw_readings = []
    for node in nodes:
        temp = (hash(node) % 100) + 20
        latency = abs(hash(node[::-1]) % 50)
        cpu_load = (hash(node + 'cpu') % 100) / 100.0
        raw_readings.append({'id': node, 'temp': temp, 'latency': latency, 'cpu': cpu_load})
    return raw_readings

# Irrelevant helper - dead code path (decoy)
def encrypt_log(data):
    encrypted = ''
    for c in data:
        encrypted += chr((ord(c) + 3) % 128)
    return encrypted

# Misleading transformation - looks important but unused later
def compute_stress_score(readings):
    score = 0
    for r in readings:
        score += r['temp'] * r['latency'] * (r['cpu'] * 10)
    return score / len(readings)

# Data normalizer with red herring operations
def normalize_readings(readings):
    norm_data = []
    avg_temp = sum(r['temp'] for r in readings) / len(readings)
    max_latency = max(r['latency'] for r in readings)
    
    # Decoy statistical computation
    variance = sum((r['cpu'] - 0.5) ** 2 for r in readings) / len(readings)
    entropy_proxy = -sum(p * math.log(p + 1e-9) for p in [r['cpu'] for r in readings])
    
    for r in readings:
        normalized = {
            'node': r['id'],
            'thermal': (r['temp'] - avg_temp) / 10.0,
            'response': min(r['latency'] / max_latency, 1.0),
            'burden': r['cpu']
        }
        norm_data.append(normalized)
    return norm_data

# Core analysis function buried among distractions
def generate_health_vector(norm_readings):
    vector = []
    for entry in norm_readings:
        # Composite metric combining normalized values
        health_score = (entry['thermal'] * 0.3 + 
                       entry['response'] * 0.3 + 
                       entry['burden'] * 0.4)
        vector.append(round(health_score, 3))
    return vector

# Unused complex structure - distractor
class DiagnosticBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0.0] * size
        self.index = 0
    
    def push(self, val):
        self.buffer[self.index] = val
        self.index = (self.index + 1) % self.size

# Threshold configuration with irrelevant entries
def build_threshold_map():
    config = defaultdict(lambda: 0.5)
    config['critical'] = 0.8
    config['warning'] = 0.6
    config['optimal'] = 0.3
    # Red herring keys
    config['deprecated_mode'] = 0.1
    config['legacy_offset'] = 0.9
    config['dummy_guard'] = 0.0
    return config

# Main analyzer - key function in logical chain
def analyze_metrics(metrics, thresholds):
    count_critical = 0
    count_warning = 0
    total_adjustment = 0.0
    
    for m in metrics:
        if m > thresholds['critical']:
            count_critical += 1
            total_adjustment += m * 1.1
        elif m > thresholds['warning']:
            count_warning += 1
            total_adjustment += m * 0.8
        else:
            total_adjustment += m * 0.5
    
    # Complex formula with multiple logic steps
    base = count_critical * 100
    bonus = count_warning * 25
    penalty = int(sum(m > thresholds['optimal'] for m in metrics)) * 10
    adjustment_factor = abs(math.sin(total_adjustment)) * 100
    
    # Final diagnostic score calculation
    final_score = base + bonus - penalty + int(adjustment_factor)
    
    # Dead computation - looks like it modifies final_score but doesn't
    temp_shadow = final_score
    for _ in range(3):
        temp_shadow = (temp_shadow ^ 255) & 1023
    
    return final_score

# Entry point with decoy operations
if __name__ == '__main__':
    system_nodes = [
        'alpha-node', 'beta-router', 'gamma-store',
        'delta-cache', 'epsilon-db', 'zeta-proxy',
        'eta-broker', 'theta-queue'
    ]
    
    # Dead encryption call - irrelevant
    log_token = encrypt_log('system_init_001')
    
    # Real data pipeline
    telemetry = collect_telemetry(system_nodes)
    processed = normalize_readings(telemetry)
    health_vector = generate_health_vector(processed)
    threshold_map = build_threshold_map()
    
    # Key statement containing answer
    final_diagnostic = analyze_metrics(health_vector, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")
    
    # Additional distraction: unused buffer
    diag_buffer = DiagnosticBuffer(5)
    for v in health_vector[-5:]:
        diag_buffer.push(v * 100)
