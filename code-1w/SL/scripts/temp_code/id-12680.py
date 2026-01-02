import math

# Irrelevant helper function (decoy)
def dummy_transform(x):
    return (x ** 2 + 3 * x + 5) % 7

# Misleading data accumulator with dead logic
class DataAccumulator:
    def __init__(self):
        self.buffer = []
        self.counter = 0
        self.ignored_flag = True  # Never actually used

    def add(self, x):
        self.buffer.append(x)
        self.counter += 1

    def flush(self):
        temp = sum(self.buffer)
        self.buffer.clear()
        return temp * 0.1  # Distractor computation

# Unused but plausible-looking utility
ignored_scaling_factors = [1.1, 0.9, 1.05, 0.95]
recent_weights = {'a': 0.2, 'b': 0.3, 'c': 0.5}

# Core processing pipeline
def bitwise_modulate(value, key):
    shifted = (value << 2) & 0xFF
    toggled = shifted ^ key
    return toggled if toggled > 0 else toggled + 256

def evaluate_signal(x):
    if x < 10:
        return int(math.sin(x) * 100)
    elif x < 50:
        return int(math.sqrt(x) * 10)
    else:
        return x // 3

# Lambda for string-based filtering (only some strings matter)
valid_prefix = lambda s: s.startswith('DATA') and s.endswith('Z')
data_tags = ['INFO_X', 'DATA_001Z', 'LOG_99', 'DATA_002Z', 'TEMP_A']
filtered_tags = [tag for tag in data_tags if valid_prefix(tag)]  # Only 2 pass

# Real signal generator (but only part is relevant)
signal_base = 0
for tag in filtered_tags:
    signal_base += ord(tag[4])  # Chars: '0' and '0' -> 48 + 48 = 96

# Another distraction: complex-looking but unused transformation chain
raw_sequence = [bitwise_modulate(i * 5, 0x1A) for i in range(8)]
smoothed = list(map(lambda x: (x + (x >> 1)) // 2, raw_sequence))
checksum = sum(smoothed) % 256

# Actual core data
primary_seed = 23
secondary_seed = 41
temp_offset = evaluate_signal(primary_seed)  # sin(23)*100 ≈ -82

# Critical nested logic with red herrings
intermediate = 0
for i in range(3):
    if i == 0:
        intermediate += temp_offset * 2
    elif i == 1:
        intermediate -= math.ceil(math.log(secondary_seed + 1))  # log(42)≈3.7 → 4
    else:
        accumulator = DataAccumulator()
        for val in [10, 20, 30]:
            accumulator.add(val)
        flushed = accumulator.flush()  # 6 → not used directly
        intermediate += int(flushed * 3)  # 18

# More distractions: string manipulation with partial relevance
diag_msg = f"Signal strength: {abs(intermediate)} dB"
diag_code = diag_msg.split(':')[1].strip().split(' ')[0]  # 'dB'

diagnostic_value = 0
if diag_code == "dB":
    diagnostic_value = 100
else:
    diagnostic_value = -100

# Real computation path embedded
shift_key = len(filtered_tags) * 13  # 2 * 13 = 26
modulated = bitwise_modulate(signal_base, shift_key)  # bitwise_modulate(96, 26)

# Final pipeline
contextual_adjustment = 0
if modulated > 100:
    contextual_adjustment = 5
else:
    contextual_adjustment = -3

# Key statement
final_output = process_pipeline = lambda data: (
    (data + intermediate + diagnostic_value + contextual_adjustment) % 97319
)

# Execute critical statement
data_stream = modulated
final_output = process_pipeline(data_stream)

print(f"Target result: {final_output}")