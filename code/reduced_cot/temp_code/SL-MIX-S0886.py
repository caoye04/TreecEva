from functools import reduce
from collections import defaultdict

def merge_sort_with_metadata(arr, metadata_map):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_with_metadata(arr[:mid], metadata_map)
    right = merge_sort_with_metadata(arr[mid:], metadata_map)
    return merge_with_tracking(left, right, metadata_map)

def merge_with_tracking(left, right, metadata_map):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if metadata_map[left[i]]['priority'] <= metadata_map[right[j]]['priority']:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

class DeliveryContext:
    def __init__(self):
        self.package_registry = defaultdict(dict)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def register_package(self, pkg_id, deadline, weight):
        priority_score = (deadline << 2) ^ (weight & 0xF)
        self.package_registry[pkg_id] = {
            'deadline': deadline,
            'weight': weight,
            'priority': priority_score
        }
        return priority_score

# Main processing logic
with DeliveryContext() as warehouse:
    shipment_batch = ['PKG001', 'PKG002', 'PKG003', 'PKG004', 'PKG005', 'PKG006']
    deadlines = [24, 12, 36, 6, 18, 48]
    weights = [15, 8, 22, 5, 12, 30]
    
    # Register all packages and calculate priorities
    for idx, pkg in enumerate(shipment_batch):
        warehouse.register_package(pkg, deadlines[idx], weights[idx])
    
    # Sort packages by priority
    sorted_packages = merge_sort_with_metadata(shipment_batch, warehouse.package_registry)
    
    # Count critical deliveries (priority > 100)
    critical_delivery_count = reduce(
        lambda count, pkg: count + (1 if warehouse.package_registry[pkg]['priority'] > 100 else 0),
        sorted_packages, 0
    )

print(f"Result: {critical_delivery_count}")