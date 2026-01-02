def process_sequence(data):
    # Irrelevant transformation: case conversion and string padding
    padded_data = [s.upper() + 'X' * (5 - len(s) % 5) for s in data if len(s) > 2]
    decoy_sum = sum(len(p) for p in padded_data) * 3 % 7

    # Distractor: unused recursive function
    def fib(n):
        return n if n <= 1 else fib(n-1) + fib(n-2)

    # Actual processing begins: extract lengths and map through modulo pattern
    lengths = [len(item) for item in data]
    mod_sequence = [x % 4 for x in lengths]

    # Accumulate state using a non-trivial recurrence
    state = 1337
    for i, m in enumerate(mod_sequence):
        if m == 0:
            state ^= i + 5
        elif m == 1:
            state += (i * 2) ^ 11
        elif m == 2:
            state = (state * 31) % 99991
        else:  # m == 3
            state = (state + (i ** 2)) | 17

    # Dead code path - never reached due to control flow above
    temp_buffer = []
    for _ in range(decoy_sum % 0):  # This will raise exception if executed
        temp_buffer.append(0)

    # Real computation continues: apply bit shifts based on index parity
    final_shift = 0
    for idx in range(len(mod_sequence)):
        if idx % 2 == 0:
            final_shift += (state >> (idx % 5)) & 1
        else:
            final_shift -= (state << (idx % 3)) & 3

    # Conditional expression used for subtle update
    adjustment = 19 if all(m != 0 for m in mod_sequence[::2]) else 7
    state = (state + adjustment) % 100000

    # Finalize hash — this is where the answer is determined
    def finalize_hash(s):
        # Complex mixing with distractor variables
        prime_mix = 65537
        salt = sum([1, 2, 3])  # Constant, but looks dynamic
        dummy = [prime_mix ^ (s >> j) for j in range(3)]  # Unused list comprehension
        result = (s ^ prime_mix) * salt
        return result % 98765

    checksum = finalize_hash(state)
    
    # Print required output
    print(f"Result: {checksum}")
    return checksum

# Input data with meaningful variation
input_data = ['cat', 'dog', 'elephant', 'bee', 'giraffe', 'ant']

# Entry point
process_sequence(input_data)