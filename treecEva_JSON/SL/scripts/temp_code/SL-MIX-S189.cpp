#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>

template<int N>
struct Power {
    static constexpr double eval(double base) {
        return base * Power<N-1>::eval(base);
    }
};

template<>
struct Power<0> {
    static constexpr double eval(double) {
        return 1.0;
    }
};

class EnergyCalculator {
private:
    double energy;
    int count;

public:
    EnergyCalculator() : energy(0.0), count(0) {}
    
    double addReading(double current, double previous) {
        double diff = current - previous;
        double decay_factor = std::exp(-0.1 * count);
        energy += Power<2>::eval(diff) * decay_factor;
        count++;
        return energy;
    }
    
    double getTotalEnergy() const { return energy; }
};

constexpr double computeDecay(int step) {
    return std::log(step + 2.0);
}

double processReadings(const std::vector<double>& readings) {
    if (readings.size() < 2) return 0.0;
    
    EnergyCalculator calc;
    double total = 0.0;
    
    for (size_t i = 1; i < readings.size(); ++i) {
        total = calc.addReading(readings[i], readings[i-1]);
        if (i >= 2) {
            total *= computeDecay(i);
        }
    }
    
    return calc.getTotalEnergy() + total;
}

int main() {
    std::vector<double> sensor_readings = {2.0, 3.0, 1.0, 4.0};
    double final_energy = processReadings(sensor_readings);
    std::cout << "Result: " << final_energy << std::endl;
    return 0;
}