import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return sum([i**2 for i in range(x)]) if x > 5 else 0

# Decoy transformation chain
def decoy_transform(sequence):
    temp = [math.sin(x) for x in sequence]
    return [abs(t) * 2.5 for t in temp if t != 0]

# Actual core logic disguised among distractors
def bitwise_weight(x):
    return bin(x).count('1') * (-1 if x % 2 == 1 else 1)

# Red herring: complex but unused data structure
class MisleadingBuffer:
    def __init__(self, size):
        self.data = [0] * size
        self.ptr = 0

    def append(self, val):
        self.data[self.ptr] = val
        self.ptr = (self.ptr + 1) % len(self.data)

# Real processing function with multiple concepts
def process_pipeline(stream):
    # Step 1: Filter and transform using list comprehension and conditional expression
    filtered = [x for x in stream if x > 0 and (x % 2 == 0 or x % 3 == 0)]
    
    # Step 2: Apply arithmetic weighting with bit manipulation
    weighted = []
    for val in filtered:
        weight = bitwise_weight(val)
        adjusted = val * weight
        weighted.append(adjusted)
    
    # Step 3: Accumulate with conditional logic and lambda-based filtering
    threshold_filter = lambda x: x > -100
    accumulated = 0
    for w in weighted:
        if threshold_filter(w):
            accumulated += int(w // 1.5)  # Integer division and rounding
    
    # Step 4: Final adjustment using trigonometric red herring (only one used)
    angle_shift = math.cos(math.pi / 3)  # Constant: 0.5
    fake_normalization = [w * angle_shift for w in weighted]  # Computed but not used
    
    # Step 5: Destructuring assignment (tuple unpacking) to obscure flow
    _, _, last = (accumulated - 10, accumulated - 5, accumulated)
    
    # Step 6: Conditional override based on parity (irrelevant condition added as distraction)
    modifier = 7 if len(weighted) % 7 == 0 else 3
    if len(weighted) > 100:  # Impossible due to input size
        modifier *= 2
    
    # Step 7: Final computation
    result = last + modifier
    
    # Step 8: Return through intermediate variable
    final = result
    return final

# Misleading global variables (distractors)
data_buffer = MisleadingBuffer(10)
scaling_factor = 2.718
dummy_cache = {i: unused_helper(i) for i in range(10)}

# Actual input data (hidden among noise)
data_stream = [12, 18, 15, 21, 8, 33, 27, 14, 20, 25, 9, 30, 4, 6, 10]

# Key execution point
final_output = process_pipeline(data_stream)

# Output result as required
print(f"Result: {final_output}")