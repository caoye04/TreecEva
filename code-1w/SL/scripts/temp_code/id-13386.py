def analyze_sequence(seq):
    # Irrelevant helper function (dead code path)
    return sum(x ** 2 for x in seq if x % 2 == 0)

# Unused constants (distractors)
MAX_ITERATIONS = 5000
THRESHOLD_LIMIT = 0.75
BASE_MULTIPLIER = 3.14159

# Simulated benchmark data with mixed types (some irrelevant)
data_log = [
    {'id': 'A1', 'raw': 85, 'active': True, 'meta': {'flag': False}},
    {'id': 'B2', 'raw': 90, 'active': False, 'meta': {'flag': True}},
    {'id': 'C3', 'raw': 78, 'active': True, 'meta': {'flag': True}}
]

# Weights for scoring (only some are used)
weights = {
    'primary': 0.6,
    'secondary': 0.3,
    'tertiary': 0.1,  # Not actually used
    'bonus': 1.5       # Distractor
}

# Auxiliary structure - partially relevant
status_map = {True: 1, False: -1}

# Bit manipulation red herring
def obscure_transform(n):
    shifted = (n << 3) & 0xFF
    toggled = shifted ^ 0b10101010
    return toggled >> 2

# Another decoy function
def validate_threshold(value, limit=THRESHOLD_LIMIT):
    return value > limit * MAX_ITERATIONS  # Never called

# Core logic disguised among distractions
def preprocess_entry(entry):
    base = entry['raw']
    modifier = status_map[entry['active']]
    return base + modifier * 2

# Conditional expression and enumerate usage (required features)
def extract_signals(data_list):
    signals = []
    for i, item in enumerate(data_list):
        # Use of conditional expression
        signal = item['raw'] * 1.1 if item['meta']['flag'] else item['raw'] * 0.9
        # Introduce enumerate-based offset
        adjusted = signal + (i - 1) * 0.5
        signals.append(adjusted)
    return signals

# Real calculation chain hidden in complexity
def calculate_performance(dataset, weight_dict):
    # Step 1: Extract active entries
    active_entries = [e for e in dataset if e['active']]
    
    # Step 2: Preprocess each
    processed = [preprocess_entry(e) for e in active_entries]
    
    # Step 3: Use enumerate and zip together (required features)
    indices = list(range(len(processed)))
    zipped_data = list(zip(processed, indices))
    indexed_sum = sum(val * (idx + 1) for val, idx in zipped_data)  # Weight by position
    
    # Step 4: Apply primary weight
    weighted_sum = indexed_sum * weight_dict['primary']
    
    # Step 5: Add bonus from signal extraction (secondary path)
    signals = extract_signals(dataset)
    signal_total = sum(s for s in signals if s > 80)  # Filter condition
    secondary_contribution = signal_total * weight_dict['secondary']
    
    # Step 6: Combine
    aggregate = weighted_sum + secondary_contribution
    
    # Step 7: Apply bit-irrelevant transform (red herring but harmless)
    masked = obscure_transform(int(aggregate) % 256)
    
    # Step 8: Final adjustment — deterministic but obscured
    final_value = aggregate - (masked * 0.01)
    
    return round(final_value, 4)

# Main execution flow
if __name__ == "__main__":
    # Misleading initialization
    temp_result = analyze_sequence([4, 6, 8, 10])  # Dead end
    runtime_flag = temp_result > 200  # Unused boolean
    
    # Actual critical computation
    benchmark_data = data_log  # Alias to confuse data flow
    final_score = calculate_performance(benchmark_data, weights)
    
    # Output required result
    print(f"Target result: {final_score}")