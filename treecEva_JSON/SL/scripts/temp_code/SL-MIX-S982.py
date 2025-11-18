import hashlib

class SessionNode:
    def __init__(self, session_id, parent=None):
        self.session_id = session_id
        self.parent = parent
        self.children = []
        if parent:
            parent.children.append(self)
    
    def add_child(self, child_id):
        child = SessionNode(child_id, self)
        return child

def compute_hash(data):
    return int(hashlib.md5(str(data).encode()).hexdigest()[:8], 16)

def validate_session(session_map, session_id, threshold=1000000):
    hash_val = session_map.get(session_id, 0)
    return hash_val > threshold and hash_val % 7 == 3

def calculate_base_score(node, session_map):
    if not node:
        return 0
    score = session_map.get(node.session_id, 0) % 100
    for child in node.children:
        score += calculate_base_score(child, session_map) * 0.5
    return int(score)

# Build session tree
root = SessionNode("sess_001")
child1 = root.add_child("sess_002")
child2 = root.add_child("sess_003")
grandchild1 = child1.add_child("sess_004")

# Populate hash table with session data
session_hashes = {
    "sess_001": compute_hash("admin_login"),
    "sess_002": compute_hash("user_query"),
    "sess_003": compute_hash("guest_access"),
    "sess_004": compute_hash("api_call")
}

# Process sessions with short-circuit evaluation
auth_weights = [2, 3, 1, 4]
session_list = ["sess_001", "sess_002", "sess_003", "sess_004"]
valid_sessions = [
    sid for i, sid in enumerate(session_list)
    if validate_session(session_hashes, sid) or auth_weights[i] > 2
]

# Calculate final authentication score
base_score = calculate_base_score(root, session_hashes)
bonus_points = sum(1 for s in valid_sessions if session_hashes[s] & 0xF == 3)
penalty = len([s for s in session_list if not validate_session(session_hashes, s)]) * 5

final_auth_score = (base_score + bonus_points * 10 - penalty) * (1 if len(valid_sessions) >= 3 else -1)
print(f"Result: {final_auth_score}")