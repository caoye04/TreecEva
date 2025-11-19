sensor_readings = [23, 45, 67, 89, 12, 34]
modulus_base = 17
transformed_values = [reading % modulus_base for reading in sensor_readings]
checksum = sum(transformed_values) % modulus_base
print(f"Result: {checksum}")