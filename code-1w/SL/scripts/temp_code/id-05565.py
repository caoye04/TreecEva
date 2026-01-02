from collections import defaultdict, Counter
import itertools

# Simulated network packet data with diagnostic tags
def generate_packet_stream():
    return [
        {'src': '192.168.1.10', 'dst': '10.0.0.5', 'size': 1460, 'flags': ['SYN', 'ACK'], 'latency_ms': 12.5},
        {'src': '10.0.0.5', 'dst': '192.168.1.10', 'size': 892, 'flags': ['ACK'], 'latency_ms': 11.8},
        {'src': '192.168.1.10', 'dst': '10.0.0.5', 'size': 1460, 'flags': ['PSH', 'ACK'], 'latency_ms': 13.1},
        {'src': '10.0.0.5', 'dst': '192.168.1.10', 'size': 256, 'flags': ['ACK'], 'latency_ms': 12.0},
        {'src': '192.168.1.10', 'dst': '10.0.0.5', 'size': 1460, 'flags': ['FIN', 'ACK'], 'latency_ms': 14.2},
        {'src': '10.0.0.5', 'dst': '192.168.1.10', 'size': 1460, 'flags': ['PSH', 'ACK'], 'latency_ms': 13.8},
        {'src': '192.168.1.10', 'dst': '10.0.0.5', 'size': 512, 'flags': ['ACK'], 'latency_ms': 12.9}
    ]

# Misleading function - looks important but unused in final calculation
def compute_entropy(data):
    freq = Counter(data)
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actually logarithmic
    return round(entropy, 3)

# Auxiliary processing with red herring outputs
def extract_flow_signatures(packets):
    signatures = []
    for pkt in packets:
        sig = f"{pkt['src'].split('.')[2]}-{pkt['dst'].split('.')[2]}-{len(pkt['flags'])}"
        signatures.append(sig)
    return signatures

# Distractor: builds irrelevant stats
def analyze_throughput(packets):
    total_bytes = sum(p['size'] for p in packets)
    avg_size = total_bytes / len(packets)
    burst_window = [p['size'] for p in packets if p['size'] > 1000]
    throughput_mbps = (total_bytes * 8) / (packets[-1].get('latency_ms', 1) * 1000)
    return {
        'total_gb': total_bytes / 1e6,
        'avg_pkt_size': avg_size,
        'burst_count': len(burst_window),
        'estimated_mbps': throughput_mbps
    }

# Core state tracker with meaningful and distracting elements
class NetworkStateTracker:
    def __init__(self):
        self.handshakes = 0
        self.active_flows = set()
        self.flag_sequence = []
        self.latency_buffer = []
        self._debug_trace = []  # Dead storage - never used later
        self.misfire_count = 0  # Distractor counter

    def update(self, packet):
        flow_key = (packet['src'], packet['dst'])
        
        # Real logic: track handshake patterns
        if 'SYN' in packet['flags'] and 'ACK' in packet['flags']:
            self.handshakes += 1
        
        # Real: collect flag sequences for analysis
        self.flag_sequence.append(len(packet['flags']))
        
        # Real: accumulate latency samples
        self.latency_buffer.append(packet['latency_ms'])
        
        # Distractor: complex but unused flow tracking
        if len(packet['src']) % 2 == 0 and packet['size'] < 1000:
            self.misfire_count += 1
        
        # Distractor: fake debug logging
        self._debug_trace.append(f"FLOW:{flow_key[0].split('.')[1]}")

# Real data transformation pipeline
def aggregate_metrics(state_log, health_index):
    # Latency base metric
    raw_latencies = state_log.latency_buffer
    base_score = sum(raw_latencies) / len(raw_latencies)
    
    # Handshake weighting
    handshake_factor = max(1, state_log.handshakes * 2)
    
    # Flag sequence complexity using itertools
    runs = 1
    for a, b in itertools.pairwise(state_log.flag_sequence):
        if a != b:
            runs += 1
    
    # Real composite formula
    intermediate = (base_score * handshake_factor) + (runs * 0.75)
    
    # Health index adjustment (simulated constant)
    adjusted = intermediate * (health_index / 100.0)
    
    # Final non-linear transformation
    final_value = int((adjusted ** 2) / 2.5) + 17
    
    # DEAD CODE PATH: masked by similar-looking logic
    if False:
        backup = sum(state_log.flag_sequence) * health_index
        final_value = backup % 1000
    
    return final_value

# Irrelevant utility - looks like it's preparing something
def build_routing_matrix(packets):
    matrix = defaultdict(lambda: defaultdict(int))
    for p in packets:
        src_segment = p['src'].split('.')[1]
        dst_segment = p['dst'].split('.')[1]
        matrix[src_segment][dst_segment] += 1
    return dict(matrix)

# Simulated health sensor (constant for determinism)
def get_system_health_diagnostics():
    return 94  # Simulated stable system

# Main execution flow
if __name__ == '__main__':
    # Step 1: Generate packet stream
    packets = generate_packet_stream()
    
    # Step 2: Extract useless signature list (distractor)
    signatures = extract_flow_signatures(packets)
    
    # Step 3: Compute meaningless entropy (red herring)
    size_entropy = compute_entropy([p['size'] for p in packets])
    
    # Step 4: Analyze throughput (collected but unused)
    throughput_stats = analyze_throughput(packets)
    
    # Step 5: Build routing matrix (never used)
    routing_table = build_routing_matrix(packets)
    
    # Step 6: Initialize tracker
    tracker = NetworkStateTracker()
    
    # Step 7: Process each packet (core relevant loop)
    for pkt in packets:
        tracker.update(pkt)
    
    # Step 8: Get system health (simple lookup)
    system_health = get_system_health_diagnostics()
    
    # Step 9: Log irrelevant counters (misfire_count is distracting)
    debug_info = {
        'flows_tracked': len(tracker.active_flows),
        'misfires': tracker.misfire_count,
        'signatures_generated': len(signatures)
    }
    
    # Step 10: CORE CALCULATION - this determines the answer
    final_diagnostic = aggregate_metrics(tracker, system_health)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")