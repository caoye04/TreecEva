import math

class AuthNode:
    def __init__(self, session_id, timestamp):
        self.session_hash = hash(session_id)
        self.timestamp = timestamp
        self.next = None

def create_auth_chain():
    # Create a chain of authentication events
    head = AuthNode("admin_session_001", 1000)
    head.next = AuthNode("user_session_202", 1030)
    head.next.next = AuthNode("admin_session_001", 1060)  # Duplicate session
    head.next.next.next = AuthNode("guest_session_999", 1090)
    return head

# Process authentication chain
current = create_auth_chain()
session_hashes = set()
timestamp_weights = []

while current:
    session_hashes.add(current.session_hash)
    # Apply exponential decay to timestamp weight
    weight = math.exp(current.timestamp / 10000)
    timestamp_weights.append(weight)
    current = current.next

# Calculate unique session factor
unique_sessions = len(session_hashes)
log_factor = math.log(unique_sessions + 1, 2)

# Apply set operations with frozen set for security context
security_context = frozenset([1, 2, 4, 8, 16])
weight_flags = frozenset([int(w) for w in timestamp_weights])
intersection_cardinality = len(security_context & weight_flags)

# Compute final security index
exponent_base = intersection_cardinality + 2
final_security_index = int(math.pow(exponent_base, log_factor))

print(f"Result: {final_security_index}")