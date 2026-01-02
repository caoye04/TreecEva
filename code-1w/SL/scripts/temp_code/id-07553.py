from collections import defaultdict, Counter
import math

# Simulated system log analysis with heavy distractions
def analyze_component_health(metrics, bias_factor=1.3):
    score = 0
    decoy_accumulator = 0
    for k, v in metrics.items():
        if 'error' in k:
            score -= v * bias_factor
        elif 'warning' in k:
            score -= v * 0.5
        elif 'success' in k:
            score += max(v // 2, 1)
        decoy_accumulator += len(k)  # Irrelevant computation
    return score + 10

def compute_entropy(data):
    total = sum(data.values())
    entropy = 0
    for count in data.values():
        if count > 0:
            p = count / total
            entropy -= p * math.log2(p)
    return round(entropy, 3)

def generate_synthetic_trace(n):
    # Dead-end function: never actually used in final result
    trace = []
    for i in range(n):
        trace.append((i, (i**2 + 3*i + 7) % 19))
    return trace

def evaluate_stability_vector(vec):
    # Misleading function that looks important but isn't called
    magnitude = sum(x**2 for x in vec) ** 0.5
    normalized = [x / magnitude for x in vec]
    return sum(math.sin(x) for x in normalized)

def decode_signal_pattern(signal):
    # Distractor transformation
    decoded = 0
    for bit in signal:
        decoded = (decoded << 1) | bit
    return decoded ^ 0xFF  # Red herring operation

def aggregate_diagnostics(nodes):
    node_scores = defaultdict(int)
    temp_buffer = []
    
    for node_id, logs in nodes.items():
        errors = logs.get('errors', 0)
        warnings = logs.get('warnings', 0)
        uptime = logs.get('uptime', 0)
        
        # Relevant scoring logic
        if uptime > 1000:
            node_scores[node_id] += 5
        if errors == 0:
            node_scores[node_id] += 7
        elif errors < 5:
            node_scores[node_id] += 2
        
        if warnings == 0 and errors == 0:
            node_scores[node_id] += 3
        
        # Complex distraction
        checksum = 0
        for c in node_id:
            checksum ^= ord(c.lower())
        temp_buffer.append(checksum % 7)
    
    # Final aggregation
    base_sum = sum(node_scores.values())
    adjustment = len(temp_buffer) % 5  # Useless but looks meaningful
    return base_sum + adjustment

def process_metrics(log_entries, system_state):
    # Core function - computes final diagnostic score
    critical_flags = 0
    event_counter = Counter()
    intermediate_results = []
    
    for entry in log_entries:
        timestamp = entry['ts']
        code = entry['code']
        severity = entry['severity']
        
        event_counter[code] += 1
        
        if severity >= 4:
            critical_flags += 1
        
        # Early return red herring - never triggered in practice
        if timestamp < 1000:
            return -999
        
        # Accumulate intermediate transformations
        transformed = (code * severity) % 13
        intermediate_results.append(transformed)
    
    # Real logic branch
    base_score = 0
    for val in intermediate_results:
        if val > 7:
            base_score += val * 2
        else:
            base_score += val
    
    # Additional logic using system state
    mode_flag = system_state.get('mode', 0)
    if mode_flag == 3:
        base_score = int(base_score * 1.5)
    elif mode_flag == 7:
        base_score += 20
    
    # Final adjustment based on counter
    high_freq_events = sum(1 for cnt in event_counter.values() if cnt > 2)
    if high_freq_events >= 2:
        base_score += 15
    
    # Decoy finalization path
    decoy_value = 0
    for i, v in enumerate(intermediate_results):
        decoy_value ^= (v + i) % 256
    decoy_value = (decoy_value * 3) % 100  # Looks complex, unused
    
    # The actual answer
    final_diagnostic = base_score + critical_flags
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    # Simulated input data
    log_entries = [
        {'ts': 1500, 'code': 5, 'severity': 3},
        {'ts': 1501, 'code': 8, 'severity': 4},
        {'ts': 1502, 'code': 5, 'severity': 2},
        {'ts': 1503, 'code': 9, 'severity': 5},
        {'ts': 1504, 'code': 8, 'severity': 1},
        {'ts': 1505, 'code': 5, 'severity': 4},
        {'ts': 1506, 'code': 6, 'severity': 5}
    ]
    
    system_state = {
        'mode': 7,
        'version': '3.8.1',
        'debug': True,
        'buffer_size': 4096,
        'timeout': 30
    }
    
    # Irrelevant data structures
    performance_snapshot = {
        'cpu_load': [0.78, 0.81, 0.75, 0.92],
        'memory_gb': {'used': 14.2, 'total': 32.0},
        'disk_io': defaultdict(int, {'reads': 1200, 'writes': 800})
    }
    
    node_topology = {
        'node-alpha': {'errors': 0, 'warnings': 1, 'uptime': 1500},
        'node-beta': {'errors': 3, 'warnings': 0, 'uptime': 1200},
        'node-gamma': {'errors': 0, 'warnings': 0, 'uptime': 2000}
    }
    
    signal_stream = [1, 0, 1, 1, 0, 0, 1]
    
    # Meaningful distraction: multiple function calls that look important
    health_score = analyze_component_health({'error_count': 2, 'warning_count': 5})
    entropy = compute_entropy(Counter('ABRACADABRA'))
    trace_data = generate_synthetic_trace(10)
    
    # Real computation path
    final_diagnostic = process_metrics(log_entries, system_state)
    
    # Additional dead-end operations
    stability = 0
    for i in range(3):
        stability += evaluate_stability_vector([1, 2, 3, i])
    
    decoded_sig = decode_signal_pattern(signal_stream)
    
    # Aggregate diagnostics (looks important but not part of final answer)
    cluster_health = aggregate_diagnostics(node_topology)
