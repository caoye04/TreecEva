import itertools

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x ** 2 for x in data if x % 3 == 0]

# Misleading transformation chain
def decoy_transform(seq):
    temp = [x * 2 + 1 for x in seq]
    return [t for t in temp if t < 50]

# Actual core logic: recursive digit sum reduction
def recursive_digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + recursive_digit_sum(n // 10)

# Secondary distraction: complex but unused filter
def prime_filter(nums):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True
    return [x for x in nums if is_prime(x)]

# Real processing pipeline
initial_seed = [1234, 5678, 9012, 3456]

# Step 1: Extract middle digits using slicing (relevant)
partial_extract = [str(num)[1:-1] for num in initial_seed]  # ['23','67','01','45']

# Step 2: Convert back to integers (relevant)
extracted_ints = [int(s) if s != '' else 0 for s in partial_extract]

# Step 3: Apply recursive digit sum to each (key step)
reduced_values = [recursive_digit_sum(val) for val in extracted_ints]

# Step 4: Transform via lambda with filtering (relevant)
transform_fn = lambda x: x * 3 if x > 5 else x + 2
transformed_data = list(map(transform_fn, reduced_values))

# Step 5: Add irrelevant itertools permutation (distractor)
perm_set = list(itertools.permutations([1, 2], 2))
dummy_matrix = [[a + b for a, b in perm_set] for _ in range(2)]  # Unused

# Step 6: Another red herring - min/max average distraction
max_val = max(transformed_data)
min_val = min(transformed_data)
avg_hack = (max_val + min_val) / 2
offset_guess = round(avg_hack) * 2  # Looks important, unused

# Step 7: Actual processing function
def process_sequence(data):
    # Nested conditional with slicing twist
    if len(data) >= 3:
        subset = data[1:3]  # Middle two
        acc = 0
        for i, val in enumerate(subset):
            if i % 2 == 0:
                acc += val * 2
            else:
                acc -= val
        # Final adjustment based on sum parity
        total = sum(data)
        if total % 2 == 0:
            acc += 5
        else:
            acc -= 3
        return acc
    else:
        return sum(data)

# Critical execution point
final_output = process_sequence(transformed_data)

# Print result as required
print(f"Target result: {final_output}")