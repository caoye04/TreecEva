from functools import reduce

# Define the modified Fibonacci sequence generator using lambda
fib_lambda = lambda a, b: a + b

# Initialize the sequence
population_sequence = [1, 1]

# Generate the sequence up to the 10th term
for i in range(2, 10):
    next_term = fib_lambda(population_sequence[i-1], population_sequence[i-2])
    population_sequence.append(next_term)

# Get the population in the 10th year
tenth_year_population = population_sequence[9]

print(f'Result: {tenth_year_population}')