class ListNode:
    def __init__(self, user_hash, timestamp):
        self.user_hash = user_hash
        self.timestamp = timestamp
        self.next = None

def hash_user_id(user_id):
    return hash(user_id) % 1000000

def is_valid_session(current_hash, prev_hash, time_diff):
    hash_check = (current_hash & prev_hash) != 0
    time_check = time_diff <= 3600
    return hash_check and time_check

def process_logs(log_entries):
    if not log_entries:
        return 0
    
    head = None
    tail = None
    valid_sessions_count = 0
    
    for entry in log_entries:
        user_id, timestamp = entry
        user_hash = hash_user_id(user_id)
        
        new_node = ListNode(user_hash, timestamp)
        
        if head is None:
            head = new_node
            tail = new_node
        else:
            time_diff = new_node.timestamp - tail.timestamp
            if is_valid_session(new_node.user_hash, tail.user_hash, time_diff):
                valid_sessions_count += 1
            tail.next = new_node
            tail = new_node
    
    return valid_sessions_count

log_data = [
    ('user_001', 1000),
    ('user_002', 2500),
    ('user_001', 4000),
    ('user_003', 6000),
    ('user_001', 7200),
    ('user_002', 9000)
]

valid_sessions_count = process_logs(log_data)
print(f"Result: {valid_sessions_count}")