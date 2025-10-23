#define _USE_MATH_DEFINES
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <memory>

class SignalProcessor {
private:
    std::map<int, int> signalRegistry;
    std::vector<int> modifiers;

public:
    SignalProcessor() {
        signalRegistry = {{1, 10}, {2, 20}, {3, 30}, {4, 40}};
        modifiers = {2, 3, 1, 4};
    }

    int processSignals() {
        auto signalAccumulator = std::make_unique<int>(0);
        bool isValid = true;
        
        for (const auto& modifier : modifiers) {
            if (signalRegistry.count(modifier) && modifier > 1) {
                *signalAccumulator += signalRegistry[modifier] * modifier;
                isValid = isValid && (signalRegistry[modifier] % 10 == 0);
            } else {
                isValid = false;
            }
        }
        
        // Execution point Y
        int processedSignalStrength = *signalAccumulator;
        if (!isValid) {
            processedSignalStrength = -1;
        } else {
            processedSignalStrength += 5;
        }
        
        return processedSignalStrength;
    }
};

int main() {
    SignalProcessor processor;
    int result = processor.processSignals();
    std::cout << "Result: " << result << std::endl;
    return 0;
}