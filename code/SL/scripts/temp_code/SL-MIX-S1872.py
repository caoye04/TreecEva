from math import gcd
from itertools import permutations

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def transform_list(head):
    current = head
    index = 1
    while current:
        current.val = gcd(current.val, index)
        current = current.next
        index += 1
    return head

def linked_list_to_array(head):
    arr = []
    current = head
    while current:
        arr.append(current.val % 7)
        current = current.next
    return arr

def create_square_matrix(arr):
    n = len(arr)
    size = int(n ** 0.5)
    if size * size != n:
        size += 1
    matrix = [[0] * size for _ in range(size)]
    for i in range(n):
        matrix[i // size][i % size] = arr[i]
    return matrix

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(n):
        submatrix = [[matrix[r][j] for j in range(n) if j != c] for r in range(1, n)]
        sign = (-1) ** c
        det += sign * matrix[0][c] * determinant(submatrix)
    return det

# Molecular atomic weights
atomic_weights = [24, 36, 54, 72, 18, 90, 108, 126, 144]
head = create_linked_list(atomic_weights)
transformed_head = transform_list(head)
mod_array = linked_list_to_array(transformed_head)
square_matrix = create_square_matrix(mod_array)
final_determinant = determinant(square_matrix)
print(f"Result: {final_determinant}")