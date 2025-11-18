import itertools

def calculate_artifact_checksum(tags):
    checksum_accumulator = 0
    tag_set = frozenset(tags)
    
    # Generate all permutations of length 3
    for perm in itertools.permutations(tag_set, 3):
        if perm[0] > perm[1]:  # Short-circuit evaluation starts here
            continue
        
        # Dynamic programming table for subsequence max-values
        dp = [0] * len(perm)
        dp[0] = ord(perm[0])
        
        for i in range(1, len(perm)):
            dp[i] = max(dp[i-1], ord(perm[i]))
        
        # Combine values using bitwise operations
        combined = dp[-1]
        for i in range(len(perm)-1):
            combined ^= (dp[i] << 1)
        
        # Update accumulator only if combined value meets condition
        if combined & 0xF0:  # Check if high nibble is non-zero
            checksum_accumulator += combined
    
    return checksum_accumulator

# Artifact tags for a specific collection
artifact_tags = ['A', 'B', 'C']
checksum_accumulator = calculate_artifact_checksum(artifact_tags)
print(f"Result: {checksum_accumulator}")