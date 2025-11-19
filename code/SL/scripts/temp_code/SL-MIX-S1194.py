def calculate_suspicious_sources():
    # Monitored subnets represented as (base_ip, mask_length)
    monitored_subnets = {
        ('192.168.1.0', 24),
        ('10.0.0.0', 16),
        ('172.16.0.0', 12)
    }
    
    # Incoming packet source IPs (as integers for bitwise operations)
    packet_sources = [
        3232235777,  # 192.168.1.1
        3232235800,  # 192.168.1.24
        167772161,   # 10.0.0.1
        167772417,   # 10.0.1.1
        2886729729,  # 172.16.0.1
        2886795265,  # 172.17.0.1
        3232236033,  # 192.168.2.1 (not in 192.168.1.0/24)
        167772161,   # Duplicate 10.0.0.1
        2886729730,  # 172.16.0.2
    ]
    
    def ip_to_int(ip_str):
        parts = ip_str.split('.')
        return (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])
    
    def create_subnet_mask(mask_length):
        return (0xFFFFFFFF << (32 - mask_length)) & 0xFFFFFFFF
    
    # Convert monitored subnets to integer representations with masks
    subnet_masks = {}
    for base_ip_str, mask_len in monitored_subnets:
        base_ip_int = ip_to_int(base_ip_str)
        mask = create_subnet_mask(mask_len)
        subnet_masks[(base_ip_int, mask)] = mask_len
    
    # Find matching sources using divide and conquer approach
    matching_sources = set()
    
    def check_subnet_match(source_ip):
        for (base_ip, mask), _ in subnet_masks.items():
            if (source_ip & mask) == base_ip:
                return True
        return False
    
    # Process packets using binary search concept on sorted subnets
    sorted_subnets = sorted(subnet_masks.keys())
    
    for source in packet_sources:
        # Ternary operator to decide whether to add to matching sources
        matching_sources.add(source) if check_subnet_match(source) else None
    
    # Count unique suspicious sources
    suspicious_source_count = len(matching_sources)
    
    return suspicious_source_count

# Main execution
suspicious_source_count = calculate_suspicious_sources()
print(f"Result: {suspicious_source_count}")