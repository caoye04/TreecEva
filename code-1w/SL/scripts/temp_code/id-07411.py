def process_shipment(data, log):
    base_count = sum(data['items']['inbound'])
    outbound_total = sum(data['items']['outbound'])
    
    # Irrelevant string processing (distractor)
    tracking_code = data['tracking'].upper().replace('-', '')
    prefix = tracking_code[:3]
    suffix = tracking_code[-3:]
    validation_checksum = len(tracking_code) + ord(prefix[0])

    # Semi-relevant slicing operation on history (some values unused)
    recent_history = log['adjustments'][-5:]
    adjustment_sum = sum([a['value'] for a in recent_history if a['type'] == 'correction'])
    
    # Dummy loop with dead computation
    temp_buffer = []
    for i in range(3):
        temp_buffer.append(1 / (i + 1))  # No impact on result

    # Core logic: inventory balance calculation
    raw_balance = base_count - outbound_total + adjustment_sum
    
    # Additional state tracking (only one field matters)
    status_flags = {
        'cleared': True,
        'audited': False,
        'finalized': len(recent_history) > 0
    }
    
    # Final adjustment based on valid conditions
    inventory_balance = raw_balance
    if status_flags['cleared'] and data['warehouse'] == 'WHR-7B':
        inventory_balance -= 2  # Correction for handling error

    return inventory_balance

# Input data setup
delivery_log = {
    'adjustments': [
        {'type': 'addition', 'value': 5},
        {'type': 'correction', 'value': 3},
        {'type': 'correction', 'value': -1},
        {'type': 'removal', 'value': 8},
        {'type': 'correction', 'value': 4}
    ]
}

shipment_data = {
    'tracking': 'TRK-789-XZ',
    'warehouse': 'WHR-7B',
    'items': {
        'inbound': [10, 15, 7, 12],
        'outbound': [8, 11, 6]
    }
}

# Execute main logic
inventory_balance = process_shipment(shipment_data, delivery_log)
print(f"Result: {inventory_balance}")