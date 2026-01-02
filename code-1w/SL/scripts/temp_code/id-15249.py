import math

# Irrelevant helper function (dead code path)
def unused_checksum(data):
    return sum(d % 256 for d in data) ^ 0xFF

# Distractor variables
temp_cache = [0] * 256
scaling_factor = 1.732
decoy_sum = 0

# Real processing components
def transform(x):
    return (x ^ 0xAA) + (x >> 3)

apply_mask = lambda val: val & 0xFFFF if val > 100 else val + 256

# Misleading intermediate computation (not used in final result)
for i in range(100):
    decoy_sum += (i * scaling_factor) ** 2

class DataStream:
    def __init__(self, input_seq):
        self.raw = input_seq
        self.filtered = []
        self.buffer = []

    def preprocess(self):
        for x in self.raw:
            if x % 2 == 0:
                self.buffer.append(transform(x))
            else:
                self.buffer.append(x + 128)

    def decode(self):
        temp = []
        for val in self.buffer:
            modified = apply_mask(val)
            if modified % 3 == 0:
                temp.append(int(math.sqrt(modified)) if modified > 0 else 0)
            elif modified % 5 == 0:
                temp.append(modified // 5)
            else:
                temp.append(modified - 10)
        self.filtered = temp

# Initialization with realistic domain-specific data (sensor readings)
sensor_readings = [150, 205, 90, 111, 240, 67, 180, 103]
stream = DataStream(sensor_readings)
stream.preprocess()

# Dead branch - never executed but looks important
if len(stream.buffer) > 1000:
    stream.buffer = [x for x in temp_cache if x < 100]

stream.decode()

# Key distraction: complex-looking but unused bit manipulation
bit_scramble = 0
for b in stream.filtered:
    bit_scramble ^= (b << 1) | (b >> 7)
bit_scramble = (bit_scramble + 0xABCD) % 65536

# Actual critical data path
stream_buffer = stream.filtered.copy()
offset_correction = sum(1 for x in stream_buffer if x > 50)

# Secondary transformation chain
adjusted = [x + offset_correction for x in stream_buffer]
compressed = ''.join(str(x) for x in adjusted)

# Use of string methods - case conversion on numeric string (distractor)
dummy_upper = compressed.upper()  # no effect

# Another lambda - real usage this time
evaluate_strength = lambda s: sum(int(c) for c in s if c.isdigit())

interim_score = evaluate_strength(compressed) // 3

# Core calculation buried in distractions
entropy_proxy = 0
for idx, val in enumerate(adjusted):
    if idx % 2 == 0:
        entropy_proxy += val * 3
    else:
        entropy_proxy -= val * 2

baseline_reference = math.floor(interim_score * 1.5)

# Final processing function combining multiple concepts
def process_data(data):
    acc = baseline_reference
    for i, v in enumerate(data):
        if i % 4 == 0:
            acc += int(math.sin(v) * 100) % 97
        elif i % 4 == 2:
            acc += v ^ (i + 1)
        else:
            acc -= (v + i) % 23
    return acc + len(data)

# Critical execution point
final_output = process_data(stream_buffer)

print(f"Target result: {final_output}")