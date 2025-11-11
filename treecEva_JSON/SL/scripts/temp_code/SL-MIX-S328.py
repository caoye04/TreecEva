import math

def calculate_trace(matrix):
    return sum(matrix[i][i] for i in range(min(len(matrix), len(matrix[0]))))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Instrument metadata
instruments = [
    {'id': 12, 'data': [[4, 2], [1, 3]]},
    {'id': 15, 'data': [[5, 0, 2], [1, 6, 3], [4, 2, 1]]},
    {'id': 17, 'data': [[9, 3], [2, 7]]},
    {'id': 21, 'data': [[8, 1, 0], [3, 2, 4], [1, 0, 5]]},
    {'id': 25, 'data': [[3, 7], [5, 2]]}
]

# Validation sets
required_primes = frozenset([2, 3, 5, 7, 11, 13, 17, 19, 23])
forbidden_ids = {14, 16, 18, 20, 22, 24}

valid_instrument_count = 0

for instrument in instruments:
    id_value = instrument['id']
    matrix_data = instrument['data']
    
    # Check if ID is not in forbidden set AND (ID is prime OR trace is prime)
    trace_value = calculate_trace(matrix_data)
    id_is_valid = id_value not in forbidden_ids
    id_or_trace_is_prime = is_prime(id_value) or is_prime(trace_value)
    
    # Additional check: if matrix dimensions are square
    is_square_matrix = len(matrix_data) == len(matrix_data[0])
    
    # Final validation: combine all conditions
    if id_is_valid and id_or_trace_is_prime and is_square_matrix:
        # Extra condition: check if trace intersects with required primes
        trace_in_required = trace_value in required_primes
        if trace_in_required or (id_value % 3 == 0):
            valid_instrument_count += 1

# Dictionary comprehension for verification (not used in count but part of validation)
verification_map = {inst['id']: calculate_trace(inst['data']) for inst in instruments}

print(f"Result: {valid_instrument_count}")