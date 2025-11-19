class AuthNode:
    def __init__(self, ip, success):
        self.ip = ip
        self.success = success
        self.next = None

def create_auth_chain(entries):
    if not entries:
        return None
    head = AuthNode(entries[0][0], entries[0][1])
    current = head
    for i in range(1, len(entries)):
        current.next = AuthNode(entries[i][0], entries[i][1])
        current = current.next
    return head

def count_subnet_stats(head):
    from collections import defaultdict
    stats = defaultdict(lambda: {'success': 0, 'fail': 0})
    
    current = head
    while current:
        parts = current.ip.split('.')
        subnet = '.'.join(parts[:2])
        if current.success:
            stats[subnet]['success'] += 1
        else:
            stats[subnet]['fail'] += 1
        current = current.next
    
    return stats

def calculate_suspicious_subnets(stats):
    count = 0
    for subnet, data in stats.items():
        if data['fail'] - data['success'] > 2:
            count += 1
    return count

# Log entries: (IP, success)
log_entries = [
    ('192.168.1.10', True),
    ('192.168.1.11', False),
    ('10.0.0.5', True),
    ('192.168.1.12', False),
    ('172.16.0.1', True),
    ('192.168.1.13', False),
    ('10.0.0.6', False),
    ('192.168.1.14', False),
    ('172.16.0.2', True),
    ('10.0.0.7', False),
    ('192.168.2.1', True),
    ('192.168.2.2', False),
    ('10.0.1.1', True),
    ('10.0.1.2', False),
    ('172.16.1.1', False),
    ('172.16.1.2', False),
    ('172.16.1.3', False),
    ('172.16.1.4', False)
]

auth_chain = create_auth_chain(log_entries)
subnet_stats = count_subnet_stats(auth_chain)
suspicious_subnets_count = calculate_suspicious_subnets(subnet_stats)
print(f"Result: {suspicious_subnets_count}")