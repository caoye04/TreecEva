class CacheSystem:
    def __init__(self, max_size=10):
        self.cache = {}
        self.access_order = []
        self.max_size = max_size
        self.hit_count = 0
        self.miss_count = 0
    
    def get(self, key):
        if key in self.cache:
            self.access_order.remove(key)
            self.access_order.append(key)
            self.hit_count += 1
            return self.cache[key]
        else:
            self.miss_count += 1
            return None
    
    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.access_order.remove(key)
            self.access_order.append(key)
        else:
            if len(self.cache) >= self.max_size:
                oldest = self.access_order.pop(0)
                del self.cache[oldest]
            self.cache[key] = value
            self.access_order.append(key)

def complex_graph_processing(nodes, edges):
    cache = CacheSystem(3)
    visited = set()
    path_costs = {}
    processing_queue = []
    
    # Initialize path costs
    for node in nodes:
        path_costs[node] = float('inf')
    path_costs[0] = 0
    
    # Build adjacency list with caching
    adj_list = {}
    for node in nodes:
        cached_neighbors = cache.get(f"neighbors_{node}")
        if cached_neighbors is None:
            neighbors = []
            for src, dst, weight in edges:
                if src == node:
                    neighbors.append((dst, weight))
            cache.put(f"neighbors_{node}", neighbors)
            adj_list[node] = neighbors
        else:
            adj_list[node] = cached_neighbors
    
    # Modified Dijkstra with caching and complex state management
    processing_queue.append((0, 0))  # (cost, node)
    iteration_count = 0
    
    while processing_queue and iteration_count < 20:
        processing_queue.sort(key=lambda x: x[0])
        current_cost, current_node = processing_queue.pop(0)
        iteration_count += 1
        
        if current_node in visited:
            cached_skip = cache.get(f"skip_{current_node}")
            if cached_skip is None:
                cache.put(f"skip_{current_node}", True)
            continue
        
        visited.add(current_node)
        
        # Cache current path cost
        cached_cost = cache.get(f"cost_{current_node}")
        if cached_cost is None:
            cache.put(f"cost_{current_node}", current_cost)
        
        # Process neighbors with complex caching logic
        for neighbor, weight in adj_list[current_node]:
            if neighbor not in visited:
                new_cost = current_cost + weight
                
                # Check cached optimization
                cache_key = f"opt_{current_node}_{neighbor}"
                cached_opt = cache.get(cache_key)
                
                if cached_opt is None:
                    optimization_factor = 1
                    if iteration_count % 2 == 0:
                        optimization_factor = 0.9
                    new_cost = int(new_cost * optimization_factor)
                    cache.put(cache_key, optimization_factor)
                else:
                    new_cost = int(new_cost * cached_opt)
                
                if new_cost < path_costs[neighbor]:
                    path_costs[neighbor] = new_cost
                    processing_queue.append((new_cost, neighbor))
                    
                    # Cache path update
                    update_key = f"update_{neighbor}_{iteration_count}"
                    cached_update = cache.get(update_key)
                    if cached_update is None:
                        cache.put(update_key, new_cost)
    
    return cache

# Test the function
nodes = [0, 1, 2, 3]
edges = [(0, 1, 2), (1, 2, 3), (2, 3, 1), (3, 0, 4)]
final_cache = complex_graph_processing(nodes, edges)
print(f"Final hit_count: {final_cache.hit_count}")