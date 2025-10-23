#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>

class Amplifier {
private:
    double factor;
public:
    constexpr Amplifier(double f) : factor(f) {}
    
    double operator()(double input) const {
        return input * factor;
    }
};

int main() {
    double inputSignal = -0.5;
    double amplificationFactor = (std::abs(inputSignal) > 1.0) ? 2.5 : 1.2;
    auto amplifier = Amplifier(amplificationFactor);
    double amplifiedSignal = amplifier(inputSignal);
    double bias = 0.1;
    double processedSignal = amplifiedSignal - bias;
    std::cout << "Result: " << processedSignal << std::endl;
    return 0;
}