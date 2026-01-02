from collections import Counter
text = "ProgrammingInPythonIsFun"

# Extract lowercase letters and count frequency
lowercase_letters = [c for c in text if c.islower()]
frequency = Counter(lowercase_letters)

# Get unique lowercase letters
unique_letters = set(lowercase_letters)

# Compute checksum using modular arithmetic on ASCII values
checksum = sum(ord(c) for c in text) % 17

# Final computation
result = len(unique_letters) * (checksum % 5)

print(f"Target result: {result}")