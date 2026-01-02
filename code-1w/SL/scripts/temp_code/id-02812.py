def analyze_temperatures(temps):
    filtered = [t for t in temps if 15 < t < 30]
    scaled = [t * 1.8 + 32 for t in filtered]
    processed_data = scaled[::2]
    result = sum(processed_data)
    return result

# Sample temperature data in Celsius
temperature_celsius = [10, 16, 20, 25, 30, 14, 22, 28, 35]

result = analyze_temperatures(temperature_celsius)
print(f"Result: {result}")