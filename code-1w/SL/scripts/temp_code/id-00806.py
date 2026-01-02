def transform_data(data):
    shift_op = lambda x: x << 2
    filtered = [x for x in data if x % 3 == 0]
    shifted = [shift_op(val) for val in filtered]
    return sum(shifted) // len(shifted) if shifted else 0

raw_input = list(range(10, 45, 3))
processed_chunk = raw_input[1:10:2]
# Some auxiliary variables (minimal distraction)
temp_sum = sum(raw_input)
size_hint = len(raw_input)
result = transform_data(processed_chunk)
print(f"Target result: {result}")