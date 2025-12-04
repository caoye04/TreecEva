import itertools

# Sock drawer inventory tracking
# Each number represents a sock with a specific pattern
sock_drawer = [1, 2, 1, 3, 2, 4, 3, 5, 5, 4, 1]

# Count how many complete pairs we have in the drawer
# A pair consists of two socks with the same pattern (same number)
available_patterns = len(set(sock_drawer))
remaining_socks = len(sock_drawer)

# Additional info for reference
unpaired_count = remaining_socks % 2

# Calculate the total number of complete pairs
total_pairs = sum(len(list(group)) // 2 for _, group in itertools.groupby(sorted(sock_drawer)))

# Track the patterns we have at least one of
patterns_present = [pattern for pattern in set(sock_drawer)]

print(f"Result: {total_pairs}")