data_bits = 0b1101
mask = 0b1011
check_flag = 1
result = data_bits ^ mask
final_value = (data_bits & mask) | (check_flag << 2)
print(f"Result: {final_value}")