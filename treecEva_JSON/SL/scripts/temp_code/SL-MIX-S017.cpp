#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>

class SignalProcessor {
public:
    std::vector<double> samples;
    
    SignalProcessor(std::initializer_list<double> init) : samples(init) {}
    
    double computeNormalizedEnergy() const {
        double sum_of_squares = 0.0;
        for (const auto& sample : samples) {
            sum_of_squares += sample * sample;
        }
        return sum_of_squares / static_cast<double>(samples.size());
    }
};

int main() {
    SignalProcessor processor{1.5, 2.0, -1.0, 3.5, 0.5};
    double normalized_energy = processor.computeNormalizedEnergy();
    std::cout << "Result: " << normalized_energy << std::endl;
    return 0;
}