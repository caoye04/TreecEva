#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

struct SampleProcessor {
    double baseGain;
    
    constexpr SampleProcessor(double gain) : baseGain(gain) {}
    
    double operator()(double sample) const {
        return sample * baseGain;
    }
};

int main() {
    std::vector<double> audioSamples = {0.5, -0.8, 1.2, -0.3, 0.9};
    SampleProcessor processor(1.5);
    
    double cumulativeEffect = 0.0;
    int processingMode = 2;
    
    for (size_t i = 0; i < audioSamples.size(); ++i) {
        double adjustedSample = processor(audioSamples[i]);
        
        switch (processingMode) {
            case 1:
                cumulativeEffect += std::abs(adjustedSample);
                break;
            case 2: {
                auto transform = [adjustedSample](double factor) {
                    return std::pow(adjustedSample, factor);
                };
                cumulativeEffect += transform(1.2);
                break;
            }
            case 3:
                cumulativeEffect += std::sqrt(std::abs(adjustedSample));
                break;
            default:
                cumulativeEffect += adjustedSample;
        }
        
        if (i % 2 == 0) {
            processingMode = (processingMode == 2) ? 3 : 1;
        }
    }
    
    std::sort(audioSamples.begin(), audioSamples.end(), [](double a, double b) {
        return std::abs(a) > std::abs(b);
    });
    
    double finalAdjustment = cumulativeEffect;
    if (std::abs(audioSamples.front()) > 1.0) {
        finalAdjustment *= 0.8;
    } else {
        finalAdjustment += 0.5;
    }
    
    std::cout << "Result: " << finalAdjustment << std::endl;
    return 0;
}