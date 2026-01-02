import math

def preprocess_signals(raw_data, threshold=0.5):
    # Irrelevant signal processing function (dead code path)
    return [x for x in raw_data if abs(x) > threshold]


def calculate_entropy(stream):
    # Misleading entropy calculation (unused)
    prob = {x: stream.count(x) / len(stream) for x in set(stream)}
    return -sum(p * math.log2(p) for p in prob.values())


efficiency_factor = 0.87
voltage_rms = 230.0
frequency = 50
harmonics = [1, 3, 5, 7]

# Simulated transient load profile (complex setup with distractors)
base_load = 1250
fluctuation_pattern = [math.sin(i * frequency) for i in range(1, 6)]
transient_loads = []
for t in range(5):
    spike = 0
    if t == 2:
        spike = 320  # Temporary overload
    adjusted = base_load * (1 + fluctuation_pattern[t]) + spike
    transient_loads.append(int(adjusted))

# Dead computation branch - simulates thermal decay (never used)
thermal_decay = []
for i in range(len(transient_loads)):
    decay_value = transient_loads[i] * math.exp(-i * 0.3)
    thermal_decay.append(round(decay_value, 2))

# Red herring: fake neural weight adjustment (irrelevant)
weights = [0.1, 0.25, 0.5, 0.75, 0.9]
weight_adjustments = [w * math.tanh(voltage_rms / 1000) for w in weights]

# Real logic begins here — nested conditional with list comprehension
overload_count = 0
for load in transient_loads:
    if load > 1400:
        overload_count += 1

# Simulate control system feedback (distractor)
current_feedback = []
for i, load in enumerate(transient_loads):
    feedback = load * (0.95 + i * 0.01)
    current_feedback.append(feedback * efficiency_factor)

# Key function that computes the actual answer
def analyze_thermal_response(loads, eff):
    # Complex internal state simulation
    temp_state = 0
    peak_hold = 0
    history = []
    
    for val in loads:
        # Thermal inertia model
        temp_state += val * 0.2
        if temp_state > peak_hold:
            peak_hold = temp_state
        temp_state *= 0.7  # Cooling factor
        history.append(round(temp_state, 1))
    
    # Secondary processing with list comprehension (core relevant logic)
    filtered_history = [h for h in history if h > 300]
    cumulative_trace = sum(filtered_history) * eff
    
    # Final transformation
    if len(filtered_history) > 2:
        cumulative_trace -= 150
    else:
        cumulative_trace += 50
    
    # Decoy operation: bit manipulation (unused result)
    masked = int(cumulative_trace) ^ 0xFF
    inverted = ~masked & 0xFFFF
    
    return int(cumulative_trace)

# Unused diagnostic function (red herring)
def generate_diagnostic_report(data):
    report = {'size': len(data), 'max': max(data), 'checksum': sum(d % 7 for d in data)}
    return report

# Unused tensor-like structure (distractor)
mock_tensor = [[[i+j+k for k in range(2)] for j in range(2)] for i in range(3)]

# Critical execution point
thermal_capacity = analyze_thermal_response(transient_loads, efficiency_factor)

# Final print statement as required
print(f"Result: {thermal_capacity}")