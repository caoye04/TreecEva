from contextlib import contextmanager

def validate_transaction_chain(transactions, index=0, accumulated_flags=0):
    if index >= len(transactions):
        return accumulated_flags
    
    current_tx = transactions[index]
    tx_valid = (current_tx['amount'] > 0) and (current_tx['timestamp'] is not None)
    
    if not tx_valid:
        return validate_transaction_chain(transactions, index + 1, accumulated_flags)
    
    checksum_match = (current_tx['checksum'] & 0xFF) == (current_tx['id'] & 0xFF)
    
    if checksum_match and current_tx['amount'] < 1000:
        new_flags = accumulated_flags | (1 << (index % 8))
        return validate_transaction_chain(transactions, index + 1, new_flags)
    elif checksum_match:
        return validate_transaction_chain(transactions, index + 1, accumulated_flags)
    else:
        return accumulated_flags

@contextmanager
def audit_trail_context(transactions):
    print(f"Starting audit of {len(transactions)} transactions")
    try:
        yield transactions
    finally:
        print("Audit completed")

transactions_ledger = [
    {'id': 1001, 'amount': 1500.0, 'timestamp': '2023-01-01', 'checksum': 0x1F2A},
    {'id': 1002, 'amount': 750.5, 'timestamp': '2023-01-02', 'checksum': 0x2B02},
    {'id': 1003, 'amount': -200.0, 'timestamp': '2023-01-03', 'checksum': 0x3C03},
    {'id': 1004, 'amount': 1200.0, 'timestamp': None, 'checksum': 0x4D04},
    {'id': 1005, 'amount': 300.0, 'timestamp': '2023-01-05', 'checksum': 0x5E05}
]

compliance_score = 0

with audit_trail_context(transactions_ledger) as ledger:
    compliance_score = validate_transaction_chain(ledger)
    
    # Apply final adjustment based on number of valid transactions
    valid_count = sum(1 for tx in ledger if tx['amount'] > 0 and tx['timestamp'] is not None)
    if valid_count >= 3 and (compliance_score & 0b1010) == 0b1010:
        compliance_score += 100
    elif valid_count < 3 or not (compliance_score & 0b0101):
        compliance_score -= 50

print(f"Result: {compliance_score}")