#define _USE_MATH_DEFINES
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

struct Package {
    int id;
    double weight;
    int urgency;
    double ratio; // urgency/weight
    
    bool operator<(const Package& other) const {
        return ratio < other.ratio; // Max heap based on ratio
    }
};

template<typename T>
class PriorityQueue {
private:
    std::priority_queue<T> pq;
public:
    void push(const T& item) { pq.push(item); }
    T top() const { return pq.top(); }
    void pop() { pq.pop(); }
    bool empty() const { return pq.empty(); }
    size_t size() const { return pq.size(); }
};

int main() {
    const double VEHICLE_CAPACITY = 100.0;
    
    // Initialize packages with ID, weight, urgency
    std::vector<Package> packages = {
        {1, 30.5, 80, 0},
        {2, 20.0, 65, 0},
        {3, 15.2, 50, 0},
        {4, 40.0, 90, 0},
        {5, 25.3, 70, 0}
    };
    
    // Calculate urgency-to-weight ratios
    for(auto& pkg : packages) {
        pkg.ratio = pkg.urgency / pkg.weight;
    }
    
    // Sort packages by ratio in descending order for preprocessing
    std::sort(packages.begin(), packages.end(), [](const Package& a, const Package& b) {
        return a.ratio > b.ratio;
    });
    
    // Load packages into priority queue
    PriorityQueue<Package> packageQueue;
    for(const auto& pkg : packages) {
        packageQueue.push(pkg);
    }
    
    double currentLoad = 0.0;
    double totalSelectedWeight = 0.0;
    
    // Greedy selection process
    while(!packageQueue.empty() && currentLoad < VEHICLE_CAPACITY) {
        Package currentPackage = packageQueue.top();
        packageQueue.pop();
        
        // Check if adding this package exceeds capacity
        bool canAdd = (currentLoad + currentPackage.weight) <= VEHICLE_CAPACITY;
        
        // Ternary operator to decide whether to add the package
        totalSelectedWeight += canAdd ? currentPackage.weight : 0.0;
        currentLoad += canAdd ? currentPackage.weight : 0.0;
    }
    
    // Final adjustment using greedy principle - check remaining capacity
    double remainingCapacity = VEHICLE_CAPACITY - currentLoad;
    
    // If there's still space, try to fit a smaller package
    if(remainingCapacity > 0 && !packageQueue.empty()) {
        // Search for a package that fits in remaining space
        std::vector<Package> tempStorage;
        bool found = false;
        
        while(!packageQueue.empty() && !found) {
            Package candidate = packageQueue.top();
            packageQueue.pop();
            
            if(candidate.weight <= remainingCapacity) {
                totalSelectedWeight += candidate.weight;
                found = true;
            } else {
                tempStorage.push_back(candidate);
            }
        }
        
        // Restore unprocessed packages
        for(const auto& pkg : tempStorage) {
            packageQueue.push(pkg);
        }
    }
    
    std::cout << "Result: " << static_cast<int>(totalSelectedWeight * 100 + 0.5) << std::endl;
    return 0;
}