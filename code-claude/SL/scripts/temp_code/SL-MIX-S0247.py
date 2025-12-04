from collections import Counter
import itertools

def digit_sum(n):
    """Calculate sum of digits in a number"""
    return sum(int(digit) for digit in str(n))

# Generate Fibonacci sequence up to 50 terms
fib_sequence = [0, 1]
for i in range(2, 50):
    fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

# Calculate digit sums for each Fibonacci number
digit_sums = [digit_sum(num) for num in fib_sequence]

# Some additional values to explore
sequence_length = len(fib_sequence)
average_digit_sum = sum(digit_sums) / sequence_length

# Find the most common digit sum
digit_counts = Counter(digit_sums)
most_common_digit_sum = digit_counts.most_common(1)[0][0]

# Calculate a secondary metric
second_metric = sum(1 for ds in digit_sums if ds % 3 == 0)

print(f"Result: {most_common_digit_sum}")