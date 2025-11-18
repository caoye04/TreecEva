from collections import defaultdict

def process_signal(encoded_values):
    state = 0
    decoded_signal = 0.0
    state_transitions = defaultdict(lambda: 0)
    
    for idx, val in enumerate(encoded_values):
        if state == 0:
            if val & 0x1:
                state = 1
                decoded_signal += (val ^ 0xF) * 0.5
            else:
                decoded_signal -= val >> 1
        elif state == 1:
            if val & 0x2:
                state = 2
                decoded_signal *= 1.5
            else:
                decoded_signal += val & 0x7
        elif state == 2:
            if val & 0x4:
                state = 0
                decoded_signal /= 2.0
            else:
                decoded_signal -= val | 0x3
        state_transitions[state] += 1
    return decoded_signal

signal_sequence = [7, 3, 6, 12, 5, 9]
decoded_signal = process_signal(signal_sequence)
print(f"Result: {decoded_signal}")