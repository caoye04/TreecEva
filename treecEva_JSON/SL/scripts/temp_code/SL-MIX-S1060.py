def packet_checksum(n):
    if n == 0:
        return 7
    elif n == 1:
        return 11
    else:
        return (packet_checksum(n-1) ^ packet_checksum(n-2) + n) % 256

def calculate_transmission_sum(k):
    return sum(packet_checksum(i) for i in range(k+1))

def transform_signal(s):
    return ((s << 2) & 255) | (s >> 6)

# Main computation
transmission_limit = 12
signal_sum = calculate_transmission_sum(transmission_limit)
verification_code = transform_signal(signal_sum)
print(f"Result: {verification_code}")