import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return x ** 3 + 2 * x - 1

# Misleading signal generator with decoy logic
def generate_noise(length):
    signal = []
    for i in range(length):
        if i % 5 == 0:
            signal.append(i * 0.1)
        elif i % 3 == 0:
            signal.append(-i * 0.05)
        else:
            signal.append(0.0)
    return signal

# Distractor: complex but unused filter chain
class FilterBank:
    def __init__(self):
        self.filters = [lambda x: x * 0.1, lambda x: x + 2, lambda x: abs(x)]

    def apply_all(self, data):
        result = data.copy()
        for f in self.filters:
            result = [f(x) for x in result]
        return result

# Real processing begins here
raw_input_stream = [8, 12, 16, 4, 20, 24]
scaling_factor = 1.5
amplified = [x * scaling_factor for x in raw_input_stream]  # [12.0, 18.0, 24.0, 6.0, 30.0, 36.0]

# Apply non-linear transformation (relevant)
transformed = []
for val in amplified:
    if val > 20:
        transformed.append(math.log(val, 2))
    else:
        transformed.append(math.sqrt(val))

# transformed = [sqrt(12), sqrt(18), log2(24), sqrt(6), log2(30), log2(36)]
# ≈ [3.464, 4.243, 4.585, 2.449, 4.907, 5.170]

# Decoy list comprehension with no side effects
decoys = [x for x in transformed if x < 4.0]

# Actual data pipeline
buffer = set(transformed)  # Use of set operation (required feature)
threshold_set = {x for x in buffer if x > 4.0}  # Another set comprehension

processed_data = list(threshold_set)  # [4.243, 4.585, 4.907, 5.170]
processed_data.sort(reverse=True)  # Sorted descending: [5.170, 4.907, 4.585, 4.243]

# Simulated diagnostic analysis using lambda (required feature)
analyze_component = lambda x: (x ** 2) / 3.5

# Real analysis function with embedded distractions
def analyze_signal(data):
    temp_results = {}
    cumulative = 0
    
    # Red herring loop (no effect on output)
    for i in range(len(data)):
        temp = data[i] * (i + 1)
        temp_results[f'temp_{i}'] = temp  # Stored but never used
    
    # Actual computation path
    weights = [0.1, 0.2, 0.3, 0.4]
    weighted_sum = 0
    
    for i in range(len(data)):
        if i % 2 == 0:
            weighted_sum += data[i] * weights[i]
        else:
            # Apply lambda transform on odd indices
            weighted_sum += analyze_component(data[i]) * weights[i]
    
    # Final nonlinear adjustment
    final_score = math.sin(weighted_sum) * 1000
    
    # Misleading assignment
    diagnostic_code = 'SIG_HIGH'
    
    # Key result
    final_diagnostic = int(round(final_score))
    
    # Dead code: unreachable under normal execution
    if False:
        backup = sum(data) / len(data)
        final_diagnostic = int(backup * 10)
    
    return final_diagnostic

# Execute main logic
final_diagnostic = analyze_signal(processed_data)

# Print result as required
print(f"Target result: {final_diagnostic}")