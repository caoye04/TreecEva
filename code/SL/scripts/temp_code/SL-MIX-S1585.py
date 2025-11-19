def encode_char(c, pos):
    return chr((ord(c) + pos) % 128)

password = "Secr3t"
encoded_chars = [encode_char(c, i) for i, c in enumerate(password)]
encoded_string = ''.join(encoded_chars)

verification_mask = [True, False, True, True, False, True]
char_checks = [ord(c) > 70 for c in encoded_string]

auth_score = sum(1 << i for i, (mask, check) in enumerate(zip(verification_mask, char_checks)) if mask and check)
print(f"Result: {auth_score}")