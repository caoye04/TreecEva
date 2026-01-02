def process_sequence(seq):
    filtered = seq[1:-1]  # Remove first and last elements
    doubled = [x * 2 for x in filtered]
    summed = sum(doubled)
    threshold = 10
    adjusted = summed + (5 if summed > threshold else -3)
    return adjusted

# Irrelevant auxiliary data (minimal distraction)
temp_log = [0, 0, 0]
config_flag = True

data = [3, 1, 4, 1, 5, 9]
result = process_sequence(data)
print(f"Result: {result}")