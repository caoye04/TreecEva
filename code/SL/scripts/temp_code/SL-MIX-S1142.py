from collections import defaultdict

def compute_routing_checksum():
    # Network nodes represented as indices 0-7
    nodes = 8
    
    # Initialize routing table with fibonacci sequence values
    fib_table = [0, 1]
    for i in range(2, nodes):
        fib_table.append(fib_table[i-1] + fib_table[i-2])
    
    # Routing decisions stored in defaultdict
    routing_decisions = defaultdict(int)
    
    # Dynamic programming table for path optimization
    dp = [[0 for _ in range(nodes)] for _ in range(nodes)]
    
    # Calculate optimal paths using DP
    for src in range(nodes):
        for dst in range(nodes):
            if src != dst:
                # Path cost is based on fibonacci values and bitwise operations
                base_cost = fib_table[src] ^ fib_table[dst]
                shifted_cost = base_cost << (src & dst)  # Bitwise AND then left shift
                dp[src][dst] = shifted_cost & 0xFF  # Keep within byte range
                
                # Record routing decision with XOR checksum
                routing_decisions[src] ^= dp[src][dst]
    
    # Calculate final checksum using another DP pass
    checksum_dp = [0] * nodes
    for i in range(1, nodes):
        # Combine previous checksum with current routing decisions
        checksum_dp[i] = (checksum_dp[i-1] ^ routing_decisions[i]) & 0xFFFF
    
    # Final step: Apply bit rotation and combine with fibonacci tail
    final_checksum = checksum_dp[nodes-1]
    rotation_bits = fib_table[nodes-1] % 16
    final_checksum = ((final_checksum << rotation_bits) | (final_checksum >> (16 - rotation_bits))) & 0xFFFF
    
    return final_checksum

final_checksum = compute_routing_checksum()
print(f"Result: {final_checksum}")