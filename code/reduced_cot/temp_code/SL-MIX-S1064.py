from collections import deque
import itertools

def calculate_load_factor(truck_id, package_weights):
    base_capacity = 1000
    loaded_weight = sum(package_weights)
    return loaded_weight / base_capacity if base_capacity > 0 else 0

class PackageProcessor:
    def __init__(self):
        self.standard_queue = deque()
        self.priority_stack = []
        self.truck_utilization = {}
    
    def add_package(self, pkg_id, weight, is_priority=False):
        if is_priority and weight > 0:
            self.priority_stack.append((pkg_id, weight))
        elif not is_priority and weight >= 0:
            self.standard_queue.append((pkg_id, weight))
    
    def process_packages(self):
        efficiency_scores = []
        truck_counter = 0
        
        # Process priority packages first (stack - LIFO)
        current_truck_load = []
        while self.priority_stack:
            pkg_id, weight = self.priority_stack.pop()
            if len(current_truck_load) < 5 and (not current_truck_load or sum(w for _, w in current_truck_load) + weight <= 800):
                current_truck_load.append((pkg_id, weight))
            else:
                load_factor = calculate_load_factor(truck_counter, [w for _, w in current_truck_load])
                self.truck_utilization[truck_counter] = load_factor
                efficiency_scores.append(load_factor * 100)
                truck_counter += 1
                current_truck_load = [(pkg_id, weight)]
        
        if current_truck_load:
            load_factor = calculate_load_factor(truck_counter, [w for _, w in current_truck_load])
            self.truck_utilization[truck_counter] = load_factor
            efficiency_scores.append(load_factor * 100)
            truck_counter += 1
        
        # Process standard packages (queue - FIFO)
        current_truck_load = []
        while self.standard_queue:
            pkg_id, weight = self.standard_queue.popleft()
            if len(current_truck_load) < 8 and (not current_truck_load or sum(w for _, w in current_truck_load) + weight <= 1000):
                current_truck_load.append((pkg_id, weight))
            else:
                load_factor = calculate_load_factor(truck_counter, [w for _, w in current_truck_load])
                self.truck_utilization[truck_counter] = load_factor
                efficiency_scores.append(load_factor * 100)
                truck_counter += 1
                current_truck_load = [(pkg_id, weight)]
        
        if current_truck_load:
            load_factor = calculate_load_factor(truck_counter, [w for _, w in current_truck_load])
            self.truck_utilization[truck_counter] = load_factor
            efficiency_scores.append(load_factor * 100)
        
        # Calculate final efficiency using greedy approach
        final_efficiency_score = 0
        if efficiency_scores:
            # Use itertools to find max efficiency segments
            segment_size = min(3, len(efficiency_scores))
            max_segment_sum = max(
                sum(efficiency_scores[i] for i in range(j, min(j+segment_size, len(efficiency_scores)))) 
                for j in range(len(efficiency_scores))
            )
            final_efficiency_score = int(max_segment_sum // 10)
        
        return final_efficiency_score

# Initialize processor
processor = PackageProcessor()

# Add packages with various weights and priorities
packages_data = [
    (101, 150, True), (102, 200, True), (103, 180, False), (104, 300, False),
    (105, 250, True), (106, 120, False), (107, 400, False), (108, 90, True),
    (109, 310, False), (110, 175, False), (111, 220, True), (112, 130, False)
]

for pkg_id, weight, is_priority in packages_data:
    processor.add_package(pkg_id, weight, is_priority)

# Process all packages and calculate final efficiency
final_efficiency_score = processor.process_packages()
print(f"Result: {final_efficiency_score}")