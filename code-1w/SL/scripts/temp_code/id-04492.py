import math

def analyze_frequency(signal_data, base_freq):
    scaled = [x * base_freq for x in signal_data]
    adjusted = [math.sin(x) + 0.1 * x for x in scaled]
    return sum(adjusted)

def shift_elements(arr, shift_by):
    if shift_by == 0:
        return arr
    return arr[-shift_by:] + arr[:-shift_by]

def calculate_entropy(data):
    # Irrelevant helper function (dead code path in this context)
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return round(entropy, 3)

def process_phases(phases, accumulator):
    temp_result = 0
    phase_copy = phases[:]
    
    for i in range(len(phase_copy)):
        if i % 2 == 0:
            temp_result += math.cos(phase_copy[i])
        else:
            temp_result -= math.sin(phase_copy[i])
    
    # Conditional expression used here (required Python feature)
    scaling_factor = 2 if temp_result > 0 else 0.5
    
    accumulator *= scaling_factor
    accumulator += temp_result
    
    # Some misleading manipulation
    accumulator = int(accumulator) + 10  # Add arbitrary offset
    accumulator -= 10  # Neutralize it (distractor)
    
    return accumulator

# Main execution
base_phases = [0.1, 0.3, 0.7, 1.2, 1.8]
frequency_signal = [0.5, 1.0, 1.5, 2.0]

# Irrelevant pre-computations (distractors)
raw_entropy = calculate_entropy([1, 2, 2, 3, 3, 3])
skewed_signal = shift_elements(frequency_signal, 2)
analyzed_power = analyze_frequency(frequency_signal, 50)

# Key state initialization
net_phase_shift = 3.0

# Core logic chain
for angle in base_phases:
    if angle < 1.0:
        net_phase_shift += angle ** 2
    else:
        net_phase_shift -= math.log(angle)

# Final adjustment step (critical execution point)
final_adjustment = process_phases(base_phases, net_phase_shift)

# Update and print result
net_phase_shift = final_adjustment
print(f"Result: {net_phase_shift}")