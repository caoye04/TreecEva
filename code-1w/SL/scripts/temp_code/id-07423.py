from itertools import combinations

# System configuration parameters
def calculate_redundant_channels():
    primary_channels = {0, 1, 2, 3, 4}
    backup_channels = {3, 4, 5, 6}
    
    # Identify overlapping channels that can serve as mutual backups
    redundant_pool = primary_channels & backup_channels
    
    # Generate all possible dual-channel pairs from the redundant pool
    channel_pairs = list(combinations(redundant_pool, 2))
    
    # Filter pairs where sum of indices provides sufficient bandwidth
    sufficient_bandwidth = []
    for pair in channel_pairs:
        if sum(pair) >= 5:
            sufficient_bandwidth.append(pair)
    
    # Validate against deployment constraints (must not include channel 4 if paired with low index)
    valid_combinations = []
    for pair in sufficient_bandwidth:
        if not (4 in pair and min(pair) < 2):
            valid_combinations.append(pair)
    
    result = len(valid_combinations)
    print(f"Result: {result}")

calculate_redundant_channels()