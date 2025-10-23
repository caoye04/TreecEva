import base64
import itertools

default_permissions = 'gA=='  # Base64 for binary 10000000
team_override_masks = ['AQ==', 'Ag==', 'BQ==']  # Base64 for 00000001, 00000010, 00000101

# Decode default permissions
default_mask = int.from_bytes(base64.b64decode(default_permissions), 'big')

# Decode and combine override masks using XOR chaining
combined_override = 0
for enc_mask in team_override_masks:
    decoded_mask = int.from_bytes(base64.b64decode(enc_mask), 'big')
    combined_override ^= decoded_mask

# Apply overrides to default permissions
final_permission_mask = default_mask | combined_override

# Convert to dictionary with bit position analysis
permission_dict = {i: bool(final_permission_mask & (1 << i)) for i in range(8)}

# Count active permissions using itertools
active_permissions = sum(itertools.chain(permission_dict.values()))

# Final calculation combines mask value with active count
security_index = final_permission_mask + active_permissions

print(f'Result: {security_index}')