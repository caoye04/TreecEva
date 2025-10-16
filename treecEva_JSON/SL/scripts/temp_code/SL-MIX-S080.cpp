#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <optional>

constexpr int tribonacci(int n) {
    if (n <= 2) return n == 2 ? 1 : 0;
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3);
}

std::optional<int> calculateTiming(int baseFlow, int correctionFactor) {
    if (baseFlow <= 0 || correctionFactor <= 0) return std::nullopt;
    return (baseFlow * correctionFactor) / (baseFlow + correctionFactor);
}

int adaptiveTimingAlgorithm(int sensorReadings[], int size) {
    int cumulativeAdjustment = 0;
    bool isValid = true;
    
    for (int i = 0; i < size && isValid; ++i) {
        int tribValue = tribonacci(sensorReadings[i]);
        auto timing = calculateTiming(tribValue, i+1);
        
        if (timing.has_value() && (i % 2 == 0 || tribValue > 0)) {
            cumulativeAdjustment += timing.value();
        } else {
            isValid = false;
        }
    }
    
    return isValid ? cumulativeAdjustment : -1;
}

int main() {
    int trafficSensors[] = {4, 5, 3, 6, 2};
    int sensorCount = sizeof(trafficSensors)/sizeof(trafficSensors[0]);
    
    int optimalTiming = adaptiveTimingAlgorithm(trafficSensors, sensorCount);
    
    std::cout << "Result: " << optimalTiming << std::endl;
    return 0;
}