def process_network_data(raw_packets, signal_strength=None):
    # Process incoming network packet data
    processed = []
    noise_factor = 0.15
    
    # Signal strength normalization (distractor)
    if signal_strength:
        normalized_signal = [s * (1 - noise_factor) for s in signal_strength]
        threshold = sum(normalized_signal) / len(normalized_signal)
    else:
        threshold = 0.75
    
    # Main packet processing
    for packet in raw_packets:
        if packet % 3 == 0 and packet % 5 == 0:
            # Special packet handling (distractor)
            processed.append(packet * 2)
        elif packet % 7 == 0:
            # Priority packets
            processed.append(packet // 2)
        else:
            # Normal packets
            processed.append(packet)
    
    return processed[::2]  # Return every other packet

def calculate_transmission_efficiency(packets, window_size=4):
    # Calculate network efficiency metrics
    if not packets:
        return 0
    
    total_efficiency = 0
    packet_windows = []
    
    # Create sliding windows (mostly distractor)
    for i in range(len(packets) - window_size + 1):
        window = packets[i:i+window_size]
        packet_windows.append(sum(window) / window_size)
    
    # Calculate base efficiency
    base_efficiency = sum(packets) / len(packets)
    
    # Apply bitwise operations to determine network congestion
    congestion_factor = 1
    for p in packets:
        if p & 0x0F > 8:  # Lower 4 bits
            congestion_factor = (congestion_factor * 0.95)
        elif p & 0xF0 > 128:  # Upper 4 bits (distractor)
            congestion_factor = (congestion_factor * 1.05)
    
    # This is what actually matters for the calculation
    key_metric = (base_efficiency * congestion_factor) % 100
    return key_metric

def analyze_error_patterns(error_data):
    # Analyze error patterns (mostly distractor)
    if not error_data:
        return []
        
    error_types = {'timeout': 0, 'corruption': 0, 'loss': 0}
    for error in error_data:
        if error < 0:
            error_types['timeout'] += 1
        elif error > 100:
            error_types['corruption'] += 1
        else:
            error_types['loss'] += abs(error - 50)
    
    # Return error frequencies - only loss matters
    return error_types['loss']

def calculate_final_metric(packet_data, error_rates):
    # Process initial data
    filtered_packets = process_network_data(packet_data)
    
    # Calculate primary metrics
    efficiency = calculate_transmission_efficiency(filtered_packets)
    error_impact = analyze_error_patterns(error_rates)
    
    # Generate misleading metrics (distractors)
    throughput = sum(filtered_packets) / max(1, len(filtered_packets))
    latency_estimate = min(filtered_packets) if filtered_packets else 0
    jitter = max(filtered_packets) - latency_estimate if filtered_packets else 0
    
    # Calculate network reliability score
    # The key calculation combines efficiency with error impact
    reliability_base = (efficiency - (error_impact * 0.01))
    
    # Apply logarithmic scaling (distractor)
    import math
    scaled_throughput = math.log10(max(10, throughput))
    
    # These operations look important but don't affect the final result
    if jitter > 50:
        reliability_factor = 0.85
    elif latency_estimate < 20:
        reliability_factor = 1.15
    else:
        reliability_factor = 1.0
    
    # Calculate final reliability score
    return round(reliability_base, 2)

# Network simulation data
packet_data = [24, 18, 36, 42, 15, 63, 21, 49, 56, 30]
error_rates = [45, 120, -5, 52, 48, 62]

# Calculate network performance metrics
throughput_estimate = sum(packet_data) / len(packet_data)
packet_loss_ratio = len([e for e in error_rates if 0 <= e <= 100]) / len(error_rates)

# This is the key calculation we're asked about
network_reliability = calculate_final_metric(packet_data, error_rates)

# Additional post-processing (distractor)
if network_reliability > 80:
    network_status = "Excellent"
elif network_reliability > 60:
    network_status = "Good"
elif network_reliability > 40:
    network_status = "Fair"
else:
    network_status = "Poor"

print(f"Network Analysis Complete")
print(f"Throughput: {throughput_estimate}")
print(f"Packet Loss: {packet_loss_ratio:.2f}")
print(f"Result: {network_reliability}")