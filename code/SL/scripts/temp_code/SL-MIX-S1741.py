import itertools

def compute_cipher_strength():
    base_chars = frozenset('abc')
    extension_chars = {'d', 'e'}
    full_charset = base_chars | extension_chars
    
    # Count all possible permutations of length 3 from the full charset
    perm_count = len(list(itertools.permutations(full_charset, 3)))
    
    # Create a mapping of each character to its ASCII value modulo 5
    char_mod_map = {char: ord(char) % 5 for char in full_charset}
    
    # Calculate the product of all unique mod values
    mod_product = 1
    for mod_val in set(char_mod_map.values()):
        mod_product *= mod_val
    
    # Cipher strength is the permutation count minus the mod product
    cipher_strength = perm_count - mod_product
    
    return cipher_strength

result = compute_cipher_strength()
print(f"Result: {result}")