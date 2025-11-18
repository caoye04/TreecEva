from dataclasses import dataclass
from typing import Optional
import math

def greedy_correction(value: int) -> int:
    denominations = [50, 20, 10, 5, 1]
    correction = 0
    for denom in denominations:
        while value >= denom:
            value -= denom
            correction += denom
        if value == 0:
            break
    return correction

def divide_conquer_sum(node: 'TransactionNode') -> int:
    if not node:
        return 0
    if not node.next:
        return node.amount
    slow = fast = node
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    left_sum = divide_conquer_sum(node)
    right_sum = divide_conquer_sum(slow)
    return left_sum + right_sum

@dataclass
class TransactionNode:
    amount: int
    next: Optional['TransactionNode'] = None

class AuditLedger:
    def __init__(self):
        self.head: Optional[TransactionNode] = None
    
    def append(self, amount: int):
        new_node = TransactionNode(amount)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def apply_corrections(self):
        current = self.head
        corrections_map = {}
        while current:
            if current.amount < 0:
                corrected = greedy_correction(abs(current.amount))
                corrections_map[current.amount] = corrected
            current = current.next
        return corrections_map

ledger = AuditLedger()
transactions = [100, -57, 25, -33, 12, -89, 45, -12, 67]
for t in transactions:
    ledger.append(t)

correction_map = ledger.apply_corrections()
total_discrepancy = divide_conquer_sum(ledger.head)
corrected_total = total_discrepancy
for original, corrected in correction_map.items():
    corrected_total += (corrected - abs(original))

if corrected_total % 2 == 0:
    audit_balance = corrected_total // 2
else:
    audit_balance = math.floor(corrected_total / 2) + 1

print(f"Result: {audit_balance}")