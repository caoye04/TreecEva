from collections import defaultdict
import math

# Simulated bio-signal processing pipeline with decoy analytics
def analyze_waveform(signal_data):
    if not signal_data:
        return 0
    
    # Irrelevant spectral analysis (dead path for this input)
    peak_frequency = max(signal_data) % 7
    phase_shift = sum([x ** 0.5 for x in signal_data if x > 3])
    coherence_score = len([x for x in signal_data if x % 2 == 0])

    # Real computation buried in noise
    base_energy = sum(signal_data) // len(signal_data)
    return base_energy + (peak_frequency * 0)  # Neutralized red herring

# Decoy function - never called but looks important
def compute_resonance(channels, mode='lfo'):
    resonance_grid = defaultdict(int)
    for c in channels:
        for i in range(len(c)):
            resonance_grid[i] += c[i] * 0.1
    return {k: v for k, v in resonance_grid.items() if v > 0.5}

# Core transformation logic
def generate_signature(raw_readings):
    temp_buffer = []
    adjustment_factor = 3
    
    for val in raw_readings:
        if val < 0:
            continue
        # Meaningful transformation
        transformed = int(math.log(val + 1) * adjustment_factor)
        temp_buffer.append(transformed)
    
    # Distractor: unused normalization
    normalized = [round(x / max(temp_buffer), 3) for x in temp_buffer if max(temp_buffer) > 0]
    
    # Actual output
    return [x * 2 for x in temp_buffer]  # doubles each element

# Misleading auxiliary processor (looks like it's used)
def evaluate_stability(indices):
    if len(indices) < 5:
        return 'UNSTABLE'
    cumulative = 0
    for i, idx in enumerate(indices):
        if i % 3 == 0:
            cumulative -= idx
        else:
            cumulative += idx * 0.5
    return str(cumulative)[:4]

# Main diagnostic engine
def process_metrics(signature, thresholds):
    diagnostic_code = 1000
    activation_level = 0
    decay_constant = 0.8
    
    # Real logic starts here
    for i, sig_val in enumerate(signature):
        if i in thresholds:
            if sig_val > thresholds[i]:
                activation_level += sig_val * (i + 1)
            else:
                activation_level -= 5
    
    # Red herring: complex-looking but unused calculation
    entropy = 0
    count_map = defaultdict(int)
    for x in signature:
        count_map[x] += 1
    for v in count_map.values():
        if v > 0:
            entropy -= v * math.log(v)
    
    # Another decoy operation
    inverted_index = {v: k for k, v in enumerate(signature) if k % 2 == 0}
    checksum = sum(inverted_index.keys()) if inverted_index else 0

    # Final computation - only this matters
    diagnostic_code += int(activation_level * decay_constant)
    
    # Dead branch - distractor
    if diagnostic_code > 2000:
        fallback = ''.join([chr(diagnostic_code % 127)] * 3)
        diagnostic_code = len(fallback)

    return diagnostic_code

# Primary execution flow
if __name__ == "__main__":
    # Input data
    sensor_stream = [15, 25, 30, 45, 12, 8, 20]
    
    # Generate health signature (key step)
    health_signature = generate_signature(sensor_stream)
    
    # Build threshold map (critical parameter)
    threshold_map = defaultdict(int)
    for idx, val in enumerate(health_signature):
        threshold_map[idx] = val - (idx * 2)  # dynamic threshold
    
    # Update specific threshold to alter control flow
    threshold_map[3] = 12
    
    # Analyze waveform (irrelevant side computation)
    aux_signal = [4, 6, 8, 10]
    wave_diagnostic = analyze_waveform(aux_signal)
    
    # Final evaluation
    final_diagnostic = process_metrics(health_signature, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")