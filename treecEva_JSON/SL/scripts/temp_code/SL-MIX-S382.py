from collections import defaultdict

class SecurityContext:
    def __init__(self, segments):
        self.segments = segments
        self.filtered = []
    
    def __enter__(self):
        # Apply first filter: only segments with even number of octets
        self.filtered = [seg for seg in self.segments if len(seg.split('.')) % 2 == 0]
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

ip_segments = ['192.168.1.0', '10.0.0.0', '172.16.0.0', '192.168.0.0', '10.10.10.10']
suspicious_count = 0

with SecurityContext(ip_segments) as ctx:
    # Apply second filter: segments where first octet is > 100 AND (third octet exists OR second octet is odd)
    secondary_filtered = []
    for segment in ctx.filtered:
        octets = segment.split('.')
        first_octet = int(octets[0])
        if first_octet > 100 and (len(octets) >= 3 or (len(octets) >= 2 and int(octets[1]) % 2 == 1)):
            secondary_filtered.append(segment)
    
    # Apply final counting logic with short-circuit evaluation
    octet_sum_map = defaultdict(int)
    for segment in secondary_filtered:
        octets = [int(o) for o in segment.split('.')]
        octet_sum = sum(octets)
        # Only count if sum is > 200 AND (at least 3 octets OR first octet > 150)
        if octet_sum > 200 and (len(octets) >= 3 or octets[0] > 150):
            octet_sum_map[octet_sum] += 1
    
    # Final suspicious count is the number of unique sums that appear exactly twice
    suspicious_count = sum(1 for count in octet_sum_map.values() if count == 2)

print(f"Result: {suspicious_count}")