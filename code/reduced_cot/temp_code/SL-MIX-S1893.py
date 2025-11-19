def signal_modulator(func):
    def wrapper(signal):
        modulated = func(signal)
        return modulated & 0xFF
    return wrapper

@signal_modulator
def amplify_signal(base_signal):
    return base_signal * 3

initial_signal = 42
register_a = {1, 3, 5, 7, 9}
register_b = frozenset([2, 4, 6, 8, 10])
composite_register = dict.fromkeys(range(5), 0)

for i in range(3):
    if (i % 2 == 0) and (initial_signal > 20):
        temp_val = (amplify_signal(initial_signal) >> i) + len(register_a.symmetric_difference(register_b))
    else:
        temp_val = (initial_signal << i) - (not bool(register_a & register_b))
    
    composite_register[i] = temp_val % 17

final_signal_strength = sum(composite_register.values())
print(f'Result: {final_signal_strength}')