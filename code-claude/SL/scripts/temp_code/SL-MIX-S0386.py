import itertools

def analyze_packet_headers(headers):
    """Analyzes packet headers for diagnostic purposes."""
    priority_levels = {'HIGH': 3, 'MEDIUM': 2, 'LOW': 1}
    total_priority = 0
    for header in headers:
        if 'priority' in header:
            total_priority += priority_levels.get(header['priority'], 0)
        if 'encrypted' in header and header['encrypted']:
            total_priority += 2
    return total_priority * 0.75  # Scaling factor

def calculate_bandwidth_overhead(data_size, protocol_type):
    """Calculate bandwidth overhead based on protocol."""
    protocol_overhead = {
        'TCP': 0.12,
        'UDP': 0.08,
        'HTTP': 0.15,
        'HTTPS': 0.18
    }
    
    base_overhead = protocol_overhead.get(protocol_type, 0.1)
    return data_size * base_overhead

def calculate_effective_throughput(packet_data, noise_factor):
    """Calculate the effective network throughput."""
    # Extract relevant data
    raw_data = packet_data['payload_size']
    protocol = packet_data['protocol']
    
    # Distractor calculations
    latency_ms = packet_data.get('latency', 30) * 2
    jitter = sum([abs(x-20) for x in packet_data.get('jitter_samples', [20, 21, 19])])
    
    # More distractors
    retransmission_count = 0
    for status in packet_data.get('transmission_status', ['OK', 'OK']):
        if status != 'OK':
            retransmission_count += 1
    
    # Calculate base throughput
    base_throughput = raw_data * 8  # Convert bytes to bits
    
    # Apply overhead reduction
    if noise_factor > 5:
        # This condition is never met with our input
        overhead = calculate_bandwidth_overhead(raw_data, 'HTTPS')
        effective_throughput = base_throughput - (overhead * 8)
    else:
        overhead = calculate_bandwidth_overhead(raw_data, protocol)
        effective_throughput = base_throughput - (overhead * 8)
    
    # Apply packet loss adjustment
    packet_loss = packet_data.get('packet_loss', 0.05)
    if packet_loss > 0.1:
        effective_throughput *= (1 - packet_loss * 2)
    else:
        effective_throughput *= (1 - packet_loss)
    
    # Misleading calculations that don't affect the result
    signal_strength = packet_data.get('signal_strength', -65)
    if signal_strength < -70:
        signal_quality = 'poor'
    elif signal_strength < -60:
        signal_quality = 'fair'
    else:
        signal_quality = 'good'
    
    # Apply noise factor (key calculation)
    noise_adjustment = 1.0
    if noise_factor < 3:
        noise_adjustment = 0.95
    elif noise_factor < 5:
        noise_adjustment = 0.9
    
    # Final throughput calculation
    return round(effective_throughput * noise_adjustment, 2)

# Network monitoring simulation
primary_interfaces = ['eth0', 'eth1', 'wlan0']
backup_interfaces = ['eth2', 'wlan1']

# Distractor - generate all possible interface combinations
all_interface_combinations = list(itertools.product(primary_interfaces, backup_interfaces))

# Distractor - analyze interface pairs
pair_scores = {}
for primary, backup in all_interface_combinations:
    pair_scores[(primary, backup)] = len(primary) + len(backup)

# Actual meaningful data
packet_data = {
    'payload_size': 1500,  # bytes
    'protocol': 'TCP',
    'latency': 25,  # ms
    'jitter_samples': [18, 22, 19, 21],
    'packet_loss': 0.03,
    'signal_strength': -58,
    'transmission_status': ['OK', 'OK', 'ERROR', 'OK'],
    'headers': [
        {'id': 1, 'priority': 'HIGH', 'encrypted': True},
        {'id': 2, 'priority': 'MEDIUM', 'encrypted': False},
        {'id': 3, 'priority': 'LOW', 'encrypted': False}
    ]
}

# More distractors
header_priority = analyze_packet_headers(packet_data['headers'])
packet_efficiency = 1 - (packet_data['packet_loss'] / 2)

# Slicing operation distractor
interface_slice = primary_interfaces[1:] + backup_interfaces[:1]

# The noise factor affects throughput calculation
noise_factor = 4

# The key calculation we're interested in
network_throughput = calculate_effective_throughput(packet_data, noise_factor)

# Additional distractor calculations that happen after our target variable
expected_throughput = packet_data['payload_size'] * 8 * 0.85  # Theoretical max
throughput_ratio = network_throughput / expected_throughput if expected_throughput > 0 else 0

print(f"Interface pairs analyzed: {len(all_interface_combinations)}")
print(f"Header priority score: {header_priority}")
print(f"Packet efficiency: {packet_efficiency}")
print(f"Result: {network_throughput}")