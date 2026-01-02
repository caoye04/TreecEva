import math

# Simulated sensor fusion system for environmental monitoring
base_threshold = 42.5
redundant_flag = False
def unused_helper(data):
    return [x * 1.5 for x in data if x > 30]

def generate_noise(length):
    # Irrelevant function - dead code path
    return [math.sin(i * 0.5) for i in range(length)]

def preprocess(raw):
    # Mix of relevant and irrelevant operations
    offset = 10
    adjusted = [x + offset for x in raw]
    filtered = [x for x in adjusted if x > base_threshold]
    inverted = list(map(lambda y: 100 - y, filtered))  # Distractor transformation
    return filtered  # Only filtered is used downstream

status_log = set()
legacy_buffer = [0] * 5  # Unused data structure

for i in range(5):
    if i % 2 == 0:
        status_log.add(f"stage_{i}_complete")
    else:
        status_log.discard("pending")  # Meaningless operation

# Simulated raw sensor inputs
temp_readings = [25.3, 38.7, 45.1, 52.6, 33.9, 47.2]
humid_readings = [30, 45, 55, 60, 40, 50]  # Unused but plausible

processed_signals = preprocess(temp_readings)

# Decoy data transformation chain
aggregated = sum([x * x for x in temp_readings]) / len(temp_readings)
normalized = math.log(aggregated + 1)  # Looks important but unused

flag_matrix = [[True if i == j else False for j in range(3)] for i in range(3)]

# Core diagnostic logic buried in distractions
def analyze_readings(data):
    if not data:
        return -1
    
    # Real computation mixed with red herrings
    mean_val = sum(data) / len(data)
    squared_devs = [(x - mean_val) ** 2 for x in data]
    variance = sum(squared_devs) / len(squared_devs)
    std_dev = math.sqrt(variance)
    
    # Multiple early returns as distractors
    if mean_val < 40:
        return mean_val * 2
    if std_dev < 5:
        return std_dev * 10
    
    # Actual execution path
    peak = max(data)
    clipped = min(peak, 50.0)
    adjustment_factor = 0.8 if peak > 50 else 1.1
    intermediate = clipped * adjustment_factor
    
    # Final computation
    entropy_proxy = -sum([ (x/sum(data)) * math.log(x/sum(data)) for x in data if x > 0 ])
    final_score = intermediate + (entropy_proxy * 2)
    
    # Dead branch with misleading name
    if len(data) > 100:
        redundant_calc = math.exp(-variance)
        return redundant_calc
    
    return final_score

# Unused recursive function - decoy complexity
def trace_propagate(val, depth):
    if depth <= 0:
        return val
    return trace_propagate(val + math.cos(depth), depth - 1)

# Key assignment statement
final_diagnostic = analyze_readings(processed_signals)

# Critical output
print(f"Result: {final_diagnostic}")