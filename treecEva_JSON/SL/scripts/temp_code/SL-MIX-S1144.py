from collections import deque

# Spectral peak data (intensity values)
peak_intensities = [45, 22, 68, 19, 73, 34, 55, 28, 61, 47]
window_size = 4
decay_factor = 0.85
trigger_threshold = 200

# Initialize tracking structures
history_buffer = deque(maxlen=window_size)
signal_energy = 0
processed_count = 0

for idx, intensity in enumerate(peak_intensities):
    # Apply decay to existing values in buffer
    history_buffer = deque([val * decay_factor for val in history_buffer], maxlen=window_size)
    
    # Add new intensity
    history_buffer.append(intensity)
    processed_count += 1
    
    # Calculate current window sum
    window_sum = sum(history_buffer)
    
    # Update energy with weighted contribution
    signal_energy += int(window_sum * (0.9 ** processed_count))
    
    # Early termination condition
    if processed_count >= 3 and window_sum > trigger_threshold:
        signal_energy = int(signal_energy * 1.5)
        break
    
    # Periodic normalization
    if processed_count % 5 == 0:
        signal_energy = int(signal_energy * 0.95)

print(f"Result: {signal_energy}")