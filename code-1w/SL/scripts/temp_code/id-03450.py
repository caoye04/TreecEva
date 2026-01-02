user_role = 'admin'
access_level = 7

timestamp = 1692547200
base_secret = 12345

# Generate session hash using bitwise and arithmetic operations
session_id = (timestamp + base_secret) & 0xFFFF

# Apply role-based modifier using conditional expression
role_modifier = 9 if user_role == 'admin' else 3

# Compute intermediate hash
intermediate_hash = (session_id * 2) ^ role_modifier

# Update access level with bit shift based on session parity
if intermediate_hash % 2 == 0:
    access_level = access_level << 1
else:
    access_level = access_level >> 1

# Final hash computation using set bits from intermediate values
bits_present = {bit for bit in range(8) if (intermediate_hash >> bit) & 1}
bit_sum = sum(bits_present)
final_hash = intermediate_hash + bit_sum

# Critical statement: compute final security key
security_key = final_hash ^ access_level

print(f"Result: {security_key}")