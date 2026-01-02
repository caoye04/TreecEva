def analyze_pattern(values):
    processed = [x for x in values if x % 2 == 1]  # Keep odd numbers
    shifted = [x ^ 3 for x in processed]  # Bitwise XOR with 3
    total = sum(shifted)
    result = total // len(shifted) if shifted else 0
    return result

data = [12, 15, 22, 33, 40, 47]
result = analyze_pattern(data)
print(f"Target result: {result}")