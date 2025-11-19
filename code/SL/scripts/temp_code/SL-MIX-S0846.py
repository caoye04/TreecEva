import math
import statistics

temp_readings_f = [78, 82, 85, 79, 81, 83, 80]
temp_readings_c = [(f - 32) * 5/9 for f in temp_readings_f]
normalized_data = [math.log2(c + 273.15) for c in temp_readings_c]  # Convert to Kelvin then log2
variance = statistics.variance(normalized_data)
status_message = f"Variance: {variance:.4f}"
encoded_status = sum(ord(char) * (2 ** idx) for idx, char in enumerate(status_message))
print(f"Result: {encoded_status}")