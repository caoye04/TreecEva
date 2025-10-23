#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>

class Accumulator {
public:
    double value;
    
    Accumulator(double v = 0.0) : value(v) {}
    
    // Move constructor
    Accumulator(Accumulator&& other) noexcept : value(other.value) {
        other.value = 0.0;
    }
    
    // Move assignment operator
    Accumulator& operator=(Accumulator&& other) noexcept {
        if (this != &other) {
            value = other.value;
            other.value = 0.0;
        }
        return *this;
    }
    
    // Overloaded += operator
    Accumulator& operator+=(const double& rhs) {
        value += rhs;
        return *this;
    }
};

int main() {
    Accumulator climateIndex(15.5);
    Accumulator tempAdjustment(0.0);
    
    bool isValid = true;
    double reading = 22.3;
    int sensorFlag = 0;
    
    // Short-circuit evaluation in condition
    if (isValid && (sensorFlag == 0 || reading > 20.0)) {
        tempAdjustment += reading;
        tempAdjustment += std::sqrt(9.0);
    }
    
    // Move semantics
    climateIndex = std::move(tempAdjustment);
    
    // Additional floating-point operation
    climateIndex += 0.7 * 2.0;
    
    std::cout << "Result: " << climateIndex.value << std::endl;
    return 0;
}