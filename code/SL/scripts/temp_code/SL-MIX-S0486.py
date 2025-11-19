import collections

temp_readings_encoded = ['12', '76', '03', '45', '27']
base8_to_decimal_map = {str(i): i * 0.5 for i in range(8)}

decoded_deviations = [
    sum(base8_to_decimal_map[digit] * (8 ** idx) for idx, digit in enumerate(reversed(reading)))
    for reading in temp_readings_encoded
]

extreme_deviation = max(abs(dev) for dev in decoded_deviations)

print(f"Result: {extreme_deviation}")