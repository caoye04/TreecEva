from collections import defaultdict, Counter

# Simulated environmental bio-sensor network data processing
def collect_samples(raw_streams, duration):
    samples = []
    temp_cache = []
    for stream in raw_streams:
        for val in stream:
            if val > 50:
                temp_cache.append(val * 0.8)
            elif val < 10:
                temp_cache.append(val * 1.2)
            else:
                temp_cache.append(val)
    
    # Irrelevant aggregation (dead path)
    max_val = max(temp_cache) if temp_cache else 0
    min_val = min(temp_cache) if temp_cache else 0
    avg_val = sum(temp_cache) / len(temp_cache) if temp_cache else 0

    # Actual relevant sampling logic
    interval = len(temp_cache) // duration
    for i in range(0, len(temp_cache), interval):
        if i + interval <= len(temp_cache):
            segment = temp_cache[i:i+interval]
            samples.append(sum(segment) / len(segment))
    return samples

# Legacy compatibility function (never called)
def legacy_transform(x):
    return (x << 2) ^ 0xFF

def normalize_readings(readings_list):
    normalized = []
    base_offset = 27.3
    scaling_factor = 1.85
    
    # Distractor: unused statistical calculations
    mean = sum(readings_list) / len(readings_list)
    variance = sum((x - mean) ** 2 for x in readings_list) / len(readings_list)
    std_dev = variance ** 0.5
    
    for val in readings_list:
        adjusted = (val - base_offset) * scaling_factor
        normalized.append(round(adjusted, 4))
    
    # Red herring: spurious transformation
    inverted = [1.0 / (1 + abs(x)) for x in normalized]
    
    return normalized

# Data fusion from heterogeneous sources
def fuse_sources(primary, secondary, mode='strict'):
    fused = []    
    # Bit manipulation decoy
    magic_key = (0xABCD ^ 0x1234) & 0xFFFF
    checksum = 0
    
    for p, s in zip(primary, secondary):
        if mode == 'strict' and abs(p - s) > 5.0:
            fused.append(p * 0.7 + s * 0.3)
        else:
            fused.append((p + s) / 2)
        
        # Accumulate irrelevant checksum
        checksum ^= int(abs(p * 10)) & 0xFF
    
    # Checksum never used
    final_checksum = (checksum + magic_key) % 256
    
    return fused

# Core analysis engine
def cluster_patterns(values, eps=1.5):
    if not values:
        return []
    
    clusters = defaultdict(int)
    visited = [False] * len(values)
    
    # Simulated DBSCAN-like clustering (simplified)
    for i in range(len(values)):
        if visited[i]:
            continue
        neighbors = []
        for j in range(len(values)):
            if abs(values[i] - values[j]) < eps:
                neighbors.append(j)
        
        if len(neighbors) >= 2:
            cluster_id = round(values[i], 1)
            clusters[cluster_id] += len(neighbors)
            for idx in neighbors:
                visited[idx] = True
    
    return dict(clusters)

# Main processing pipeline
def process_readings(data, thresholds):
    # Intermediate storage
    stats = defaultdict(float)
    diagnostics = []
    
    # Extract key metrics
    for key, vals in data.items():
        if key in thresholds:
            above_threshold = [v for v in vals if v > thresholds[key]]
            count_ratio = len(above_threshold) / len(vals)
            stats[key] = count_ratio
            
            # Spurious bitwise operation chain
            encoded = 0
            for v in above_threshold[:4]:
                encoded ^= int(v) & 0xF
                encoded = (encoded << 1) | (encoded >> 3)
            encoded = encoded & 0xFF
            
    # Real diagnostic logic
    score = 0.0
    for k, ratio in stats.items():
        if k.startswith('sensor_'):
            if ratio > 0.6:
                score += 15.7
            elif ratio > 0.3:
                score += 7.2
        elif k.startswith('probe_'):
            score += ratio * 10.3
    
    # Final computation - this is where answer is determined
    adjustment = len(stats) * 3.1
    final_diagnostic = round(score - adjustment, 4)
    
    # Dead code - misleading output
    debug_code = (int(final_diagnostic) ^ 0xAA) & 0xFF
    
    return final_diagnostic

# --- Entry Point ---
if __name__ == "__main__":
    # Simulated input data streams
    stream_a = [12, 8, 55, 62, 9, 44, 7, 67, 58, 11]
    stream_b = [14, 6, 53, 65, 13, 42, 5, 70, 56, 10]

    # Step 1: Collect samples over 5-second duration
    samples_a = collect_samples([stream_a], 5)
    samples_b = collect_samples([stream_b], 5)
    
    # Step 2: Normalize both streams
    norm_a = normalize_readings(samples_a)
    norm_b = normalize_readings(samples_b)
    
    # Step 3: Fuse data from two sources
    fused_data = fuse_sources(norm_a, norm_b, mode='strict')
    
    # Step 4: Cluster patterns in fused data
    patterns = cluster_patterns(fused_data, eps=2.0)
    
    # Step 5: Prepare aggregated structure (key step)
    aggregated_data = {
        'sensor_alpha': [9.2, 10.1, 11.3, 8.7, 12.0, 10.5, 9.8],
        'sensor_beta': [6.5, 7.1, 6.9, 8.2, 7.3],
        'probe_gamma': [4.4, 5.1, 3.9, 5.0, 4.7, 5.3, 4.1],
        'probe_delta': [3.8, 4.0, 3.6, 4.2]
    }
    
    # Threshold configuration map
    threshold_map = {
        'sensor_alpha': 10.0,
        'sensor_beta': 7.0,
        'probe_gamma': 4.5,
        'probe_delta': 4.0
    }
    
    # Critical statement
    final_diagnostic = process_readings(aggregated_data, threshold_map)
    
    # Output result
    print(f"Target result: {final_diagnostic}")