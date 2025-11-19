def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def fib_mod(n, mod_val=1000):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, (a + b) % mod_val
    return b

correction_factor = lambda x: (x**2 + 1) % 100

signal_sequence = []
for i in range(20):
    base_signal = fib_mod(i)
    if i % 3 == 0 and i != 0:
        corrected_signal = correction_factor(base_signal)
        signal_sequence.append(corrected_signal)
    else:
        signal_sequence.append(base_signal)

# Dictionary comprehension to map prime indices to their signal values
peaks_map = {i: signal_sequence[i] for i in range(len(signal_sequence)) if is_prime(i)}

# Sum all peak signal values
peak_sum = sum(peaks_map.values())
print(f"Result: {peak_sum}")