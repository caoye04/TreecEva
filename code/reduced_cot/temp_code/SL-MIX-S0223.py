import hashlib
import heapq

def hash_subsequence(subseq):
    return int(hashlib.md5(subseq.encode()).hexdigest()[:8], 16) % 1000000

def is_palindrome(s):
    return s == s[::-1]

dna_strand = "ATGCCGTAATGCCGTAATGCCGTAATGCCGTA"
palindromic_hashes = set()

for i in range(len(dna_strand) - 3):
    subseq = dna_strand[i:i+4]
    if is_palindrome(subseq):
        palindromic_hashes.add(hash_subsequence(subseq))

# Convert to sorted list for deterministic heap operations
sorted_hashes = sorted(list(palindromic_hashes))

# Create a max heap using negative values
hash_heap = [-x for x in sorted_hashes]
heapq.heapify(hash_heap)

# Process heap elements
signature_components = []
while len(hash_heap) > 1:
    first = -heapq.heappop(hash_heap)
    second = -heapq.heappop(hash_heap)
    combined = (first ^ second) & 0xFFFF  # XOR and mask to 16 bits
    heapq.heappush(hash_heap, -combined)
    signature_components.append(combined)

final_signature = sum(signature_components) % 10000
print(f"Result: {final_signature}")