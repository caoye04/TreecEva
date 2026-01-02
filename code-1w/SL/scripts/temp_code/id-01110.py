def apply_calibration(signal, flag):
    adjust = lambda x, f: round(x * 1.05) if f else round(x * 0.95)
    return adjust(signal, flag)

raw_signal = 897
base_offset = 42  # Irrelevant variable (minimal interference)
activation_threshold = 900

# Determine flag state using bitwise and relational logic
is_active = (raw_signal + 5) > activation_threshold
flag_modifier = 0b1010 ^ 0b1100  # XOR operation for bit pattern
bit_filtered = flag_modifier & 0b0011
threshold_flag = is_active or (bit_filtered == 2)

# Final computation depending on threshold_flag
final_diagnostic = apply_calibration(raw_signal, threshold_flag)
print(f"Result: {threshold_flag}")