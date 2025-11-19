document_signatures = [
    "The quick brown fox jumps over the lazy dog",
    "A journey of a thousand miles begins with a single step",
    "To be or not to be, that is the question",
    "In the beginning God created the heavens and the earth",
    "The only thing we have to fear is fear itself"
]

processed_hashes = set()
collision_count = 0

for idx, text in enumerate(document_signatures):
    words = text.lower().split()
    signature = frozenset(words)
    sig_hash = hash(signature)
    
    if sig_hash in processed_hashes:
        collision_count += 1
        if collision_count > 1:
            break
    else:
        processed_hashes.add(sig_hash)
    
    # Early return simulation for efficiency
    if len(processed_hashes) >= 3:
        remaining_unique = sum(1 for i in range(idx+1, len(document_signatures))
                              if hash(frozenset(document_signatures[i].lower().split())) not in processed_hashes)
        if remaining_unique == 0:
            break

print(f"Result: {collision_count}")