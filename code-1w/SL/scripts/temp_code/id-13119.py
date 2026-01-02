from collections import defaultdict

def calculate_checksum(data):
    freq_map = defaultdict(int)
    for char in data:
        freq_map[char] += 1
    
    # Compute weighted sum using character frequencies and ASCII values
    weighted_sum = 0
    for char, count in freq_map.items():
        weighted_sum += ord(char) * count
    
    # Apply bit manipulation to final sum
    temp = weighted_sum ^ 0xAAAA
    result = (temp + (temp >> 4)) & 0xFFFF
    return result

# Irrelevant utility function (minimal distraction)
def reverse_string(s):
    return s[::-1]

# Input data
data = "abccba"

# Key computation
result = calculate_checksum(data)
print(f"Result: {result}")