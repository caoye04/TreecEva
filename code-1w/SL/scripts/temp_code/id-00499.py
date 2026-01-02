from functools import reduce
import math

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    return sum(-x * math.log2(x) for x in data if x > 0)

def transform_sequence(seq, key_factor):
    # Applies bitwise and modular arithmetic transformations
    transformed = []
    for i, val in enumerate(seq):
        shifted = (val << 2) ^ key_factor
        modded = (shifted + i) % 19
        transformed.append(modded)
    return transformed

def evaluate_consistency(metrics, threshold=10):
    # Evaluates pattern consistency using set operations and lambda filtering
    unique_metrics = set(metrics)
    filtered = list(filter(lambda x: (x % 3 == 0) or (x & 1), unique_metrics))
    
    # Dead code path - never executed due to fixed condition
    debug_mode = False
    if debug_mode:
        print("Debug:", len(filtered))
    
    return len(filtered) > threshold

def aggregate_signals(raw_data, mode="strict"):
    # Complex aggregation with multiple distractions
    baseline = sum(raw_data) // len(raw_data)
    adjusted = [x - baseline + (i ** 2) for i, x in enumerate(raw_data)]
    
    # Irrelevant transformation chain
    temp_state = [math.ceil(x / 2.5) for x in adjusted]
    temp_state = [t ^ 7 for t in temp_state]  # Bitwise red herring
    
    # Real processing begins
    if mode == "strict":
        processed = [p for p in temp_state if p > 0]
        reduced = reduce(lambda acc, v: acc + (v & 15), processed, 0)
        return reduced
    else:
        return sum(temp_state)

def finalize_evaluation(interim_results, offset):
    # Final computation involving character counting distraction and real logic
    magic_const = 263
    checksum = 0
    
    # Distractor: string manipulation unrelated to final result
    identifier = "diagnostic_2048"
    char_count = {c: identifier.count(c) for c in set(identifier)}
    unused_weight = sum(char_count.values()) * 2  # Never used
    
    for val in interim_results:
        if val < 0:
            continue
        # Core calculation
        checksum += (val * 3) % 17
    
    # Critical formula
    result = (checksum * 2) - offset
    return result

# Main execution flow
if __name__ == "__main__":
    # Initial signal data
    signal_readings = [12, 7, 14, 3, 8, 11, 6]
    
    # Step 1: Transform readings
    key_phase = 5
    processed_signal = transform_sequence(signal_readings, key_phase)
    
    # Step 2: Evaluate consistency (returns boolean, not used directly)
    is_stable = evaluate_consistency(processed_signal, threshold=6)
    
    # Step 3: Aggregate signals into score
    raw_aggregation = aggregate_signals(processed_signal, mode="strict")
    
    # Step 4: Build intermediate results with dummy container
    temp_results = []
    temp_results.append(raw_aggregation)
    temp_results.append(len(processed_signal))
    temp_results.append(42)  # Red herring constant
    
    # Unused variables - dead code paths
    shadow_copy = temp_results.copy()
    shadow_copy.append(calculate_entropy([0.25, 0.25, 0.5]))  # Irrelevant entropy
    
    # Baseline offset computed via modular arithmetic
    baseline_offset = (key_phase ** 3) % 29
    
    # Key statement
    filtration_score = finalize_evaluation(temp_results, baseline_offset)
    
    # Output result
    print(f"Result: {filtration_score}")