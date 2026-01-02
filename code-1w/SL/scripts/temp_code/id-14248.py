from itertools import compress

def optimize_bandwidth(channels, threshold):
    # Calculate signal quality for each channel
    signal_strength = [ch['power'] / (ch['noise'] + 1) for ch in channels]
    
    # Determine which channels exceed threshold
    valid_mask = [strength > threshold for strength in signal_strength]
    
    # Use conditional expression to select bandwidth: boost if valid
    optimized = [ch['base_bw'] * (2 if valid else 1) for ch, valid in zip(channels, valid_mask)]
    
    # Aggregate total optimized bandwidth
    total = sum(optimized)
    scaling_factor = 0.9 if sum(valid_mask) >= 3 else 1.0
    final_bandwidth = int(total * scaling_factor)
    
    # Irrelevant auxiliary variable (minimal distraction)
    debug_mode = False
    
    return final_bandwidth

# Define channel data
channels = [
    {'power': 8, 'noise': 2, 'base_bw': 50},
    {'power': 6, 'noise': 3, 'base_bw': 40},
    {'power': 9, 'noise': 1, 'base_bw': 60},
    {'power': 5, 'noise': 4, 'base_bw': 35},
    {'power': 7, 'noise': 2, 'base_bw': 55}
]
threshold = 2.0

result = optimize_bandwidth(channels, threshold)
print(f"Result: {result}")