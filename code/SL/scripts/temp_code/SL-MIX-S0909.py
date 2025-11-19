from collections import Counter

def fibonacci_sequence(n):
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

# Generate first 15 Fibonacci numbers
fib_numbers = fibonacci_sequence(15)

# Initialize counter for digits
occurrence_counter = Counter()

# Process each number as string to count individual digits
for num in fib_numbers:
    digit_str = str(num)
    occurrence_counter.update(digit_str)

# Get the count of digit '1'
target_count = occurrence_counter['1']

print(f"Result: {target_count}")