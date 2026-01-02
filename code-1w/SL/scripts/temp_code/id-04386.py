import math

# Irrelevant utility function (dead code path)
def unused_helper(x):
    return x ** 3 + 2 * x - 1

# Misleading precomputed constants (distractors)
baseline_offset = 17.3
reference_anchor = 982
junk_threshold = 42  # Unused in actual logic

def analyze_phase(signal_input, threshold=5):
    # Complex but partially irrelevant processing
    magnitude = sum([abs(x) for x in signal_input]) / len(signal_input)
    normalized = [x / (magnitude + 1e-6) for x in signal_input]
    
    # Real logic begins here: count transitions above threshold
    crossings = 0
    for i in range(1, len(normalized)):
        if normalized[i-1] < threshold and normalized[i] >= threshold:
            crossings += 1
    
    # Red herring computation
    dummy_score = math.exp(-0.1 * magnitude) * 100
    
    return crossings

# Decoy data structures
legacy_map = {'A': 1, 'B': 4, 'C': 9}
temp_buffer = set()
for k in range(5):
    temp_buffer.add(k * k % 7)

# Core system parameters
logic_flow = [3, 7, 2, 8, 1, 9, 4, 6]
calibration_data = {'gain': 0.85, 'bias': -0.15, 'iterations': 3}

# Distractor loop with no side effects
accumulator = 0
for _ in range(100):
    accumulator += int(math.sqrt(_ + 1)) % 3

# Lambda-based transformation chain (relevant)
filter_func = lambda x: x > 4
weight_func = lambda x: x * 0.75 if x > 6 else x * 0.5
transformed_flow = list(map(weight_func, filter(filter_func, logic_flow)))

# Secondary analysis with misleading intermediate
def evaluate_coherence(data):
    total = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            total += math.log(val + 1)
        else:
            total -= math.sin(val)
    return round(total, 4)

coherence_score = evaluate_coherence(transformed_flow)  # Not used later

# Actual critical computation path
rolling_window = []
for val in logic_flow:
    if val % 2 == 1:
        rolling_window.append(val * 2)
    else:
        rolling_window.append(val // 2)

# Nested conditional with multiple branches (some irrelevant)
adjustment_factor = 1.0
if len(rolling_window) > 5:
    if sum(rolling_window) % 2 == 0:
        adjustment_factor = 1.2
    elif max(rolling_window) < 10:
        adjustment_factor = 0.9
    else:
        adjustment_factor = 1.05
else:
    adjustment_factor = 0.8

# Final processing using lambda and dictionary lookup
lookup_map = {1: 3, 2: 1, 3: 4, 4: 1, 5: 5, 6: 9}
processed_values = []
for v in rolling_window:
    key = v % 6 if v % 6 != 0 else 6
    processed_values.append(lookup_map[key] * adjustment_factor)

# Integration step with hidden rounding behavior
intermediate_total = 0
for idx, val in enumerate(processed_values):
    if idx % 3 == 0:
        intermediate_total += math.ceil(val)
    elif idx % 3 == 1:
        intermediate_total += int(val)
    else:
        intermediate_total += math.floor(val)

# Final diagnostic calculation (key statement)
final_diagnostic = int(intermediate_total + coherence_score) % 10000

# Output result as required
print(f"Result: {final_diagnostic}")