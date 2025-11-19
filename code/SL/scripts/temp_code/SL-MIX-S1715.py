from functools import reduce
from collections import namedtuple

def tokenize_amount(amount_str):
    return [int(c) for c in amount_str if c.isdigit()]

Transaction = namedtuple('Transaction', ['amount', 'fee'])
transactions = [
    Transaction('123.45', '2.5'),
    Transaction('67.89', '1.2'),
    Transaction('456.78', '3.0')
]

processed_values = []
for txn in transactions:
    digits = tokenize_amount(txn.amount)
    fee_digits = tokenize_amount(txn.fee)
    combined = digits + fee_digits
    xor_result = reduce(lambda x, y: x ^ y, combined, 0)
    processed_values.append(xor_result)

checksum = reduce(lambda acc, val: (acc + val) & 0xFF, processed_values, 0)
print(f'Result: {checksum}')