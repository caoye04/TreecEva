import math

def generate_mask(n):
    # Irrelevant function: generates a bitmask but not used in main logic
    return sum(1 << i for i in range(n) if i % 3 == 0)

def auxiliary_transform(x):
    # Distractor function: used in dead code path
    return (x >> 1) ^ (x << 2)

class DataProcessor:
    def __init__(self, threshold):
        self.threshold = threshold
        self.counter = 0

    def analyze(self, val):
        self.counter += 1
        if val < self.threshold:
            return val ** 2
        else:
            return int(math.sqrt(val))

# Unused global variables (distractors)
MAX_BUFFER_SIZE = 1024
temp_cache = [0] * 50
debug_log = []

# Simulated sensor data with noise
raw_readings = [144, 25, 196, 81, 225, 64, 169]

# Dead code path: precompute something unused
transformed = list(map(lambda x: (x + 10) * 2, raw_readings))
filtered_data = [x for x in raw_readings if x > 50]  # Partially used idea, misleading

# Primary data stream derived from raw readings
data_stream = [x for x in raw_readings if x % 2 == 0]  # Only even perfect squares

# Decoy processing chain
buffer = []
for item in raw_readings:
    if item > 100:
        buffer.append(item // 4)
    elif item == 81:
        buffer.append(0)  # Red herring

# Real processing begins here
processor = DataProcessor(threshold=100)

# Complex nested comprehension with filtering and transformation
intermediate = [
    processor.analyze(val) 
    for val in data_stream 
    if val != 64 or processor.counter < 5
]

# Additional distraction: recursive countdown (never called)
def countdown(n):
    return 1 if n <= 0 else n - countdown(n - 2)

# Conditional expression with side effects (counter incremented in analyze)
backup_mode = len(filtered_data) > 4 else False

# Key computation involving multiple steps
scaling_factor = 3 if backup_mode else 2
adjusted = [x * scaling_factor for x in intermediate]

# Final aggregation using bit manipulation (only some bits matter)
def aggregate(values):
    acc = 0
    for v in values:
        acc ^= v  # XOR accumulation
        acc = (acc + (v & 7)) % 1000  # Use only low-order bits
    return acc

# Misleading early assignment
prelim_result = aggregate([64, 81])  # Uses constants, irrelevant

# Actual target computation
final_output = aggregate(adjusted)

# Print required output
print(f"Result: {final_output}")