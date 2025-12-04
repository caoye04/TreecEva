from collections import Counter, defaultdict

def analyze_connection_metrics(raw_data, threshold=75):
    # Process irrelevant metrics
    redundant_stats = defaultdict(int)
    for entry in raw_data:
        if entry % 3 == 0:
            redundant_stats['divisible_by_3'] += 1
        if entry % 5 == 0:
            redundant_stats['divisible_by_5'] += 1
    
    # This analysis is not used in the main calculation
    outlier_count = sum(1 for x in raw_data if x > threshold * 2)
    return {'metrics': redundant_stats, 'outliers': outlier_count}

def calculate_network_score(packet_loss, latency_data, connection_data):
    # Start with base reliability score
    base_score = 100
    
    # Apply packet loss penalty (this is relevant)
    packet_loss_factor = min(packet_loss * 1.5, 50)
    adjusted_score = base_score - packet_loss_factor
    
    # Process latency data (mostly distraction)
    latency_penalty = 0
    for server, values in latency_data.items():
        if server.startswith('east'):
            # This condition is never true with our data
            latency_penalty += sum(values) / len(values) if values else 0
    
    # Process connection data (the key calculation)
    connection_factor = 0
    total_connections = sum(connection_data.values())
    
    if total_connections > 0:
        success_rate = connection_data.get('successful', 0) / total_connections
        # This is the most important factor
        connection_factor = success_rate * 25
    
    # Calculate theoretical maximum (distraction)
    theoretical_max = base_score - (packet_loss * 0.8) + (1.0 * 25)
    
    # Apply bitwise operations for signal quality (distraction)
    signal_quality = 0b1010 & 0b1100
    signal_boost = signal_quality >> 1
    
    # Final calculation (only some factors matter)
    reliability = adjusted_score + connection_factor - (signal_boost * 0.5)
    
    # Round to avoid floating point issues
    return round(reliability, 2)

# Main execution starts here
packet_data = [12, 45, 67, 23, 89, 34, 56, 78, 90]
metrics_analysis = analyze_connection_metrics(packet_data)

# Packet loss percentage (this matters)
packet_loss = 8.5

# Server latency measurements (mostly distraction)
latency_stats = {
    'west-01': [45, 48, 52, 47, 49],
    'central-01': [30, 32, 35, 31, 29],
    'west-02': [50, 53, 48, 51, 49]
}

# Process string data for server names (distraction)
server_names = "west-01,central-01,west-02,south-01"
active_servers = server_names.split(',')
server_count = len(active_servers)

# Apply string operations (distraction)
encoded_servers = [s.replace('-', '_').upper() for s in active_servers]

# Track connection history (this matters)
connection_history = Counter()
connection_history['successful'] = 85
connection_history['failed'] = 12
connection_history['timeout'] = 3

# Calculate network reliability score
network_reliability = calculate_network_score(packet_loss, latency_stats, connection_history)

# Process additional metrics (distraction)
uptime_percentage = 99.7
traffic_volume = 1240
network_load = (traffic_volume / 1000) * (100 - uptime_percentage)

# Calculate alternative reliability (distraction)
alt_reliability = (uptime_percentage / 100) * (100 - packet_loss)

print(f"Network reliability score: {network_reliability}")