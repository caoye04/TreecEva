#define _USE_MATH_DEFINES
#include <iostream>
#include <algorithm>
#include <memory>

class SignalAnalyzer {
private:
    std::unique_ptr<int[]> signals;
    int count;

public:
    SignalAnalyzer(int* data, int size) : count(size) {
        signals = std::make_unique<int[]>(count);
        std::copy(data, data + count, signals.get());
    }
    
    double calculateMedian() {
        std::sort(signals.get(), signals.get() + count);
        
        if (count % 2 == 0) {
            return (signals.get()[count/2 - 1] + signals.get()[count/2]) / 2.0;
        } else {
            return signals.get()[count/2];
        }
    }
};

constexpr int sensor_count = 7;

int main() {
    int readings[sensor_count] = {45, 23, 67, 12, 89, 34, 56};
    
    SignalAnalyzer analyzer(readings, sensor_count);
    double median_signal = analyzer.calculateMedian();
    
    std::cout << "Result: " << median_signal << std::endl;
    
    return 0;
}