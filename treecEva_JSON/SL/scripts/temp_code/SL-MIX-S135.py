def compute_depth(s, current=0):
    if not s:
        return current
    return compute_depth(s[:-1], current + 1)

input_text = 'hello world'
depth_value = compute_depth(input_text)
hashed_value = hash(input_text) % 1000
signature_result = hashed_value + depth_value
print(f'Result: {signature_result}')