import math

# Irrelevant helper function (dead code path)
def legacy_calculate(x):
    return (x ** 2 + 3 * x + 1) % 7

# Unused utility for string obfuscation
def obscure_key(s):
    return ''.join(chr((ord(c) + 5) % 90 + 32) for c in s)

# Real processing begins here
raw_signals = [14, 8, 22, 17, 3, 9, 11]
scaling_factor = 2.5
offset_threshold = 6.7

# Distractor: irrelevant signal normalization
normalized = [(val - min(raw_signals)) / (max(raw_signals) - min(raw_signals)) for val in raw_signals]
scaled_normalized = [round(n * scaling_factor, 3) for n in normalized]

# Actual data transformation chain
transformed_data = []
for x in raw_signals:
    if x % 2 == 0:
        transformed_data.append(int(math.sqrt(x) * 10))
    else:
        transformed_data.append(x * 3 + 1)

# Decoy sorting operation (misleading intermediate result)
sorted_temp = sorted(transformed_data, reverse=True)
duplicate_check = len(transformed_data) != len(set(transformed_data))

# Configuration with red herring fields
class Config:
    def __init__(self):
        self.mode = 'diagnostic'
        self.debug_level = 99  # unused
        self.max_iterations = 1000  # unused
        self.threshold = 45
        self.weights = [0.1, 0.3, 0.6]  # unused

config = Config()

# Bit manipulation decoy
checksum = 0
for val in raw_signals:
    checksum ^= (val << 2) & 0xFF

# Real processing function with nested logic
def process_metrics(data, cfg):
    base_score = sum(d for d in data if d > cfg.threshold)
    
    # Nested filtering and transformation
    filtered = [d for d in data if d < 50]
    mapped = list(map(lambda x: x + 5 if x % 4 == 0 else x - 2, filtered))
    
    # Conditional adjustment based on bit count
    ones_count = bin(sum(mapped))[2:].count('1')
    adjustment = -3 if ones_count > 10 else 2
    
    # String-based switch (irrelevant but looks important)
    mode_flag = 'D' + 'I'.lower() + 'A' + 'G'.swapcase()
    if mode_flag == 'DIAG':
        adjustment += 1  # never reached due to case mismatch
    
    # Critical calculation
    aggregate = sum(mapped) + adjustment
    
    # Secondary filter that actually matters
    high_vals = list(filter(lambda x: x > 40, data))
    bonus = len(high_vals) * 7
    
    return aggregate + bonus

# Additional distraction: unused recursive function
def forecast(trend, depth):
    if depth <= 0 or trend > 100:
        return trend
    return forecast(trend * 1.1 + 2, depth - 1)

# Unused data structure cross-reference
reference_map = {i: chr(65 + (i % 26)) for i in range(30)}
lookup_chain = [reference_map.get(x % 30, '?') for x in transformed_data]

# Key execution point
final_diagnostic = process_metrics(transformed_data, config)

# Print required result
print(f"Result: {final_diagnostic}")