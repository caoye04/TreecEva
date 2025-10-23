#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <numeric>

class SignalStrength {
public:
    double value;
    
    SignalStrength(double v) : value(v) {}
    
    // Overload + operator to combine signal strengths
    SignalStrength operator+(const SignalStrength& other) const {
        return SignalStrength(this->value + other.value);
    }
    
    // Overload / operator for averaging
    SignalStrength operator/(double divisor) const {
        return SignalStrength(this->value / divisor);
    }
};

int main() {
    std::vector<SignalStrength> readings = {
        SignalStrength(2.5),
        SignalStrength(3.7),
        SignalStrength(1.8),
        SignalStrength(4.2),
        SignalStrength(3.3)
    };
    
    SignalStrength sum(0.0);
    for (const auto& reading : readings) {
        sum = sum + reading;
    }
    
    SignalStrength averageReading = sum / readings.size();
    
    std::cout << "Result: " << averageReading.value << std::endl;
    
    return 0;
}