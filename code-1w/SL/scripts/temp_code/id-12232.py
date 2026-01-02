import math

# Simulated sensor data and calibration parameters (mostly irrelevant)
sensor_a_offset = 0.023
sensor_b_offset = -0.017
temp_calibration_map = {i: round(math.sin(i * 0.1), 4) for i in range(100)}
baseline_readings = [round(math.cos(x * 0.2), 3) for x in range(50)]

# Real-time signal buffer with mixed noise and valid entries
raw_signal_stream = [
    1.2, 0.9, 1.5, 2.3, -0.1, 4.4, 3.2, 0.0, 1.1, 2.2,
    5.1, -0.5, 3.3, 2.1, 1.8, 0.7, 4.6, 3.9, 2.7, 1.0
]

# Ancillary functions – some are decoys


def validate_entry(val):
    return isinstance(val, float) and val > -1.0


def normalize(val, min_val=0.0, max_val=5.0):
    # Unused normalization function
    return (val - min_val) / (max_val - min_val) if max_val != min_val else 0.0


def apply_mask(data, mask_factor=0.9):
    # Distractor transformation not used in main logic
    return [x * mask_factor for x in data]


def decode_timestamp(ts):
    # Fake parsing function – never called
    return (ts >> 4) & 0xFF, ts & 0x0F

# Core processing chain begins here

def filter_outliers(stream):
    mean_val = sum(stream) / len(stream)
    std_dev = (sum((x - mean_val) ** 2 for x in stream) / len(stream)) ** 0.5
    threshold = mean_val + 1.8 * std_dev
    return [x for x in stream if x <= threshold and x >= 0.5]  # Filters to specific band


def transform_item(x, idx):
    if idx % 2 == 0:
        return x ** 2
    else:
        return abs(int(x)) * 0.5


def process_signals(data_list):
    indexed_data = enumerate(data_list)
    transformed = []
    for i, val in indexed_data:
        result = transform_item(val, i)
        transformed.append(result)
    
    # Aggregation using lambda and zip
    pairing = lambda a, b: a + b
    paired_sums = [pairing(x, y) for x, y in zip(transformed[::2], transformed[1::2])]
    
    # Final computation path
    adjustment_factor = 1.5 if len(paired_sums) > 3 else 1.0
    raw_total = sum(paired_sums)
    
    # Misleading intermediate that looks important but isn't final
    diagnostic_score = raw_total * 0.87 + 12.5  
    
    # Actual output
    final_output = int(raw_total * adjustment_factor)  # This will be printed
    
    # Dead code branch – unreachable
    if False:
        fallback = math.log(diagnostic_score + 1)
        return fallback
        
    return final_output

# Irrelevant counters
packet_counter = 0
error_flags = []
redundant_buffer = [0] * 20

# Main execution flow
filtered_data = filter_outliers(raw_signal_stream)

# Unused alternate path
if len(filtered_data) < 5:
    filtered_data = [1.0, 1.0, 1.0]

# Critical statement
final_output = process_signals(filtered_data)

# Spurious post-processing
final_output += 0  # No-op
final_output *= 1  # No-op

# Output result
print(f"Result: {final_output}")