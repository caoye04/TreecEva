def signal_analyzer(data_stream):
    # Irrelevant preprocessing steps (distractors)
    temp_cache = [x ** 2 for x in data_stream if x % 3 == 0]
    checksum = sum(temp_cache) % 100
    normalized = [x / (checksum + 1e-5) for x in temp_cache]

    # Core logic buried among distractions
    filtered = [x for x in data_stream if x > 0]
    shifted = [filtered[i] - filtered[i-1] for i in range(1, len(filtered))]
    squared_deltas = [d**2 for d in shifted if d != 0]

    # Decoy function call with no side effects
    def decoy_transform(seq):
        return [seq[-i] * 2 for i in range(1, len(seq)+1)]

    # Actual relevant transformation
    if len(squared_deltas) >= 5:
        windowed = squared_deltas[2:7]  # slicing operation used here
        averaged = sum(windowed) / len(windowed)
        scaled = int(averaged * 3.7)
    else:
        scaled = 1337  # dead branch (never reached due to input)

    # Red herring: unused complex structure
    history_log = {}
    for idx, val in enumerate(data_stream):
        if val not in history_log:
            history_log[val] = []
        history_log[val].append(idx * 2 + (val % 7))

    # Another irrelevant computation
    bit_analysis = 0
    for num in data_stream:
        bit_analysis ^= (num << 2) & 0xFF

    return scaled


def noise_filter(signal):
    # Simple smoothing (unused in final path)
    smoothed = []
    for i in range(1, len(signal) - 1):
        smoothed.append((signal[i-1] + signal[i] + signal[i+1]) // 3)
    return smoothed


def final_processor(buffer):
    # Critical transformation on buffer
    base_value = sum(buffer) // len(buffer)
    adjustment = len(buffer) % 9
    return base_value + adjustment * 6


# Simulated sensor data (fixed seed for determinism)
data_input = [12, 15, 18, 22, 25, 30, 33, 36, 40, 42]

# Dead code path: complex but unused state machine
class StateTracker:
    def __init__(self):
        self.state = 0
        self.transitions = []

    def advance(self, val):
        self.state = (self.state + val) % 5
        self.transitions.append(self.state)

tracker = StateTracker()
for v in data_input:
    tracker.advance(v % 10)

# Main processing chain
raw_output = signal_analyzer(data_input)
output_buffer = [raw_output + i*2 for i in range(5)]

# Key statement
result = final_processor(output_buffer)

print(f"Target result: {result}")