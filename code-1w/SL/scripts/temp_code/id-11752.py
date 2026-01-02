temperature_data = [23.5, 19.0, 17.3, 21.8, 26.1, 30.0, 24.7]
base_value = 100
threshold = 4

# Extract subset of temperatures and reverse to find latest in range
data_slice = temperature_data[2:5]  # Days 3-5 readings
reversed_slice = data_slice[::-1]   # Most recent first
current_peak = reversed_slice[0]

result = current_peak * threshold > base_value

print(f"Result: {result}")