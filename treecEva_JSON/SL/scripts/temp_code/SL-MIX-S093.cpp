#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <vector>

class SignalAmplifier {
private:
    double gain;
    int stageCount;

public:
    constexpr SignalAmplifier(double g, int stages) : gain(g), stageCount(stages) {}
    
    double operator()(double input) const {
        return input * std::pow(gain, stageCount);
    }
};

int main() {
    // Signal processing pipeline
    std::vector<double> rawSensorReadings = {2.5, 3.7, 1.2, 4.8, 2.1};
    
    // Calculate mean of readings
    double sum = 0;
    for (const auto& reading : rawSensorReadings) {
        sum += reading;
    }
    double meanReading = sum / rawSensorReadings.size();
    
    // Calculate variance
    double varianceSum = 0;
    for (const auto& reading : rawSensorReadings) {
        varianceSum += std::pow(reading - meanReading, 2);
    }
    double readingVariance = varianceSum / rawSensorReadings.size();
    
    // Signal conditioning parameters
    bool isHighGainMode = (meanReading > 3.0) && (readingVariance < 2.0);
    bool isNoiseFilterActive = (readingVariance > 1.0) || (meanReading < 2.0);
    
    // Amplification setup using RAII
    constexpr SignalAmplifier amplifier(1.5, isHighGainMode ? 3 : 2);
    
    // Process signal with noise considerations
    double conditionedSignal = 0;
    if (isNoiseFilterActive && isHighGainMode) {
        conditionedSignal = amplifier(meanReading) - (readingVariance * 0.5);
    } else if (isNoiseFilterActive || !isHighGainMode) {
        conditionedSignal = amplifier(meanReading) + (readingVariance * 0.3);
    } else {
        conditionedSignal = amplifier(meanReading);
    }
    
    // Final conditioning score calculation using lambda
    auto computeConditioningScore = [readingVariance](double signal, bool filter) -> double {
        return filter ? signal * (1.0 + readingVariance/10.0) : signal;
    };
    
    double finalConditioningScore = computeConditioningScore(conditionedSignal, isNoiseFilterActive);
    
    std::cout << "Result: " << finalConditioningScore << std::endl;
    return 0;
}