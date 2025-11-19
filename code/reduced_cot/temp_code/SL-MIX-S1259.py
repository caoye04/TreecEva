import heapq

def pack_items_greedy(container_volumes, item_sizes):
    # Max heap implementation using negative values
    max_heap = [-vol for vol in container_volumes]
    heapq.heapify(max_heap)
    
    # Sort items in descending order for greedy packing
    item_sizes.sort(reverse=True)
    
    containers_used = 0
    remaining_spaces = []
    
    for item in item_sizes:
        # Try to fit item in existing containers
        if max_heap and -max_heap[0] >= item:
            # Use the container with maximum available space
            space = -heapq.heappop(max_heap)
            space -= item
            if space > 0:
                heapq.heappush(max_heap, -space)
        else:
            # Need a new container
            containers_used += 1
            new_container_space = 100 - item  # Assuming standard container size of 100
            if new_container_space > 0:
                heapq.heappush(max_heap, -new_container_space)
    
    return containers_used

# Container volumes available initially
initial_containers = [30, 50, 70]
# Item sizes to be packed
items_to_pack = [20, 40, 60, 10, 25, 35]

containers_used = pack_items_greedy(initial_containers, items_to_pack)
print(f"Result: {containers_used}")