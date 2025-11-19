permissions_mask = 0b11010110
key = 0b10110011

# Step 1: XOR with key
step1 = permissions_mask ^ key

# Step 2: Left shift by 1
step2 = step1 << 1

# Step 3: Apply conditional update using ternary
step3 = step2 & 0xFF if step2 > 255 else step2 | 0xF0

# Step 4: Right shift by 2
step4 = step3 >> 2

# Define a lambda to check if number of set bits is even
even_bits = lambda x: bin(x).count('1') % 2 == 0

# Step 5: Create a dictionary of possible masks and their even_bits status
mask_options = {i: step4 ^ i for i in range(4)}
filtered_dict = {k: v for k, v in mask_options.items() if even_bits(v)}

# Step 6: Merge with another dictionary using dict comprehension
base_dict = {0: 0b1111, 1: 0b0000, 2: 0b1010, 3: 0b0101}
merged_dict = {k: filtered_dict.get(k, 0) | base_dict[k] for k in base_dict}

# Step 7: Final mask is the XOR of all values in merged_dict
final_permission_mask = 0
for val in merged_dict.values():
    final_permission_mask ^= val

print(f"Result: {final_permission_mask}")