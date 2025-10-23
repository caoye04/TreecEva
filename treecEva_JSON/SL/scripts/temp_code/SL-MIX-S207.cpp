#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <unordered_map>
#include <memory>

struct ThermalNode {
    double temperature;
    std::shared_ptr<ThermalNode> next;
    ThermalNode(double temp) : temperature(temp), next(nullptr) {}
};

class ThermalRegulator {
private:
    std::unordered_map<int, double> cache;
    
    double dissipateHeatRecursive(int depth, double currentTemp) {
        if (depth <= 0) return currentTemp;
        
        if (cache.find(depth) != cache.end()) {
            return cache[depth];
        }
        
        double dissipated = currentTemp * 0.85;
        double adjusted = dissipateHeatRecursive(depth - 1, dissipated);
        cache[depth] = adjusted;
        return adjusted;
    }
    
public:
    double computeOptimalCooling(std::shared_ptr<ThermalNode> head) {
        double totalEnergy = 0.0;
        auto current = head;
        int nodeCount = 0;
        
        // Greedy aggregation of thermal data
        while (current != nullptr) {
            double normalizedTemp = log(current->temperature + 1);
            totalEnergy += pow(normalizedTemp, 2.0);
            current = current->next;
            nodeCount++;
        }
        
        // Apply recursive dissipation model
        double predictedLoad = dissipateHeatRecursive(5, totalEnergy);
        
        // Calculate final cooling factor
        double coolingAdjustment = exp(predictedLoad / nodeCount) - 1;
        return coolingAdjustment;
    }
};

int main() {
    // Initialize thermal sensor network
    auto node1 = std::make_shared<ThermalNode>(85.5);
    auto node2 = std::make_shared<ThermalNode>(92.3);
    auto node3 = std::make_shared<ThermalNode>(78.9);
    auto node4 = std::make_shared<ThermalNode>(95.1);
    
    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    
    ThermalRegulator regulator;
    double optimalCoolingFactor = regulator.computeOptimalCooling(node1);
    
    std::cout << "Result: " << optimalCoolingFactor << std::endl;
    return 0;
}