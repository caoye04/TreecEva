def apply_transformations(sequence, filter_mask):
    processed = 0
    for char in sequence:
        if char.isalpha():
            processed += ord(char) & filter_mask
    return processed

# Irrelevant helper (minimal distraction)
def reverse_string(s):
    return s[::-1]

data = "X9Lm2Z"
mask = 15
result = apply_transformations(data, mask)
print(f"Target result: {result}")