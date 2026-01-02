from collections import defaultdict
import math

# Simulated sensor data with noise and metadata
data_packets = [
    {'id': 101, 'readings': [3.2, 1.8, 4.5, 2.7], 'status': 'active', 'calib': 0.98},
    {'id': 102, 'readings': [2.1, 2.3, 2.2, 2.4], 'status': 'active', 'calib': 1.02},
    {'id': 103, 'readings': [], 'status': 'idle', 'calib': 1.00},
    {'id': 104, 'readings': [5.5, 6.1, 5.8], 'status': 'active', 'calib': 0.95}
]

# Irrelevant auxiliary mapping (distractor)
type_mapping = defaultdict(lambda: 'unknown')
type_mapping.update({101: 'temperature', 102: 'pressure', 104: 'flow'})

# Noise threshold constants (some are unused - red herring)
NOISE_FLOOR = 0.1
CLIP_THRESHOLD = 4.0
MAX_READINGS = 10

# Signal filtering function with multiple layers of processing
def filter_noisy_readings(readings, threshold=2.5, mode='clip'):
    if not readings:
        return [0.0]
    
    # Apply soft squashing for high values (not used in final logic - misleading)
    squashed = [x / (1 + x) for x in readings if x > 0]
    
    # Actual relevant transformation
    filtered = []
    for x in readings:
        if mode == 'clip' and x > CLIP_THRESHOLD:
            filtered.append(CLIP_THRESHOLD)
        elif x >= threshold:
            filtered.append(x)
    return filtered if filtered else [threshold]  # Ensure non-empty

# Checksum calculator (dead code path - never called)
def compute_checksum(data):
    checksum = 0
    for b in str(data).encode('utf-8'):
        checksum = (checksum * 31 + b) % 65537
    return checksum

# Data enrichment with decoy operations
def enrich_packet(packet):
    raw = packet['readings']
    calib = packet['calib']
    
    # Multiple irrelevant transformations
    normalized = [round(x * calib, 3) for x in raw] if raw else [0.0]
    squared_devs = [(x - 2.5)**2 for x in normalized]  # Unused metric
    entropy_proxy = -sum(math.log(x + 1e-5) for x in squared_devs) if squared_devs else 0  # Red herring
    
    # Relevant processing
    valid_readings = filter_noisy_readings(normalized, threshold=2.0, mode='clip')
    
    return {
        'node_id': packet['id'],
        'readings': valid_readings,
        'quality': len(valid_readings),
        'aux_score': entropy_proxy  # Distractor field
    }

# Higher-order function returning lambda (required python feature)
create_aggregator = lambda method: (
    lambda vals: sum(vals) / len(vals) if vals else 0
) if method == 'mean' else (
    lambda vals: max(vals) if vals else 0
)

mean_agg = create_aggregator('mean')
max_agg = create_aggregator('extreme')  # Unused

# Complex data pipeline with conditional logic and distractors
def process_signal_packets(packets):
    processed = []
    temp_store = []  # Dead storage (never used later)

    for p in packets:
        if p['status'] != 'active':
            continue
            
        enriched = enrich_packet(p)
        
        # Spurious transformation chain
        transformed = list(map(lambda x: x * 1.1 + 0.05, enriched['readings']))
        clipped_again = [min(x, 3.9) for x in transformed]  # Not used
        
        # Key computation
        aggregate = mean_agg(enriched['readings'])
        if aggregate > 3.0:
            enriched['flag'] = True
            temp_store.append(aggregate * 0.1)  # Diverted use
        else:
            enriched['flag'] = False
        
        processed.append(enriched)
    
    return processed

# Diagnostic analyzer with branching logic
def analyze_signal(data_list):
    if not data_list:
        return -1.0
    
    # Build frequency map of qualities (distractor structure)
    quality_count = defaultdict(int)
    for item in data_list:
        quality_count[item['quality']] += 1
    
    # Compute weighted diagnostic score
    total_weight = 0.0
    diagnostic_sum = 0.0
    
    for entry in data_list:
        base_val = entry['readings'][0] if entry['readings'] else 0
        flag_bonus = 10 if entry['flag'] else 0
        
        # Complex but deterministic weight calculation
        length_factor = len(entry['readings'])
        exp_decay = math.exp(-0.3 * length_factor)  # Diminishes longer readings
        weight = (base_val + 0.1 * flag_bonus) * (1 - exp_decay)
        
        diagnostic_sum += weight * (length_factor + flag_bonus)
        total_weight += weight
    
    # Final result depends on weighted average with nonlinear factors
    return round(diagnostic_sum / total_weight if total_weight != 0 else 0, 6)

# --- Execution Flow ---
processed_data = process_signal_packets(data_packets)

# Decoy computations to mislead analysis
_ = [compute_checksum(p) for p in data_packets]  # Dead call
_ = sorted(processed_data, key=lambda x: x.get('aux_score', 0), reverse=True)  # Unused sort
shadow_value = sum(len(p['readings']) for p in processed_data) * 0.01  # Unused

final_diagnostic = analyze_signal(processed_data)
print(f"Result: {final_diagnostic}")