import hashlib
from statistics import mean

temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9]

with open('temp_log.txt', 'w') as f:
    for temp in temperature_readings:
        f.write(str(temp) + '\n')

hash_values = []
with open('temp_log.txt', 'r') as f:
    for line in f:
        temp_str = line.strip()
        hash_val = int(hashlib.md5(temp_str.encode()).hexdigest(), 16) % 1000
        hash_values.append(hash_val)

stability_index = int(mean(hash_values))
print(f'Result: {stability_index}')