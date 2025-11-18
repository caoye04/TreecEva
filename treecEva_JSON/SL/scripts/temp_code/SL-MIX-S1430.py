from collections import Counter

def process_restock(inventory, restock_events):
    for snack, priority, quantity in restock_events:
        if priority >= 3:
            inventory[snack] += quantity
    return inventory

# Initial inventory state
vending_inventory = Counter({'chips': 10, 'cookies': 5, 'nuts': 5})

# Restock events: (snack_name, priority_level, quantity)
restock_schedule = [
    ('chips', 4, 15),
    ('cookies', 2, 20),
    ('nuts', 3, 10),
    ('crackers', 1, 25),
    ('pretzels', 3, 12)
]

# Process all restock events
updated_inventory = process_restock(vending_inventory, restock_schedule)

# Calculate total high-priority snacks (priority >= 3)
high_priority_total = sum(count for snack, count in updated_inventory.items() 
                        if any(priority >= 3 for event_snack, priority, _ in restock_schedule if event_snack == snack))

# Add initial high-priority snacks that weren't restocked
high_priority_total += sum(count for snack, count in vending_inventory.items() 
                          if snack not in [event[0] for event in restock_schedule] and 
                          any(priority >= 3 for event_snack, priority, _ in [('chips', 4, 0), ('nuts', 3, 0)] if event_snack == snack))

print(f"Result: {high_priority_total}")