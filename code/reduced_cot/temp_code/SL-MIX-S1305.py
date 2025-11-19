import statistics

temp_readings_hex = ['0x1A', '0x2B', '0x1F', '0x30', '0x22']
temp_readings_dec = [int(hex_val, 16) for hex_val in temp_readings_hex]
average_temp = statistics.mean(temp_readings_dec)
print(f'Result: {average_temp}')