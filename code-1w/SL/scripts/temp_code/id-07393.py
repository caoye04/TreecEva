import math

# Irrelevant utility function (dead code path)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm else v

def analyze_phase_shift(signal):
    # Distractor computation with no impact on final result
    shifted = [(i * 2 + 1) % 8 for i in range(16)]
    magnitude = sum(math.sin(x) for x in shifted)
    return abs(magnitude) > 3

# Misleading intermediate structure
class DataBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size
    
    def fill(self, val):
        self.buffer = [val % 256] * self.size

    def checksum(self):
        # Looks important but unused
        return sum(self.buffer) % 1000

# Real processing begins here
def evaluate_convergence(x, y, threshold=0.001):
    iterations = 0
    while abs(x - y) > threshold and iterations < 5000:
        x = (x + y) / 2.0
        y = math.sqrt(x * y)
        iterations += 1
    return iterations

data_log = [
    {'timestamp': 100, 'value': 42, 'flags': [1, 0, 1]},
    {'timestamp': 150, 'value': 38, 'flags': [0, 1, 1]},
    {'timestamp': 200, 'value': 45, 'flags': [1, 1, 0]}
]

config = {
    'mode': 'aggressive',
    'tolerance': 0.05,
    'boost': True
}

# Complex distractor: looks like it's used but isn't
temp_registry = [{'id': i, 'state': (i * i + 3) % 7} for i in range(10)]
for item in temp_registry:
    item['active'] = item['state'] % 2 == 0

# Decoy transformation chain
transform = lambda seq: [math.log(1 + x['value']) for x in seq if x['value'] > 30]
intermediate = transform(data_log)
scaled = [x * 1.5 for x in intermediate if x < 4.0]  # Partial filtering

# Actual core logic hidden among noise
flag_sum = sum(sum(entry['flags']) for entry in data_log)
timestamp_diff = data_log[-1]['timestamp'] - data_log[0]['timestamp']
base_metric = flag_sum * 100 / timestamp_diff

# Conditional expression with meaningful outcome
adjustment = 1.25 if config['boost'] and config['tolerance'] < 0.1 else 0.85

# Key computational step involving prior elements
convergence_iter = evaluate_convergence(100.0, 50.0, threshold=0.02)
efficiency_score = base_metric * adjustment + (convergence_iter // 100)

# Dead assignment - distractor
buffer = DataBuffer(512)
buffer.fill(2047)

# Unused complex list comprehension
_ = [\n    {'idx': i, 'calc': (lambda a, b: a**2 - b)(j, i)}
    for i in range(3)
    for j in range(i+1, 6)
]

# Final orchestration point
final_output = process_metrics(data_log, config) if 'mode' in config else None

# But we actually compute efficiency_score independently
# The following line is critical and produces the answer
print(f"Result: {efficiency_score}")

# Simulate missing function to avoid error
process_metrics = lambda x, y: sum(d['value'] for d in x) % 100