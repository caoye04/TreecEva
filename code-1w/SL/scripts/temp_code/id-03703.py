def calculate_score(entries):
    total = 0
    for item in entries:
        if item['status'] == 'active':
            total += item['weight']
    return total

# System configuration data
cfg_mode = 'production'
debug_flags = [False, True, False]

# Main data input
data = [
    {'id': 1, 'weight': 3, 'status': 'inactive'},
    {'id': 2, 'weight': 7, 'status': 'active'},
    {'id': 3, 'weight': 5, 'status': 'active'},
    {'id': 4, 'weight': 2, 'status': 'inactive'},
    {'id': 5, 'weight': 9, 'status': 'active'}
]

# Irrelevant helper (minimal distraction)
def validate_entry(e):
    return e['id'] > 0

# Key slicing operation
data_slice = data[1:4]  # Middle three entries

# Core computation
result = calculate_score(data_slice)

print(f"Result: {result}")