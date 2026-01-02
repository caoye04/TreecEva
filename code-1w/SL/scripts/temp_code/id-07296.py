import math

# Simulated sensor array diagnostics with interference

def collect_readings():
    raw_samples = [18.2, 22.5, 19.8, 24.1, 20.3, 25.6, 17.9, 23.4]
    scaling_factor = 1.05
    adjusted = [x * scaling_factor for x in raw_samples]
    outlier_check = [x for x in adjusted if x > 25]  # red herring
    return adjusted

# Irrelevant preprocessing function (distractor)
def normalize_signal(data):
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return [0 for _ in data]
    return [(x - min_val) / (max_val - min_val) for x in data]

# Decoy analysis with misleading logic
def quick_diagnose(data):
    avg = sum(data) / len(data)
    if avg > 21:
        return "ELEVATED"
    return "NORMAL"

# Core processing with conditional expressions and bit manipulation
def process_critical_readings(raw, config_flag):
    baseline = sum(raw) / len(raw)
    deviation_map = [abs(x - baseline) for x in raw]
    
    # Conditional expression + bit flag usage
    correction_mode = 0b101 if config_flag & 0b100 else 0b010
    shift_comp = (correction_mode >> 1) & 1
    
    # Apply non-linear transformation only if condition met
    processed = [
        math.log(x) * 2 if (i % 2 == 0 and shift_comp) else x * 0.95 
        for i, x in enumerate(raw)
    ]
    
    # Dead code path (never executed due to fixed flag)
    if config_flag < 0:
        processed = [math.sqrt(x) for x in processed if x > 0]
    
    padding = [0.0] * 2  # unused distraction
    final_padded = processed + padding  # irrelevant extension
    
    return processed  # only this matters

# Main diagnostic engine
def analyze_readings(data, thresh):
    n = len(data)
    segments = [data[:4], data[4:]]
    
    # Multiple comparison operations and short-circuiting
    valid = n > 6 and all(x > 10 for x in data) or thresh < 0
    
    if not valid:
        return -999
    
    # Complex aggregation with distractors
    mean_a = sum(segments[0]) / 4
    mean_b = sum(segments[1]) / 4
    diff_ratio = (mean_b - mean_a) / mean_a if mean_a != 0 else 0
    
    # Bitwise analysis on derived values (red herring)
    signature = int(abs(diff_ratio * 100))
    parity_check = bin(signature).count('1') % 2  # unused
    
    # Key decision logic with early return avoided
    score_raw = 0
    for val in data:
        if val > thresh * 1.1:
            score_raw += 1.5
        elif val > thresh:
            score_raw += 0.8
        else:
            score_raw += 0.3
    
    # Final transformation using conditional expression
    final_score = score_raw if score_raw <= 10 else 8 + (score_raw - 10) * 0.5
    
    # Unused alternate scoring method (decoy)
    alt_score = sum(1 for x in data if x > thresh) * 1.2
    
    return round(final_score * 100) / 100  # deterministic decimal

# Irrelevant auxiliary functions
def generate_report_header():
    return "SENSOR_DIAG_V3"

def compress_data(arr):
    return [arr[i] for i in range(0, len(arr), 2)]

def validate_checksum(data):
    return True  # always passes

# Global decoy variables
system_status = "ACTIVE"
last_calibration = "2023-11-05"
emergency_override = False
config_mask = 0b1101
spare_buffer = [0] * 16

# Main execution flow
if __name__ == "__main__":
    readings = collect_readings()
    normalized = normalize_signal(readings)  # computed but unused
    fast_result = quick_diagnose(readings)   # distractor call
    
    # Actual relevant processing chain
    processed_data = process_critical_readings(readings, config_mask)
    threshold = 20.5
    
    # Critical statement
    final_diagnostic = analyze_readings(processed_data, threshold)
    
    # Print required result
    print(f"Target result: {final_diagnostic}")