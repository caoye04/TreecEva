import math

# Simulated sensor data processing with embedded logic chain
def fetch_raw_readings():
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

def clean_data(raw):
    cleaned = [x for x in raw if x > 0]
    adjustment_factor = 0.9
    adjusted = [int(x * adjustment_factor) + 1 for x in cleaned]
    # Distractor: irrelevant transformation
    temp_shift = sum([x ** 0.5 for x in adjusted]) // len(adjusted)
    return adjusted

def generate_lookup(limit):
    # Dead code path - never actually used in final computation
    lookup = {}
    for i in range(limit):
        lookup[i] = (i ** 2 + 3 * i + 7) % 11
    return lookup

def transform_entry(val, shift):
    if val % 2 == 0:
        return val << 1
    else:
        return val ^ shift

def apply_filter(data, mode='standard'):
    shift_key = 5 if mode == 'enhanced' else 3
    filtered = []
    for item in data:
        transformed = transform_entry(item, shift_key)
        # Irrelevant intermediate check
        if transformed > 15:
            continue  # Red herring filter that doesn't affect core logic
        filtered.append(transformed)
    return filtered

def recursive_reduce(seq, index=0):
    if index >= len(seq) - 1:
        return seq[index] if seq else 0
    return seq[index] + 0.5 * recursive_reduce(seq, index + 1)

def analyze_pattern(data, limit):
    base_score = recursive_reduce(data)
    peak = max(data) if data else 0
    # Complex conditional expression (required Python feature)
    penalty = 7 if (peak > 10 and len(data) < 8) else (3 if peak > 5 else 0)
    # Secondary distractor calculation with no impact
    dummy_chain = [(x | 4) ^ 2 for x in data if x % 3 == 0]
    dummy_sum = sum(dummy_chain) * 0.1
    # Core answer logic buried among distractions
    raw_total = sum(data)
    adjustment = math.log(abs(raw_total) + 1) if raw_total != 0 else 0
    return int(base_score - penalty + adjustment)

# Main execution flow
if __name__ == "__main__":
    readings = fetch_raw_readings()
    processed = clean_data(readings)
    
    # Unused but plausible-looking analysis
    unused_lookup = generate_lookup(10)
    anomaly_count = sum(1 for x in processed if x in [7, 8, 9])  # Dead statistic
    
    # Real transformation begins here
    transformed_data = apply_filter(processed, mode='standard')
    
    # Multiple branching paths with one decoy
    threshold = 4
    if sum(transformed_data) > 20:
        threshold += 1
    else:
        temp_val = [x for x in transformed_data if x > 5]  # Unused list
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Print required output
    print(f"Target result: {final_diagnostic}")