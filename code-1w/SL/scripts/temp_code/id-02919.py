import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    raw_signals = [i * 0.5 for i in range(20)]
    filtered = [x for x in raw_signals if x > 3.0]
    processed = []
    for val in filtered:
        if val % 2 == 0:
            processed.append(int(val ** 1.5))
        else:
            processed.append(int(val * 1.8))
    return processed

# Legacy checksum function (irrelevant to final result)
def compute_legacy_checksum(data):
    checksum = 0
    for item in data:
        checksum ^= item
        checksum = (checksum * 3) % 7
    return checksum

# Signal validation using windowed variance (distraction)
def validate_signal_stability(readings):
    if len(readings) < 5:
        return False
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    return variance < 150

# Core diagnostic aggregator (critical path)
def aggregate_metrics(entries, threshold):
    # Irrelevant pre-processing step
    normalized = [max(0, e - 2) for e in entries if e > 1]
    
    # Decoy statistical analysis
    peak = max(normalized)
    floor = min(normalized)
    spread = peak - floor
    
    # Actual logic: count how many exceed dynamic threshold
    adjusted_threshold = threshold * 1.2 if spread > 40 else threshold * 0.8
    
    # Misleading intermediate transformation
    transformed = []
    for e in normalized:
        if e > adjusted_threshold:
            transformed.append(e * 0.9)
        else:
            transformed.append(math.sqrt(e + 1))
    
    # Critical decision logic (depends on initial count)
    significant_count = sum(1 for e in entries if e > threshold)
    
    # Fake adaptive weighting
    weights = [0.8 + 0.02 * i for i in range(len(transformed))]
    weighted_sum = sum(w * v for w, v in zip(weights, transformed))
    
    # Final determination based on original signal count and threshold
    if significant_count >= 6:
        base_score = 850 + (significant_count * 12)
    elif significant_count >= 3:
        base_score = 420 + (significant_count * 18)
    else:
        base_score = 90 + (significant_count * 10)
    
    # Apply irrelevant environmental correction factor
    env_factor = 1.05  # assumed constant
    corrected = base_score * env_factor
    
    # Final adjustment based on legacy pattern (unused)
    legacy_flag = (corrected % 25) > 10
    
    # ACTUAL OUTPUT logic - depends only on significant_count and fixed math
    final_value = int(corrected - 35) if legacy_flag else int(corrected - 25)
    
    return final_value

# Unused auxiliary functions (dead code paths)
def deprecated_analysis(x):
    return [i << 2 for i in x if i & 1]

def dummy_calibration(seq):
    return sum(s % 7 for s in seq) * 0.3

# Global configuration (some misleading constants)
SYSTEM_MODE = "diagnostic"
CALIBRATION_OFFSET = 0.78
DEBUG_FLAGS = {"verbose": False, "safe_mode": True}
TEMPORAL_WINDOW = 30  # unused

# Generate inputs
log_entries = generate_telemetry()
system_threshold = 14.0

# Compute legacy checksum (never used)
checksum = compute_legacy_checksum(log_entries)

# Validate signal (result ignored)
is_stable = validate_signal_stability(log_entries)

# Main computation
final_diagnostic = aggregate_metrics(log_entries, system_threshold)

# Print result as required
print(f"Result: {final_diagnostic}")