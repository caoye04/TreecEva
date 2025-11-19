class TransactionNode:
    def __init__(self, hash_val, next_node=None):
        self.hash_val = hash_val
        self.next = next_node

def build_transaction_chain(transaction_hashes):
    if not transaction_hashes:
        return None
    head = TransactionNode(transaction_hashes[0])
    current = head
    for h in transaction_hashes[1:]:
        current.next = TransactionNode(h)
        current = current.next
    return head

def compute_verification_score(chain_head):
    xor_accumulator = 0
    node_count = 0
    current = chain_head
    while current:
        xor_accumulator ^= current.hash_val
        node_count += 1
        current = current.next
    
    # Correction factor: if odd number of nodes, multiply by 3; else subtract 5
    if node_count % 2 == 1:
        correction_factor = 3
    else:
        correction_factor = -5
        
    return xor_accumulator + correction_factor

def main():
    # Transaction hashes represented as integers for simplicity
    raw_transactions = ["tx_001", "tx_002", "tx_003", "tx_004"]
    transaction_hashes = [hash(t) & 0xFFFF for t in raw_transactions]  # Limit hash size
    
    # Build linked list chain
    chain_head = build_transaction_chain(transaction_hashes)
    
    # Compute verification score
    final_verification_score = compute_verification_score(chain_head)
    
    print(f"Result: {final_verification_score}")

if __name__ == "__main__":
    main()