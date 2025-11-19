def fibonacci_sequence(n):
    if n <= 1:
        return n
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

sensor_readings = [3.7, 5.1, 2.8, 9.3, 4.6]
fib_indices = [i for i in range(len(sensor_readings))]
fib_values = [fibonacci_sequence(i) for i in fib_indices]

transformed_readings = []
for i, reading in enumerate(sensor_readings):
    transformed_value = int(reading * 10) & fib_values[i]
    transformed_readings.append(transformed_value)

checksum = 0
for val in transformed_readings:
    checksum ^= val

selected_values = []
remaining = checksum
while remaining > 0:
    msb = 1 << (remaining.bit_length() - 1)
    selected_values.append(msb)
    remaining ^= msb

greedy_sum = sum(selected_values[:3])
checksum = checksum ^ greedy_sum

print(f"Result: {checksum}")