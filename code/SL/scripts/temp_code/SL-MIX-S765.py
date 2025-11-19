from dataclasses import dataclass
from typing import Optional
import math

def compute_checksum(values, start, end):
    if start == end:
        return values[start] if start < len(values) else 0
    if start > end:
        return 0
    mid = (start + end) // 2
    left_sum = compute_checksum(values, start, mid)
    right_sum = compute_checksum(values, mid + 1, end)
    return left_sum ^ right_sum

def validate_transaction_chain(head: 'TransactionNode') -> int:
    transactions = []
    current = head
    while current:
        transactions.append(current.amount)
        current = current.next
    
    if not transactions:
        return 0
        
    checksum = compute_checksum(transactions, 0, len(transactions) - 1)
    
    # Apply additional validation logic
    threshold = 1000
    adjustment = 0
    
    for i, amt in enumerate(transactions):
        if amt > threshold:
            adjustment += (amt >> 2) & 0xFF  # Right shift by 2 and mask with 0xFF
        else:
            adjustment -= amt & 0x0F  # Mask with 0x0F
    
    # Final validation score combines checksum and adjustments
    final_validation_score = (checksum & 0xFFFF) | ((adjustment << 16) & 0xFFFF0000)
    return final_validation_score

@dataclass
class TransactionNode:
    amount: int
    timestamp: int
    next: Optional['TransactionNode'] = None

# Build transaction chain
node1 = TransactionNode(1200, 10001, None)
node2 = TransactionNode(800, 10002, None)
node3 = TransactionNode(1500, 10003, None)
node4 = TransactionNode(600, 10004, None)

node1.next = node2
node2.next = node3
node3.next = node4

final_validation_score = validate_transaction_chain(node1)
print(f"Result: {final_validation_score}")