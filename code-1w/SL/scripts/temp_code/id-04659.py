from collections import defaultdict

# Simulate multi-phase signal processing with noise filtering and state tracking
raw_signals = [3, 7, 2, 8, 4, 9, 1, 5]
noise_floor = 2
detected_peaks = []
peak_magnitudes = defaultdict(int)
processing_log = []

for i, signal in enumerate(raw_signals):
    if signal > noise_floor:
        detected_peaks.append(i)
        peak_magnitudes['high'] += signal
        processing_log.append(f'Peak at {i}: {signal}')
    elif signal == noise_floor:
        peak_magnitudes['medium'] += signal
    else:
        peak_magnitudes['low'] += signal

# Initialize transformation passes
transformed = [0] * len(detected_peaks)
for idx, pos in enumerate(detected_peaks):
    transformed[idx] = raw_signals[pos] ^ (pos & 3)  # XOR with position mask

# Begin iterative refinement phase
refinement_steps = 0
equilibrium_score = 0
history = []

for epoch in range(3):
    forward_pass = []
    backward_pass = []
    
    for j, val in enumerate(transformed):
        shifted = val << 1
        masked = shifted & 15
        if j % 2 == 0:
            forward_pass.append(masked + epoch)
        else:
            backward_pass.append(masked - epoch)
    
    # Introduce auxiliary computation (distractor)
    temp_analysis = list(zip(forward_pass[::2], backward_pass[::-2] if len(backward_pass) > 1 else [0]))
    avg_coupling = sum([a ^ b for a, b in temp_analysis]) / max(len(temp_analysis), 1)
    
    # Key computational statement
    equilibrium_score = abs(sum(forward_pass) - sum(backward_pass)) // (epoch + 1)
    
    # Log intermediate state (not used later)
    history.append({'epoch': epoch, 'score': equilibrium_score, 'coupling': avg_coupling})
    refinement_steps += 1

# Final adjustment based on peak count (irrelevant to final score but adds logic path)
if len(detected_peaks) > 5:
    equilibrium_score -= 10
else:
    equilibrium_score += 5

# Print result as required
print(f'Result: {equilibrium_score}')