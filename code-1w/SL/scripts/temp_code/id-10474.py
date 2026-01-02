from collections import defaultdict

# System configuration parameters (many are decoys)
max_nodes = 15
topology_refresh_rate = 0.25
packet_size_kb = 64
redundancy_factor = 2.0
signal_strength = 97
jitter_threshold = 12.4

# Irrelevant network metrics (distractors)
current_dropped_packets = 3
historical_avg_latency = [14, 16, 13, 15, 17]
node_health_status = {f'node_{i}': 'active' for i in range(max_nodes)}

def analyze_signal_integrity(signal_data):
    # Unused function - red herring
    return sum(v ** 0.5 for v in signal_data if v > 10)

def calculate_theoretical_capacity(channels):
    # Misleading intermediate function - never called
    total = 0
    for c in channels:
        if c['bandwidth'] > 40:
            total += c['bandwidth'] * 1.5
    return total

# Real data structures used in computation
event_queue = [("start", 1), ("pause", 5), ("resume", 8)]
latency_map = defaultdict(lambda: 10)
for i, val in enumerate([5, 8, 6, 9, 7]):
    latency_map[f'router_{i}'] = val

channels = [
    {'id': 'chA', 'bandwidth': 120, 'status': 'active', 'load': 0.65},
    {'id': 'chB', 'bandwidth': 85, 'status': 'standby', 'load': 0.4},
    {'id': 'chC', 'bandwidth': 150, 'status': 'active', 'load': 0.75},
    {'id': 'chD', 'bandwidth': 95, 'status': 'active', 'load': 0.55},
]

# Decoy transformation (unused but looks important)
transformed_channels = []
for ch in channels:
    normalized_score = (ch['bandwidth'] / (ch['load'] + 1)) * 0.85
    transformed_channels.append({'id': ch['id'], 'score': normalized_score})

# Simulated diagnostic trace (irrelevant computations)
diagnostic_log = []
for event, timestamp in event_queue:
    if event == "start":
        diagnostic_log.append(f"Initiated at {timestamp}")
    elif event == "pause":
        diagnostic_log.append(f"Paused at {timestamp}s")

# Core logic disguised among distractions
def evaluate_channel_efficiency(bandwidth, load_factor, base_latency):
    efficiency = (bandwidth * (1 - load_factor)) - base_latency
    return efficiency if efficiency > 0 else 0.0

def optimize_transmission(active_channels, latency_profile):
    total_efficiency = 0.0
    active_count = 0
    
    # Key logic with nested conditions and dictionary lookups
    for channel in active_channels:
        if channel['status'] != 'active':
            continue
            
        router_key = f"router_{active_count % 5}"
        base_latency = latency_profile[router_key]
        
        # Conditional expression used
        load_factor = channel['load'] if channel['load'] > 0 else 0.1
        
        efficiency = evaluate_channel_efficiency(
            channel['bandwidth'], 
            load_factor, 
            base_latency
        )
        
        # Only accumulate if efficiency meets threshold
        if efficiency >= 20:
            total_efficiency += efficiency
        
        active_count += 1
    
    # Final adjustment using conditional expression
    scaling_factor = 1.25 if total_efficiency > 100 else 1.1
    adjusted_bandwidth = total_efficiency * scaling_factor
    
    # Critical result variable
    return int(adjusted_bandwidth)

# Execution point of interest
final_bandwidth = optimize_transmission(channels, latency_map)

# Print required output
print(f"Target result: {final_bandwidth}")