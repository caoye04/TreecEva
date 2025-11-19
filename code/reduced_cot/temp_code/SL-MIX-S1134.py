from collections import deque

def process_signal(samples):
    window = deque(maxlen=5)
    weighted_sum = 0
    
    for i, sample in enumerate(samples):
        window.append(sample)
        if len(window) == 5:
            temp_sum = 0
            for j, val in enumerate(window):
                weight = (j * 3 + 1) % 7
                temp_sum += val * weight
            weighted_sum = temp_sum % 1000
    
    return weighted_sum

signal_samples = [3, 7, 2, 8, 1, 9, 4, 6, 5, 0, 11, 13]
final_weighted_sum = process_signal(signal_samples)
print(f"Result: {final_weighted_sum}")