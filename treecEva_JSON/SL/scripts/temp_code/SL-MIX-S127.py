import math

def process_data(arr):
    transformed = []
    for i in range(len(arr)):
        if i % 2 == 0:
            transformed.append(arr[i] ** 2)
        else:
            transformed.append(math.sqrt(abs(arr[i])))
    return transformed

def aggregate_stats(data):
    total_sum = sum(data)
    avg = total_sum / len(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return {
        'sum': total_sum,
        'average': avg,
        'std_dev': std_dev,
        'min': min(data),
        'max': max(data)
    }

def encode_string(s):
    encoded = ''
    for char in s:
        if char.isalpha():
            shifted = chr(((ord(char.lower()) - ord('a') + 5) % 26) + ord('a'))
            encoded += shifted.upper() if char.isupper() else shifted
        else:
            encoded += char
    return encoded

data_points = [4, -9, 16, -25, 36, -49, 64]
processed_data = process_data(data_points)
stats = aggregate_stats(processed_data)
secret_key = "XyZ123!@#"
encoded_key = encode_string(secret_key)

# Calculate intermediate values
A = int(stats['sum'])
B = int(stats['std_dev'] * 100)  # Scale up for integer precision
C = len(encoded_key)
D = sum(ord(c) for c in encoded_key)

# Perform bit operations
E = (A & 0xFF) ^ (B | 0xF0)
F = (C << 4) + (D >> 2)

# Final computation
final_result = ((E * F) % 10000) + int(math.log(D, 2) * 100)
print(f"Result: {final_result}")