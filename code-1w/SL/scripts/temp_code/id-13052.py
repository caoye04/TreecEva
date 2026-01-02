import math

# Simulated network node diagnostic system
def analyze_node_health(signal_strength, latency, packet_loss, threshold=0.75):
    normalized_signal = max(0.0, min(1.0, (signal_strength + 85) / 15))  # dBm to normalized
    normalized_latency = 1 - (min(latency, 500) / 500)
    normalized_packet_loss = 1 - packet_loss

    health_score = (
        0.4 * normalized_signal +
        0.35 * normalized_latency +
        0.25 * normalized_packet_loss
    )

    return health_score > threshold, health_score

# Irrelevant helper - distractor
def calculate_snr(power, noise):
    if noise == 0:
        return float('inf')
    return 10 * math.log10(abs(power) / abs(noise))

# Signal processing chain - partially relevant, partially red herring
def process_frequency_bands(raw_spectrum):
    filtered = [x for x in raw_spectrum if 2.4 <= x <= 2.5 or 5.0 <= x <= 5.9]
    bands = {
        'wifi_2g': [f for f in filtered if 2.4 <= f <= 2.5],
        'wifi_5g': [f for f in filtered if 5.0 <= f <= 5.9]
    }
    
    # Distractor computation
    interference_density = sum(len(bands[b]) for b in bands) / (len(filtered) + 1e-8)
    
    # Real metric used later
    return len(bands['wifi_2g']) + len(bands['wifi_5g'])

# Data transformation with decoy logic
def extract_metadata(header_string):
    parts = header_string.split('|')
    metadata = {}
    for p in parts:
        if '=' in p:
            k, v = p.split('=', 1)
            metadata[k.strip()] = v.strip()
    
    # Decoy values
    checksum = sum(ord(c) for c in header_string) % 256
    entropy = -sum((header_string.count(c)/len(header_string)) * math.log2(header_string.count(c)/len(header_string)) 
                   for c in set(header_string))
    
    # Only this is actually used
    return int(metadata.get('node_id', 0))

# Complex state tracker - mixes relevant and irrelevant logic
class NetworkStateTracker:
    def __init__(self):
        self.history = []
        self.anomalies = 0
        self.last_reset = None
    
    def update(self, reading, timestamp):
        self.history.append((reading, timestamp))
        if reading < 0.3:
            self.anomalies += 1
        
        # Fake normalization
        fake_norm = sum(math.sin(x[0]) for x in self.history[-10:])
        return fake_norm

# Bit manipulation for channel encoding - red herring with one real usage
def encode_channel_id(node_id, cluster):
    combined = (node_id & 0xFF) << 8 | (cluster & 0xFF)
    masked = combined ^ 0xAA55
    parity = bin(combined).count('1') % 2
    final = (masked << 1) | parity
    return final & 0xFFFF

# Main aggregation function - key logic buried in noise
def aggregate_metrics(nodes):
    tracker = NetworkStateTracker()
    total_weighted_score = 0.0
    active_count = 0
    signal_outliers = 0
    
    # Real data path
    base_spectrum = [2.3, 2.45, 2.48, 5.1, 5.3, 5.8, 6.0]
    total_bandwidth = process_frequency_bands(base_spectrum)
    
    # Irrelevant list comprehensions and slicing
    dummy_headers = [
        f'node={i}|status=up|voltage=3.{i}' for i in range(5)
    ]
    recent_headers = dummy_headers[-3:]
    id_sum = sum(extract_metadata(h) for h in recent_headers)
    
    # Core processing loop with distractions
    for node_data in nodes:
        raw_header = node_data.get('header', 'node=0|status=unknown')
        extracted_id = extract_metadata(raw_header)
        
        health_flag, health_score = analyze_node_health(
            node_data['signal'],
            node_data['latency'],
            node_data['packet_loss']
        )
        
        # Encode but don't use - distraction
        encoded = encode_channel_id(extracted_id, node_data['cluster'])
        encoded_str = ''.join(chr(encoded >> (8*i) & 0xFF) for i in range(2))  # meaningless
        
        # Actual contribution
        weight = 1.0
        if node_data['priority']:
            weight *= 1.25
        
        tracker.update(health_score, node_data['timestamp'])
        total_weighted_score += health_score * weight
        active_count += weight
        
        # Outlier detection - unused metric
        if abs(node_data['signal'] + 80) > 15:
            signal_outliers += 1
    
    # Distractor: bitwise operation with no impact
    final_key = total_bandwidth ^ id_sum
    final_key = (final_key << 1) ^ (final_key >> 2)
    
    # The actual answer computation - hard to isolate
    base_average = total_weighted_score / (active_count + 1e-8)
    adjustment = (tracker.anomalies * 0.05)
    final_diagnostic = int((base_average - adjustment) * 10000)
    
    return final_diagnostic

# Input data - realistic structure with extra fields
network_nodes = [
    {
        'header': 'node=12|status=up|version=2.1',
        'signal': -78,
        'latency': 45,
        'packet_loss': 0.02,
        'priority': True,
        'cluster': 3,
        'timestamp': 1712345600
    },
    {
        'header': 'node=15|status=up|version=2.3',
        'signal': -82,
        'latency': 120,
        'packet_loss': 0.05,
        'priority': False,
        'cluster': 3,
        'timestamp': 1712345605
    },
    {
        'header': 'node=21|status=degraded|version=1.8',
        'signal': -91,
        'latency': 300,
        'packet_loss': 0.12,
        'priority': True,
        'cluster': 7,
        'timestamp': 1712345610
    },
    {
        'header': 'node=8|status=up|version=2.0',
        'signal': -76,
        'latency': 80,
        'packet_loss': 0.03,
        'priority': False,
        'cluster': 7,
        'timestamp': 1712345615
    }
]

# Execution point of interest
final_diagnostic = aggregate_metrics(network_nodes)
print(f"Result: {final_diagnostic}")