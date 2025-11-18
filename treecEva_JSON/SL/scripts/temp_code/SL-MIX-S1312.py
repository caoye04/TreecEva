from functools import reduce

def adaptive_filter(input_samples, coeff_map):
    memory_taps = {k: 0 for k in range(-3, 1)}
    processed_signal = 0
    
    def recursive_tap(n, x_n):
        if n < 0:
            return memory_taps[n]
        else:
            feedback = sum(coeff_map[f'b{i}'] * recursive_tap(n-i, input_samples[n-i]) for i in range(1, 4) if n-i >= 0)
            feedforward = coeff_map['a0'] * x_n
            result = feedforward + feedback
            memory_taps[0] = result
            for j in range(-1, -4, -1):
                memory_taps[j] = memory_taps[j+1]
            return result
    
    for idx in range(len(input_samples)):
        processed_signal = recursive_tap(idx, input_samples[idx])
    return processed_signal

signal_coefficients = {'a0': 0.5, 'b1': 0.3, 'b2': 0.15, 'b3': 0.05}
input_sequence = [100, 50, 25, 12.5, 6.25]
target_result = adaptive_filter(input_sequence, signal_coefficients)
print(f'Result: {target_result}')