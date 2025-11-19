from functools import reduce

def compute_movement_hash(op_type, item_id, quantity):
    base_str = f"{op_type}:{item_id}:{quantity}"
    return hash(base_str) % 10000

def update_warehouse_checksum(current_checksum, op_details):
    op_type, item_id, quantity = op_details
    if quantity <= 0:
        return current_checksum
    movement_hash = compute_movement_hash(op_type, item_id, quantity)
    if op_type == "OUT":
        return current_checksum - movement_hash
    elif op_type == "IN":
        return current_checksum + movement_hash
    else:
        return current_checksum

operations_log = [
    ("IN", "WIDGET_A", 150),
    ("OUT", "GADGET_B", 75),
    ("IN", "SPROCKET_C", 200),
    ("OUT", "WIDGET_A", 50),
    ("IN", "GIZMO_D", 0),  # Invalid quantity, should be skipped
    ("TRANSFER", "GADGET_B", 25),  # Unknown operation type, should be ignored
    ("IN", "WIDGET_A", 100)
]

# Initialize warehouse state
inventory_levels = {
    "WIDGET_A": 1000,
    "GADGET_B": 500,
    "SPROCKET_C": 250
}

active_items = {k: v for k, v in inventory_levels.items() if v > 0}
checksum_registry = {item: hash(item) % 1000 for item in active_items}
initial_checksum = sum(checksum_registry.values())

final_checksum = reduce(update_warehouse_checksum, operations_log, initial_checksum)
print(f"Result: {final_checksum}")