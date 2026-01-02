import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw_values = [i * 1.5 + 2.3 for i in range(120) if i % 3 != 0]
    filtered = [x for x in raw_values if x > 5.0]
    return filtered[:50]

# Irrelevant auxiliary function - dead code path (distractor)
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [math.sin(x - mean_val) for x in data]

# Data transformation with embedded logic red herrings
def transform_signal(readings, mode='advanced'):
    temp_buffer = []
    checksum = 0
    
    for idx, val in enumerate(readings):
        adjusted = val * (idx % 7 + 1)
        checksum ^= int(adjusted)  # Bitwise distraction
        
        if idx % 5 == 0:
            adjusted = abs(math.cos(adjusted)) * 100
        elif idx % 5 == 2:
            adjusted = math.log(max(adjusted, 1.1)) * 10
        else:
            adjusted = adjusted ** 0.5
            
        temp_buffer.append(adjusted * 1.07)
    
    # Decoy operation with no downstream effect
    outlier_score = sum(1 for x in temp_buffer if x > 50)
    normalization_factor = math.sqrt(sum([x**2 for x in temp_buffer[:10]]) + 1e-6)
    
    # Actual relevant transformation output
    normalized = [x / normalization_factor for x in temp_buffer]
    return normalized

# Diagnostic engine with conditional bypasses and early returns
def analyze_pattern(data, threshold):
    magnitude_peak = max(data)
    base_metric = sum([x for x in data if x > threshold])
    
    if magnitude_peak < 3.0:
        return -1 * base_metric  # Early exit red herring

    # Complex interdependent calculations with misleading intermediate names
    proxy_cache = []
    running_weight = 0.0
    
    for i, value in enumerate(data):
        weight = (i + 1) / len(data)
        running_weight += weight
        
        # Irrelevant transformation chain
        if value > threshold * 1.5:
            transformed = math.atan(value) * (running_weight % 1.3)
            proxy_cache.append(transformed - 0.1)
        else:
            transformed = value ** 0.33
            if transformed > 2.0:
                proxy_cache.append(transformed / 3.0)
            else:
                proxy_cache.append(transformed * 1.5)
    
    # Critical logic buried among distractors
    primary_index = 0
    for j in range(len(proxy_cache)):
        if proxy_cache[j] > 1.0:
            primary_index += int(proxy_cache[j]) % (j + 1)
    
    # Real result computation - depends on prior loop
    aggregate = sum(proxy_cache[k] * (k % 4 + 1) for k in range(0, len(proxy_cache), 3))
    adjustment = math.floor(primary_index * 0.7) or 1
    final_score = (aggregate * adjustment) / (magnitude_peak + 1)
    
    # Decoy final checks that don't affect outcome
    consistency_check = all(proxy_cache[i] <= proxy_cache[i+1] for i in range(len(proxy_cache)-1) if i % 7 == 0)
    if consistency_check:
        final_score += 0.001  # Irrelevant under this input
        
    return int(final_score * 100) / 100.0

# Unused but plausible-looking functions (distractors)
def validate_calibration(sequence):
    return [x for x in sequence if x % 2 == 0 and x > 10]

def compute_legacy_index(arr):
    return sum(math.tan(x/10) for x in arr if x < 20)

# Main execution flow
if __name__ == "__main__":
    readings_source = collect_readings()
    transformed_data = transform_signal(readings_source, mode='advanced')
    key_threshold = 2.5
    final_diagnostic = analyze_pattern(transformed_data, key_threshold)
    print(f"Result: {final_diagnostic}")