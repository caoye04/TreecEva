import itertools

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def calculate_fibonacci(n):
    """Generate nth Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Generate initial sequence based on bit operations
def generate_sequence(length):
    """Generate a sequence using bit operations."""
    sequence = []
    base = 10
    for i in range(length):
        # Distractor calculations
        distractor = (i << 2) | (i >> 1)
        irrelevant = (i & 0x3) * (i | 0x5)
        
        # The actual calculation uses a simple formula
        value = (i + base) ^ (i & base)
        sequence.append(value)
    return sequence

# Process sequence through filters
def filter_sequence(seq):
    """Apply various filters to the sequence."""
    # Misleading filter that seems important but isn't used
    complex_filter = lambda x: (x % 3 == 0) and (x % 5 != 0)
    
    # Generate some Fibonacci numbers as distractors
    fib_numbers = [calculate_fibonacci(i) for i in range(8)]
    
    # Distractor sequence transformations
    transformed = list(map(lambda x: x * 2 - 3, seq))
    
    # The actual filtering logic
    filtered = [x for x in seq if x > 5 and x < 20]
    
    # More distraction with itertools
    all_permutations = list(itertools.permutations([1, 2, 3], 2))
    all_combinations = list(itertools.combinations(range(4), 2))
    
    # Distractor calculation that looks important
    magic_number = sum(fib_numbers) & 0xFF
    
    return filtered

def calculate_sequence_value(sequence):
    """Calculate a value from the sequence."""
    # Distractor operations with itertools
    cycle_iter = itertools.cycle([1, 2, 3, 4])
    cycle_values = [next(cycle_iter) for _ in range(10)]
    
    # Initialize result variables
    result = 1
    alternate_result = 0
    temp_result = 1
    
    # Process sequence with distractor calculations
    for idx, value in enumerate(sequence):
        # Distractor calculation path
        if idx % 3 == 0 and False:  # Never executes due to 'and False'
            alternate_result += value ** 2
            continue
            
        # Another distractor
        temp = (value << 1) if is_prime(value) else (value >> 1)
        
        # The actual calculation - multiply primes together
        if is_prime(value):
            result *= value
        
        # More distraction
        temp_result = temp_result * idx if idx > 0 else temp_result
    
    # Final distractor calculations
    binary_sum = sum(bin(x).count('1') for x in sequence)
    hex_representation = sum(int(hex(x)[2:], 16) for x in sequence if x > 10)
    
    return result

# Main execution
sequence_length = 15
initial_sequence = generate_sequence(sequence_length)

# Distractor variables
sequence_sum = sum(initial_sequence)
sequence_product = 1
for num in initial_sequence[:5]:
    sequence_product *= num
    
# Apply the filter
filtered_sequence = filter_sequence(initial_sequence)

# Calculate the final value
prime_product = calculate_sequence_value(filtered_sequence)

# More distractions
binary_representation = bin(prime_product)[2:]
digit_sum = sum(int(digit) for digit in str(prime_product))

print(f"Result: {prime_product}")