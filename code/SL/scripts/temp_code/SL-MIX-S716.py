import base64
import statistics

temp_readings_celsius = [22, 25, 27, 24, 23, 26, 28]
encoded_readings = base64.b64encode(str(temp_readings_celsius).encode('utf-8'))
decoded_readings = eval(base64.b64decode(encoded_readings).decode('utf-8'))
temp_variance = statistics.variance(decoded_readings)
print(f'Result: {temp_variance}')