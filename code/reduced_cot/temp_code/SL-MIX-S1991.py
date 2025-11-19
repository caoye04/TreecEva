import heapq
import itertools

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def rotate_string(s, n):
    if not s:
        return s
    n = n % len(s)
    return s[n:] + s[:n]

def calculate_defect_score(batch_id):
    # Sum of ASCII values of letters minus sum of digits
    letter_sum = sum(ord(c) for c in batch_id if c.isalpha())
    digit_sum = sum(int(c) for c in batch_id if c.isdigit())
    return letter_sum - digit_sum

# Initialize tracking structures
batch_identifiers = ['BRAVO7', 'ALPHA3', 'DELTA9', 'GAMMA1', 'EPSILON5', 'ZETA2', 'THETA8', 'IOTA4']
fib_gen = fibonacci_sequence(len(batch_identifiers))
defect_heap = []

# Process each batch
for batch_id in batch_identifiers:
    fib_number = next(fib_gen)
    # Apply string transformation
    transformed_id = rotate_string(batch_id, fib_number)
    # Calculate and push defect score
    score = calculate_defect_score(transformed_id)
    heapq.heappush(defect_heap, score)

# After all batches processed, find minimum defect score
final_min_defect = defect_heap[0] if defect_heap else 0
print(f"Result: {final_min_defect}")