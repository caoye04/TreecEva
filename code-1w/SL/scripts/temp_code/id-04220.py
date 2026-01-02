def calculate_checksum(sequence):
    checksum = 0
    for index, value in enumerate(sequence):
        if index % 2 == 0:
            checksum += value << 1
        else:
            checksum ^= value
    return checksum

data = [12, 10, 8, 6, 4, 2]
offset = 3
multiplier = 2

# Irrelevant variable (minimal distraction)
temp_result = [x * multiplier for x in data[::2]]

result = calculate_checksum(data)
print(f"Result: {result}")