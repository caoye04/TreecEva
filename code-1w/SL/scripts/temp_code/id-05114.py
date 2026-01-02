import math

def analyze_component(reading, threshold=75):
    # Irrelevant helper with dead logic
    if reading < 0:
        return False
    normalized = (reading / 100) ** 0.5
    return normalized > 0.8

def compute_checksum(sequence):
    # Distractor function - looks important but unused in critical path
    chk = 0
    for i, val in enumerate(sequence):
        chk ^= (val + i) % 256
    return chk

def transform_data(raw_list):
    # Mix of relevant and irrelevant operations
    temp_values = []
    outlier_count = 0
    for idx, item in enumerate(raw_list):
        if item > 90:
            outlier_count += 1
        adjusted = item * 0.95 if item > 80 else item * 1.02
        temp_values.append(round(adjusted))
    
    # Dead code path - misleading intermediate result
    if outlier_count > 10:
        temp_values = [x - 5 for x in temp_values]
        
    return temp_values

def evaluate_stability(metrics):
    # Critical computation buried in noise
    base_score = 0
    penalty = 0
    for i, val in enumerate(metrics):
        if i % 3 == 0 and val < 70:
            penalty += 10
        elif val > 95:
            base_score += 5
    return base_score - penalty

def process_metrics(log_data, settings):
    # Core logic with distractions
    filtered = [x for x in log_data if x >= settings['min_threshold']]
    
    # Irrelevant transformation chain
    processed_chain = []
    accumulator = 0
    for v in filtered:
        accumulator += v * 0.1
        processed_chain.append(int(accumulator))
    
    # Real metric calculation
    avg = sum(filtered) / len(filtered) if filtered else 0
    peak = max(filtered) if filtered else 0
    
    # Conditional expression determining key state
    mode_flag = 'high' if avg > 85 else 'normal'
    
    # Bit manipulation red herring
    bit_analysis = 0
    for x in filtered[:5]:
        bit_analysis |= (x << 2) & 0xFF
    
    # Actual efficiency formula buried among decoys
    stability = evaluate_stability(filtered)
    efficiency_score = (avg * 0.6) + (stability * 2) + (100 - peak) * 0.1
    
    # Unused complex structure to increase nesting and confusion
    summary_report = {
        'stats': {
            'mean': avg,
            'max': peak,
            'stability_bonus': stability
        },
        'flags': [
            f'{mode_flag}-mode',
            'analyzed'
        ]
    }
    
    # Final output assignment - point of interest
    final_output = {
        'result_code': 200,
        'efficiency_score': round(efficiency_score, 4),
        'diagnostics': processed_chain[-3:] if len(processed_chain) >= 3 else []
    }
    
    return final_output

# Simulated sensor data log - realistic input
sensor_readings = [88, 76, 92, 85, 96, 79, 83, 94, 87, 91, 77, 89, 95, 84, 90]

dummy_sequence = [10, 20, 30, 40, 50]  # Unused but plausible-looking data

# Configuration dict with plausible parameters
config = {
    'min_threshold': 75,
    'debug_mode': False,
    'version': '2.1'
}

# Transform data (irrelevant to final result but looks important)
data_intermediate = transform_data(sensor_readings)

# Actual entry point
data_log = sensor_readings  # Reset to original to avoid confusion from transform

final_output = process_metrics(data_log, config)

# Extract target variable
Result: {final_output['efficiency_score']}