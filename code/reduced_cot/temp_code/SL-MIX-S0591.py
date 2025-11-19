def mod_encoder(value, modulus):
    return (value * 3 + 7) % modulus

sensor_readings = [15, 22, 8, 31]
modulus_base = 10
encoded_signal = 0

for reading in sensor_readings:
    encoded_signal = mod_encoder(reading, modulus_base)
    
print(f"Result: {encoded_signal}")