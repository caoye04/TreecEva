from collections import defaultdict

def compress_string(s):
    if not s:
        return ""
    
    compressed = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
    compressed.append(f"{current_char}{count}")
    
    return ''.join(compressed)

input_text = 'aaabbcdddd'
encoded_result = compress_string(input_text)
compressed_length = len(encoded_result)
print(f"Result: {compressed_length}")