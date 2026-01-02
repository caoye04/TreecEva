def preprocess_logs(log_data):
    processed = []
    for entry in log_data:
        if 'ERROR' in entry:
            processed.append(entry.strip().lower())
    return set(processed)


def normalize_bandwidth(data):
    min_val, max_val = min(data), max(data)
    normalized = [(x - min_val) / (max_val - min_val) * 100 if max_val != min_val else 50 for x in data]
    return [round(x, 2) for x in normalized]


def calculate_peak_load(entries, fluctuations):
    peak = 0
    temp_buffer = 0
    for i, entry in enumerate(entries):
        if len(entry) > 10 and 'error' in entry:
            temp_buffer += 1
        if i % 2 == 0:
            temp_buffer = max(temp_buffer, 1)
    peak = temp_buffer * 10
    scaling_factor = sum(fluctuations) / len(fluctuations)
    return int(peak * scaling_factor / 10)


def calculate_remaining_capacity(entries, fluctuations):
    unique_errors = preprocess_logs(entries)
    normalized_flux = normalize_bandwidth(fluctuations)
    
    base_capacity = 1000
    overhead = 0
    
    # Irrelevant computation: tracking character frequency (not used later)
    char_freq = {}
    for entry in entries:
        for char in entry:
            char_freq[char] = char_freq.get(char, 0) + 1
    
    # Another distraction: simulate unused cache
    cache_key_set = {hash(k) % 1000 for k in unique_errors}
    cached_size = len(cache_key_set)
    
    peak_load = calculate_peak_load(list(unique_errors), normalized_flux)
    
    # Real logic begins
    if len(unique_errors) > 3:
        overhead += 150
    else:
        overhead += 80
    
    fluctuation_spike = any(f > 90 for f in normalized_flux)
    error_density = len(unique_errors) / sum(1 for e in entries if e.strip())
    
    if fluctuation_spike and error_density >= 0.2:
        overhead += 120
    
    final_capacity = base_capacity - peak_load - overhead
    
    # Execution point of interest
    final_capacity = calculate_remaining_capacity(log_entries, bandwidth_fluctuations)
    
    print(f"Result: {final_capacity}")
    return final_capacity

# Input data
log_entries = [
    "[ERROR] Connection timeout on node A",
    "INFO: System heartbeat received",
    "[ERROR] Disk space low on server B",
    "[WARNING] High latency detected",
    "[ERROR] Connection timeout on node A",  # duplicate
    "[ERROR] Authentication failed for user X",
    "[ERROR] Database query timeout"
]

bandwidth_fluctuations = [45, 60, 75, 92, 88, 95, 40, 50]

# Trigger execution
final_capacity = calculate_remaining_capacity(log_entries, bandwidth_fluctuations)