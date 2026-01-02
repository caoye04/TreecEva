import math

# Simulated sensor data processing pipeline for environmental monitoring
raw_readings = [14.2, -5.1, 8.9, 0.0, 23.7, -1.3]
dummy_flags = [True, False, True, False]
offset_adjustment = 3.14159
temp_cache = {}

# Irrelevant lookup table for deprecated hardware
legacy_map = {1: 'A', 2: 'B', 3: 'C'}
device_status = {'active': True, 'calibrated': False}

# Distractor: unused transformation
lambda_shift = lambda x: x ** 2 if x > 0 else abs(x)

# Core data transformation with meaningful and irrelevant parts
def transform_readings(data, bias=1.1):
    processed = []
    scaling_factor = 1.0 + (bias / 10)
    noise_floor = 0.01
    decoy_sum = 0

    for val in data:
        # Real transformation step
        adjusted = (val + offset_adjustment) * scaling_factor
        
        # Red herring computation
        for i in range(2):
            decoy_sum += i * adjusted  # Unused accumulation

        # Actual required transformation
        if adjusted < 0:
            adjusted = abs(adjusted) * 0.9
        processed.append(round(adjusted, 6))
    
    # Distractor: string manipulation unrelated to result
    status_msg = "Processed_" + "_".join(map(str, dummy_flags)).lower()
    status_msg = status_msg.replace("true", "valid").replace("false", "idle")

    return processed

def validate_entry(val, threshold=5.0):
    # Simple validation used in filtering
    return val > threshold

# Misleading pre-processing function that is never called
def obsolete_filter(x):
    return list(filter(lambda z: z % 2 == 0, x))

# Another decoy function with bitwise red herring
def flag_analysis(x):
    result = 0
    for i in range(len(dummy_flags)):
        result |= (i << 1)  # Complex-looking but unused
    return result

# Configuration with mixed relevant and irrelevant fields
config = {
    'version': '2.1',
    'enable_enhancement': True,
    'scaling_method': 'adaptive',
    'threshold': 7.5,
    'iterations': 3
}

# Step 1: Transform raw data
transformed_data = transform_readings(raw_readings, bias=1.1)

# Step 2: Apply conditional filtering based on threshold
filtered_data = [x for x in transformed_data if validate_entry(x, config['threshold'])]

# Step 3: Compute diagnostic metrics
primary_metric = sum(filtered_data)
secondary_metric = len([x for x in transformed_data if x < 10])

# Step 4: Bitwise obfuscation layer (some relevant use)
data_flag = len(filtered_data) ^ 5  # XOR used meaningfully
if data_flag & 1:  # Check least significant bit
    primary_metric -= 2.5

# Step 5: Conditional expression chain
aux_score = (secondary_metric * 1.5) if config['enable_enhancement'] else (secondary_metric * 0.8)

# Step 6: Final processing with lambda integration
metric_processor = lambda m, s: round(m * 0.85 + s * 1.2, 6)

# Step 7: Key statement — answer depends on this execution
def process_metrics(metrics, cfg):
    base = metric_processor(primary_metric, aux_score)
    adjustment = 0.0

    # Nested conditional distractors
    if cfg['scaling_method'] == 'linear':
        adjustment = -10.0
    elif cfg['scaling_method'] == 'legacy':
        adjustment = sum([math.log(abs(x) + 1) for x in raw_readings])
    else:
        # Actual path: adaptive scaling applies
        sample_peak = max(transformed_data)
        adjustment = math.sqrt(sample_peak) * 0.5

    # Decoy dictionary updates
    temp_cache['last_run'] = base
    temp_cache['flags'] = data_flag

    # Final computation
    result = base + adjustment

    # Irrelevant string operation
    log_str = "Final_Result:" + str(result).upper()
    log_str = log_str.replace(":", "_")

    return result

final_diagnostic = process_metrics(transformed_data, config)
print(f"Result: {final_diagnostic}")