import math

# Irrelevant helper function (dead code path)
def unused_similarity(a, b):
    return sum(1 for x, y in zip(a, b) if x == y) / len(a)

# Misleading data transformation chain
def transform_signal(x):
    return (x * 1.8) + 32  # Looks like F to C but not used correctly

# Decoy function with plausible but unused logic
def calculate_urgency(level, threshold=5):
    if level > threshold:
        return math.log(level) * 100
    return 0

# Real processing begins here — deeply nested and mixed with noise
def analyze_pattern(sequence):
    accumulator = 0
    temp_offset = 17
    magic_factor = 3.14159
    
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            accumulator += (val ** 2) % 7
        else:
            accumulator -= (val + temp_offset) % 4
    
    # Red herring: complex-looking but unused expression
    derived_bias = (magic_factor * temp_offset) // (accumulator + 1) if accumulator != 0 else 0
    
    return accumulator

# Lambda used for conditional filtering — relevant
filter_valid = lambda x: x > 0 and x != 999

# Another decoy: signal normalization with no downstream effect
def normalize_readings(readings):
    max_val = max(readings)
    return [r / max_val for r in readings]

# Key function that contributes to final answer
def compute_adaptive_weight(length, base=10):
    weight = base
    for _ in range(length % 4):
        weight = (weight * 1.5) % 100
    return round(weight, 3)

# Function containing bit manipulation red herring
def assess_integrity(checksum):
    # Bitwise operations that look important but are only partially used
    stage1 = checksum ^ 0xFF
    stage2 = stage1 >> 2
    stage3 = stage2 & 0x3F
    
    # Only this modulo result matters; rest is distraction
    return stage3 % 11

# Core evaluation logic buried among distractions
def evaluate_performance(metrics):
    raw_total = 0
    adjustment = 0
    
    # Extract relevant subset using lambda
    valid_metrics = list(filter(filter_valid, metrics))
    
    # Meaningful calculation: analysis result affects output
    pattern_result = analyze_pattern(valid_metrics)
    
    # Irrelevant intermediate — looks like calibration
    fake_calibration = transform_signal(len(valid_metrics))
    
    # This weight is actually used
    dynamic_weight = compute_adaptive_weight(len(valid_metrics))
    
    # Multiple branches with one key condition
    if len(valid_metrics) > 3:
        raw_total += pattern_result * 2
        if pattern_result > 5:
            adjustment += 5
        elif pattern_result == 5:
            adjustment += 2
        else:
            adjustment -= 3
    else:
        raw_total += pattern_result
        adjustment -= 1
    
    # Integrity check feeds into final score
    integrity = assess_integrity(sum(valid_metrics))
    
    # Critical computation hidden in a sea of variables
    score_component_1 = raw_total + adjustment
    score_component_2 = dynamic_weight * integrity
    
    # Final formula — only this matters
    final_computation = int(score_component_1 + (score_component_2 / 2.5))
    
    # Dead assignment — misleading
    final_computation = final_computation % 97 if final_computation > 50 else final_computation + 8
    
    return final_computation

# Simulated input data — contains red herring values (e.g., 999 as sentinel)
metric_data = [3, -1, 6, 999, 2, 5]  # -1 and 999 filtered out

# Unused but plausible variable initializations (distractors)
baseline_ref = 42.0
aggregation_mode = 'weighted'
calibration_lock = True
override_sequence = [0xFF, 0xAA, 0x55]

# Key execution point
final_score = evaluate_performance(metric_data)

# Output result as required
print(f"Target result: {final_score}")