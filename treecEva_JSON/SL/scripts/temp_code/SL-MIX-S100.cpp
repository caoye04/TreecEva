#define _USE_MATH_DEFINES
#include <iostream>
#include <queue>
#include <vector>
#include <unordered_map>
#include <algorithm>

struct Container {
    int id;
    int weight;
    int zone;
    int urgency;
    int priority;
    
    Container(int i, int w, int z, int u) : id(i), weight(w), zone(z), urgency(u) {
        priority = (weight * 2) + (zone * 3) + (urgency * 5);
    }
};

struct Compare {
    bool operator()(const Container& a, const Container& b) {
        return a.priority < b.priority;
    }
};

int main() {
    // Priority queue (max-heap) for containers
    std::priority_queue<Container, std::vector<Container>, Compare> container_heap;
    
    // Zone priority mapping
    std::unordered_map<int, int> zone_priority = {{1, 10}, {2, 7}, {3, 5}, {4, 3}};
    
    // Initialize containers
    std::vector<Container> containers;
    containers.emplace_back(101, 50, 1, 8);
    containers.emplace_back(102, 30, 2, 6);
    containers.emplace_back(103, 70, 1, 9);
    containers.emplace_back(104, 40, 3, 4);
    containers.emplace_back(105, 60, 2, 7);
    containers.emplace_back(106, 20, 4, 5);
    containers.emplace_back(107, 80, 1, 10);
    
    // Adjust priorities based on zone mapping
    for (auto& container : containers) {
        container.priority += zone_priority[container.zone];
        container_heap.push(container);
    }
    
    // Process first batch (top 3 priority containers)
    int processed_count = 0;
    while (!container_heap.empty() && processed_count < 3) {
        Container top = container_heap.top();
        container_heap.pop();
        processed_count++;
        
        // Early return if we find a container with priority over 200
        if (top.priority > 200) {
            std::cout << "Target result: " << top.priority << std::endl;
            return 0;
        }
    }
    
    // Get the top priority score of remaining containers
    int top_priority_score = 0;
    if (!container_heap.empty()) {
        top_priority_score = container_heap.top().priority;
    }
    
    std::cout << "Target result: " << top_priority_score << std::endl;
    return 0;
}