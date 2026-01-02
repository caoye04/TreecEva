def analyze_signal(values):
    # Irrelevant signal processing (distractor)
    fft_result = [v * 2 for v in values]  # Fake FFT
    threshold = 42
    filtered = [v for v in fft_result if v > threshold]
    return sum(filtered) % 100

# Unused function (dead code path)
def legacy_calculate(x):
    return (x << 2) ^ 7

# Red herring data
sensor_log = [15, 23, 8, 44, 91, 67]
signal_strength = analyze_signal(sensor_log)

# Core logic disguised among distractions
def transform_input(data):
    a, b, c = data
    temp = (a + b) * 2 - c
    return temp // 3 if temp > 30 else temp * 2

def validate_entry(code):
    # Bit manipulation decoy
    masked = code & 0xFF
    flipped = masked ^ 0xAA
    return flipped == 85

# Real computation hidden in lambda and recursion
tree_sum = lambda lst: lst[0] + tree_sum(lst[1:]) if lst else 0

def process_metrics(raw):
    # Recursive structure with early exit
    if len(raw) <= 1:
        return raw[0] if raw else 0
    mid = len(raw) // 2
    left = raw[:mid]
    right = raw[mid:]
    return process_metrics(left) + process_metrics(right)

# Distractor variables
baseline = 127
calibration_offset = baseline ^ 64
debug_flag = False

# Main pipeline
metric_data = [6, 9, 15, 21, 33]

# Multiple assignment red herring
x, y, z = metric_data[0], metric_data[1], metric_data[2]
intermediate = transform_input((x, y, z))

# String manipulation distraction
status_msg = "System_Ready"
status_upper = status_msg.upper().replace("_", " ")
checksum = sum(ord(c) for c in status_upper if c.isalpha()) % 50

# Conditional branch with misleading logic
if validate_entry(85):
    adjustment = 5
else:
    adjustment = -5

# Key recursive aggregation
aggregated = process_metrics(metric_data)

# Final evaluation combining multiple concepts
def evaluate_performance(data):
    base = tree_sum(data)
    bonus = len(data) ** 2
    penalty = 0
    for i, val in enumerate(data):
        if val % 3 == 0 and i % 2 == 1:
            penalty += 3
    # Critical line: what is final_score?
    final_score = (base + bonus - penalty + intermediate + adjustment) * 2
    return final_score

# Execution point of interest
final_score = evaluate_performance(metric_data)
print(f"Result: {final_score}")