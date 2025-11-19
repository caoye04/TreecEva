import hashlib
from itertools import permutations
from functools import reduce

def compute_hash_chain(paper_id, depth):
    if depth == 0:
        return hashlib.md5(paper_id.encode()).hexdigest()
    else:
        prev_hash = compute_hash_chain(paper_id, depth - 1)
        return hashlib.md5(prev_hash.encode()).hexdigest()

def validate_submission(title, authors, year):
    # Generate author permutations
    author_perms = list(permutations(authors))
    perm_hashes = []
    
    for perm in author_perms[:3]:  # Only first 3 permutations
        combined = ''.join(perm) + str(year)
        perm_hashes.append(hashlib.sha256(combined.encode()).hexdigest())
    
    # Compute hash chain for title
    title_hash = compute_hash_chain(title, 2)
    
    # Combine using XOR operation
    combined_result = reduce(lambda x, y: hex(int(x, 16) ^ int(y, 16)), perm_hashes, '0x0')
    
    # Final verification score
    score = (int(combined_result, 16) % 1000) + len(title_hash) 
    
    return score

# Research paper details
paper_title = "AdvancedQuantumAlgorithms"
paper_authors = ["DrSmith", "ProfJohnson", "DrWilliams"]
paper_year = 2023

# Validate the submission
verification_score = validate_submission(paper_title, paper_authors, paper_year)
print(f"Result: {verification_score}")