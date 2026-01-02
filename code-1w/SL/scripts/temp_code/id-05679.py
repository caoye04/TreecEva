import itertools

# Simulated sensor array diagnostics with multiple noise filters and data transformation paths

def collect_diagnostics(raw_stream, calibration_factor):
    temp_log = []
    for val in raw_stream:
        if val < 0:
            temp_log.append(abs(val) * calibration_factor)
        elif val == 0:
            temp_log.append(1.0)
        else:
            temp_log.append(val ** 0.5)
    return temp_log


def apply_noise_filter(signal, method='median'):
    sorted_sig = sorted(signal)
    length = len(sorted_sig)
    if method == 'median':
        mid = length // 2
        return sorted_sig[mid] if length % 2 == 1 else (sorted_sig[mid-1] + sorted_sig[mid]) / 2
    return sum(sorted_sig) / length  # mean fallback


def generate_combinations(elements):
    # Distractor: generates unused combinatorial metadata
    combo_stats = {}
    for r in range(1, len(elements)+1):
        combos = list(itertools.combinations(elements, r))
        combo_stats[r] = len(combos)
    return combo_stats

# Irrelevant helper function — dead code path
def legacy_checksum(data):
    checksum = 0
    for item in data:
        if isinstance(item, int):
            checksum ^= item
    return checksum

# Unused signal smoothing function (red herring)
def smooth_signal(x, window=3):
    smoothed = []
    for i in range(len(x)):
        start = max(0, i - window + 1)
        smoothed.append(sum(x[start:i+1]) / (i - start + 1))
    return smoothed

# Core processing chain
raw_sensor_data = [144, -64, 0, 256, -81, 100, 121, -49]
decoy_labels = ['A', 'B', 'C', 'D']

# Step 1: Apply initial calibration
initial_processing = collect_diagnostics(raw_sensor_data, calibration_factor=1.5)

# Step 2: Generate irrelevant combinatorics (distractor)
label_combos = generate_combinations(decoy_labels)  # Unused later

# Step 3: Filter out values below dynamic threshold
dynamic_threshold = sum(initial_processing) / len(initial_processing) * 0.6
filtered_data = [x for x in initial_processing if x > dynamic_threshold]

# Step 4: Build threshold map using string-based key derivation (uses string method)
base_keys = ['alpha', 'beta', 'gamma']
threshold_map = {}
for k in base_keys:
    key_upper = k.upper()
    if 'A' in key_upper:
        threshold_map[k] = dynamic_threshold * 1.1
    elif 'G' in key_upper:
        threshold_map[k] = dynamic_threshold * 0.9
    else:
        threshold_map[k] = dynamic_threshold

# Step 5: Misleading early exit check (never triggered due to data)
if len(threshold_map) > 10:
    final_diagnostic = -999
    print(f"Result: {final_diagnostic}")
else:
    # Real computation path
    def process_readings(data, config):
        result = 0.0
        weights = [1.2, 0.8, 1.5]  # arbitrary scaling factors
        keys_in_order = sorted(config.keys())
        
        # Use of string join as distractor
        debug_tag = ''.join([k[0] for k in keys_in_order]).upper()
        
        if debug_tag.startswith('A'):
            for i, val in enumerate(data):
                weight = weights[i % len(weights)]
                intermediate = val * weight
                if intermediate > config['alpha']:
                    result += intermediate * 0.7
                elif intermediate > config['beta']:
                    result += intermediate * 0.5
                else:
                    result += intermediate * 0.3
        
        # Additional noise filter applied only to subset (relevant)
        subset_for_validation = [data[i] for i in range(0, len(data), 2)]
        validation_floor = apply_noise_filter(subset_for_validation, method='median')
        
        # Final adjustment based on filtered median
        if result > 0:
            result -= validation_floor * 0.25
        
        # Decoy bitwise operation (looks important but unused)
        decoy_flag = 0b1010 ^ 0b1100 & 0b0011
        
        return round(result, 6)
    
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
# Output result
print(f"Result: {final_diagnostic}")