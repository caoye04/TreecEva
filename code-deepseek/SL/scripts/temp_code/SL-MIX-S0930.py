warehouse_inventory = "clean:15,dirty:8,clean:22,dirty:3,clean:9"
items_list = warehouse_inventory.split(',')
count_clean = 0
count_dirty = 0

for item in items_list:
    if item.startswith('clean:'):
        quantity = int(item.split(':')[1])
        count_clean += quantity
    elif item.startswith('dirty:'):
        quantity = int(item.split(':')[1])
        count_dirty += quantity

final_count = count_clean + count_dirty
print(f"Result: {final_count}")