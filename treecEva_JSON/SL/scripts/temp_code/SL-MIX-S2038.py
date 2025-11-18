import itertools

# Prime digits for cryptographic permutations
prime_digits = [2, 3, 5, 7]

# Generate all permutations of length 3 from prime digits
permutation_list = list(itertools.permutations(prime_digits, 3))

# Calculate the product of digits for each permutation and sum them
aggregate_product_sum = sum(a * b * c for a, b, c in permutation_list)

# Count permutations where all digits are identical (though with prime digits, this is always 0)
same_digit_count = sum(1 for a, b, c in permutation_list if a == b == c)

# Compute the security index
security_index = aggregate_product_sum - same_digit_count

print(f"Result: {security_index}")