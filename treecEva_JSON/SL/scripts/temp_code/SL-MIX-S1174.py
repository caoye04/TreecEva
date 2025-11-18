from math import gcd
from functools import reduce

# Pie type identifiers (prime numbers)
pie_identifiers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

tuesday_sales = [1, 0, 2, 1, 0, 1, 0, 1, 0, 0]  # Number of each pie type sold

# Create list of identifiers for pies actually sold
sold_pies = [pie_identifiers[i] for i, count in enumerate(tuesday_sales) if count > 0]

# Calculate the product of all sold pie identifiers
sales_hash = reduce(lambda x, y: x * y, sold_pies, 1)

# Calculate GCD checksum of all identifiers
checksum = reduce(gcd, pie_identifiers)

# Final security hash combines the sales hash and checksum
final_security_hash = sales_hash + checksum

print(f"Result: {final_security_hash}")