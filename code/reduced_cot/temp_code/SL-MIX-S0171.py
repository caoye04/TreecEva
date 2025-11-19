from collections import namedtuple
import hashlib

def encode_token(s):
    return ''.join(chr(ord(c) + 1) for c in s)

def decode_token(s):
    return ''.join(chr(ord(c) - 1) for c in s)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Initialize linked list with encoded tokens
head = Node(encode_token("alpha"))
head.next = Node(encode_token("beta"))
head.next.next = Node(encode_token("gamma"))

# Token validation sets
valid_prefixes = frozenset(['b', 'g'])
blacklisted_suffixes = {'eta', 'lta'}

# Matrix transformation
matrix = [
    [2, 3],
    [1, 4]
]
vector = [5, 7]

# Process linked list
checksum_components = []
current = head
while current:
    decoded = decode_token(current.data)
    prefix_valid = decoded[0] in valid_prefixes
    suffix_blacklisted = decoded[-3:] in blacklisted_suffixes
    hash_valid = hashlib.md5(decoded.encode()).hexdigest()[-1] in '0123456'
    
    if prefix_valid and not suffix_blacklisted and hash_valid:
        # Apply matrix transformation
        transformed = [matrix[0][0]*vector[0] + matrix[0][1]*vector[1], 
                      matrix[1][0]*vector[0] + matrix[1][1]*vector[1]]
        checksum_components.append(sum(transformed))
    current = current.next

# Calculate final checksum
final_checksum = sum(checksum_components) if checksum_components else -1
print(f"Result: {final_checksum}")