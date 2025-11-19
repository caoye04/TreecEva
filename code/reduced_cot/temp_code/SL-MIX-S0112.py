from itertools import permutations

# Initial signal mask
signal_mask = 15

# Apply transformations
transformed_signal = signal_mask ^ 9
transformed_signal <<= 2
transformed_signal &= 60

# Find positions of set bits
set_bit_positions = []
for i in range(8):
    if transformed_signal & (1 << i):
        set_bit_positions.append(i)

# Calculate number of 2-signal ordered combinations
if len(set_bit_positions) >= 2:
    test_combinations = len(list(permutations(set_bit_positions, 2)))
else:
    test_combinations = 0

print(f"Result: {test_combinations}")