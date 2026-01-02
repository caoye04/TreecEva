from itertools import cycle

# Simulate sensor data stream and validation checks
current_state = 73
reference_value = 41

# Bitwise condition: check if 3rd and 5th bits differ between state and reference
bit_condition = ((current_state >> 2) & 1) ^ ((reference_value >> 4) & 1)

# Simulated signal string from device
signal_str = "SYNC_ACK_READY"

# String condition: check for presence of critical substrings
string_condition = signal_str.startswith("SYNC") and "READY" in signal_str and signal_str.count("_") >= 2

# Combine conditions with logical negation
threshold_flag = not (bit_condition or string_condition)

# Irrelevant distraction: cycling through dummy states (no effect on logic)
dummy_states = [10, 20, 30]
cycler = cycle(dummy_states)
for _ in range(3):
    next(cycler)

# Output result
print(f"Result: {threshold_flag}")