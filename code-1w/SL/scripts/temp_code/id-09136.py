def calculate_modular_sum(stream, mod_base):
    weighted_sum = 0
    for index, value in enumerate(stream):
        weight = (index + 1) % 5
        contribution = (value * weight) % mod_base
        weighted_sum = (weighted_sum + contribution) % mod_base
    return weighted_sum

# Simulated sensor data stream
data_stream = [23, 67, 88, 45, 12, 91, 34]
base = 17

# Auxiliary unrelated tracking (minimal interference)
count_high = 0
for val in data_stream:
    if val > 50:
        count_high += 1

# Core computation
temp_result = sum(data_stream) % base
interim = (temp_result * 2) % base

# Key statement
final_checksum = calculate_modular_sum(data_stream, base)

print(f"Target result: {final_checksum}")