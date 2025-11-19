def compute_checksum(packets):
    n = len(packets)
    dp = [0] * (n + 1)
    xor_prefix = 0
    
    for i in range(1, n + 1):
        xor_prefix ^= packets[i-1]
        dp[i] = dp[i-1] ^ xor_prefix
    
    return dp[n]

def process_packets_with_verification(packet_sequences):
    verification_score = 0
    for seq in packet_sequences:
        checksum = compute_checksum(seq)
        verification_score ^= checksum
    return verification_score

# Packet sequences represented as lists of byte values
network_traffic = [
    [0b11001010, 0b10110101, 0b11100010],
    [0b10101010, 0b01010101],
    [0b11110000, 0b00001111, 0b10101010, 0b01010101]
]

verification_score = process_packets_with_verification(network_traffic)
print(f"Result: {verification_score}")