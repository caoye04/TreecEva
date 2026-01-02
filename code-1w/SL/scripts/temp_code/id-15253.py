import itertools

# Irrelevant helper function (dead code path)
def unused_transform(x):
    return (x << 3) ^ 0xFF

def generate_mask(n):
    # Distractor: complex-looking bit manipulation with no real impact
    mask = 0
    for i in range(n % 7):
        mask |= (1 << (i * 3))
    return mask & 0b1111  # Limited effect, red herring

# Decoy data processing chain
class DataObfuscator:
    def __init__(self, key=13):
        self.key = key
        self.history = []

    def scramble(self, val):
        # Looks important but not used in final computation
        return (val ^ self.key) % 997

    def encode_stream(self, stream):
        return [self.scramble(x) for x in stream]

# Real processing begins here
def filter_valid_entries(sequence):
    # Only values where sum of digits is divisible by 3 and index is even
    valid = []
    for idx, num in enumerate(sequence):
        digit_sum = sum(int(d) for d in str(abs(num)))
        if digit_sum % 3 == 0 and idx % 2 == 0:
            valid.append(num)
    return valid

def compute_weighted_sum(values):
    if not values:
        return 0
    # Weight based on position using modular arithmetic
    weights = [(i + 1) % 5 + 1 for i in range(len(values))]
    return sum(val * weights[i] for i, val in enumerate(values))

def extract_features(data):
    # Uses lambda and itertools to create distraction
    paired = list(itertools.combinations(data, 2))
    diffs = list(map(lambda pair: abs(pair[0] - pair[1]), paired))
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    
    # This looks like feature engineering but is unused
    _ = [d ** 2 for d in diffs if d > avg_diff]
    
    return avg_diff  # Actually not used later, minor red herring

def process_pipeline(input_data):
    # Step 1: Filter valid entries by digit-sum rule
    step1 = filter_valid_entries(input_data)
    
    # Step 2: Apply transformation that includes irrelevant parts
    obfuscator = DataObfuscator(key=42)
    decoy_data = obfuscator.encode_stream(step1)  # Computed but unused
    
    # Step 3: Compute actual result from original filtered data
    temp_result = compute_weighted_sum(step1)
    
    # Step 4: Use of lambda in non-critical way (distraction)
    augment = lambda x: x + (x >> 2) if x > 0 else x
    adjusted = augment(temp_result)
    
    # Step 5: Final adjustment using modular arithmetic
    final = (adjusted * 3) % 10007
    
    # Irrelevant logging
    debug_info = {
        'input_len': len(input_data),
        'filtered_count': len(step1),
        'decoy_checksum': sum(decoy_data[:5]) if len(decoy_data) >= 5 else 0,
        'phantom_feature': extract_features(step1)
    }
    
    return final

# Main execution
if __name__ == '__main__':
    # Input data with meaningful pattern
    raw_signal = [123, 456, 789, 101, 202, 303, 404, 505]
    
    # Unused transformations (red herrings)
    shifted_signal = [x << 1 for x in raw_signal]
    masked_values = [x & generate_mask(x) for x in shifted_signal]
    
    # Critical assignment
    data_stream = [x * 2 for x in raw_signal]  # Doubled input
    
    # Key statement
    final_output = process_pipeline(data_stream)
    
    print(f"Result: {final_output}")