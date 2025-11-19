from dataclasses import dataclass
from typing import Optional
import itertools

class PolynomialNode:
    def __init__(self, coefficient: int, exponent: int):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next: Optional[PolynomialNode] = None

def insert_term(head: Optional[PolynomialNode], coefficient: int, exponent: int) -> PolynomialNode:
    new_node = PolynomialNode(coefficient, exponent)
    if not head or head.exponent < exponent:
        new_node.next = head
        return new_node
    current = head
    while current.next and current.next.exponent > exponent:
        current = current.next
    if current.exponent == exponent:
        current.coefficient += coefficient
    else:
        new_node.next = current.next
        current.next = new_node
    return head

def evaluate_polynomial(head: PolynomialNode, x: int) -> int:
    result = 0
    current = head
    exponents = []
    temp = head
    while temp:
        exponents.append(temp.exponent)
        temp = temp.next
    exponents.sort(reverse=True)
    
    for exp in exponents:
        # Binary search for the term with exponent exp
        low, high = 0, len(exponents) - 1
        found = False
        while low <= high:
            mid = (low + high) // 2
            if exponents[mid] == exp:
                found = True
                break
            elif exponents[mid] > exp:
                low = mid + 1
            else:
                high = mid - 1
        if found:
            # Find the actual node
            node = head
            while node and node.exponent != exp:
                node = node.next
            if node:
                result += node.coefficient * (x ** exp)
    return result

tokens = [2, 3, -1, 1, 5, 0, 3, 2]  # coefficient, exponent pairs
head: Optional[PolynomialNode] = None

# Parse tokens into polynomial
for i in range(0, len(tokens), 2):
    coeff, exp = tokens[i], tokens[i+1]
    head = insert_term(head, coeff, exp)

# Evaluate polynomial at x=3
x_value = 3
evaluated_result = evaluate_polynomial(head, x_value)
print(f"Result: {evaluated_result}")