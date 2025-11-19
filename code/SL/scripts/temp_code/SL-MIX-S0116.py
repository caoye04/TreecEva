from collections import deque

def compute_signal_checksum(signal_samples):
    window = deque(maxlen=5)
    checksum = 0
    
    for idx, sample in enumerate(signal_samples):
        window.append(sample)
        
        # Only compute checksum when window is full
        if len(window) == 5:
            # Weighted sum with position-based weights
            weighted_sum = sum((i + 1) * val for i, val in enumerate(window))
            # Apply modular arithmetic with floating point adjustment
            mod_result = (weighted_sum % 17) + (idx * 0.5)
            # Logical condition for checksum update
            if mod_result > 10.0 and not (idx % 3 == 0 and idx > 15):
                checksum = (checksum + int(mod_result)) % 100
            elif mod_result <= 10.0 or (idx > 10 and idx < 20):
                checksum = (checksum ^ int(mod_result)) % 100
    
    return checksum

# Process a sequence of signal samples
signal_data = [12, 7, 23, 9, 15, 4, 18, 11, 6, 25, 3, 20, 8, 14, 19, 5, 22, 10, 17, 1]
processed_checksum = compute_signal_checksum(signal_data)
print(f"Result: {processed_checksum}")