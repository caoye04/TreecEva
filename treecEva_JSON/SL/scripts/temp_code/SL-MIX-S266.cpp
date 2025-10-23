#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <optional>

class PackageLoader {
private:
    std::vector<std::pair<int, int>> packages; // {priority, weight}
    int truckCapacity;
    int minLoadRequirement;
    int loadedPackages;
    
    bool tryGreedyLoad() {
        // Sort by priority descending
        std::sort(packages.begin(), packages.end(), 
                  [](const auto& a, const auto& b) { return a.first > b.first; });
        
        int currentWeight = 0;
        loadedPackages = 0;
        
        for (const auto& pkg : packages) {
            if (currentWeight + pkg.second <= truckCapacity) {
                currentWeight += pkg.second;
                loadedPackages++;
            }
            // Early return if we've met minimum requirement
            if (currentWeight >= minLoadRequirement && 
                (packages.size() <= 5 || loadedPackages >= 3)) {
                return true;
            }
        }
        
        return currentWeight >= minLoadRequirement;
    }
    
    std::optional<int> backtrackLoad(int index, int currentWeight, int count) {
        // Base cases
        if (currentWeight >= minLoadRequirement && currentWeight <= truckCapacity) {
            return count;
        }
        if (index >= static_cast<int>(packages.size()) || 
            currentWeight > truckCapacity) {
            return std::nullopt;
        }
        
        // Try including current package
        auto withPackage = backtrackLoad(index + 1, 
                                        currentWeight + packages[index].second, 
                                        count + 1);
        
        // Try excluding current package (short-circuit if withPackage is valid)
        std::optional<int> withoutPackage;
        if (!withPackage.has_value() || withPackage.value() > count) {
            withoutPackage = backtrackLoad(index + 1, currentWeight, count);
        }
        
        // Return better solution
        if (withPackage.has_value() && withoutPackage.has_value()) {
            return std::min(withPackage.value(), withoutPackage.value());
        } else if (withPackage.has_value()) {
            return withPackage;
        } else {
            return withoutPackage;
        }
    }

public:
    PackageLoader(int capacity, int minLoad) 
        : truckCapacity(capacity), minLoadRequirement(minLoad), loadedPackages(0) {}
    
    void addPackage(int priority, int weight) {
        packages.push_back({priority, weight});
    }
    
    int executeLoading() {
        // Try greedy approach first
        if (tryGreedyLoad()) {
            return loadedPackages;
        }
        
        // If greedy fails, use backtracking
        auto result = backtrackLoad(0, 0, 0);
        if (result.has_value()) {
            loadedPackages = result.value();
            return loadedPackages;
        }
        
        // If both fail, load nothing
        loadedPackages = 0;
        return 0;
    }
};

int main() {
    PackageLoader loader(100, 70);
    
    // Add packages: {priority, weight}
    loader.addPackage(5, 30);
    loader.addPackage(8, 25);
    loader.addPackage(3, 20);
    loader.addPackage(7, 15);
    loader.addPackage(6, 35);
    loader.addPackage(4, 10);
    loader.addPackage(9, 40);
    
    int loadedPackages = loader.executeLoading();
    
    std::cout << "Result: " << loadedPackages << std::endl;
    return 0;
}