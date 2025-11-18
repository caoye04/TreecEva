import math
from collections import defaultdict

def compute_session_keys(entropy_pool):
    # Dynamic programming table for key derivation
    dp = defaultdict(int)
    dp[0] = entropy_pool[0]
    
    # Process entropy pool using divide and conquer approach
    for i in range(1, len(entropy_pool)):
        # Bitwise transformation with previous state
        xor_result = dp[i-1] ^ entropy_pool[i]
        # Exponential mapping for key expansion
        exp_result = int(math.pow(xor_result, 1.5))
        # Apply modulo to keep numbers manageable
        dp[i] = exp_result % 1000000
    
    # Verification token calculation using bitwise operations
    checksum = 0
    for i in range(len(dp)):
        # Rotate left by 3 positions and XOR with current dp value
        rotated = ((dp[i] << 3) | (dp[i] >> 29)) & 0xFFFFFFFF
        checksum ^= rotated
    
    return checksum

# Initial entropy values for key generation
initial_entropy = [1729, 2048, 4096, 8192, 16384]

# Compute session keys and derive final verification token
session_key_checksum = compute_session_keys(initial_entropy)

print(f"Result: {session_key_checksum}")