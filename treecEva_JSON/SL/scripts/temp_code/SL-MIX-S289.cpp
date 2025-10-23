#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>

class SignalSegment {
public:
    double amplitude;
    int frequency;
    
    constexpr SignalSegment(double amp = 0, int freq = 0) : amplitude(amp), frequency(freq) {}
    
    SignalSegment operator+(const SignalSegment& other) const {
        return SignalSegment(amplitude + other.amplitude, frequency + other.frequency);
    }
    
    SignalSegment operator*(double factor) const {
        return SignalSegment(amplitude * factor, frequency);
    }
};

constexpr double adjustGain(int freq) {
    return (freq > 1000) ? 1.5 : (freq > 500 ? 1.2 : 1.0);
}

SignalSegment processSegment(SignalSegment seg, int depth) {
    if (depth <= 0) {
        double gain = adjustGain(seg.frequency);
        return seg * gain;
    }
    
    SignalSegment left(seg.amplitude/2, seg.frequency-100);
    SignalSegment right(seg.amplitude/2, seg.frequency+100);
    
    SignalSegment processedLeft = processSegment(left, depth-1);
    SignalSegment processedRight = processSegment(right, depth-1);
    
    return processedLeft + processedRight;
}

int main() {
    SignalSegment baseSegment(100.0, 800);
    SignalSegment processed = processSegment(baseSegment, 2);
    
    int harmonicLevel = 3;
    double modulationFactor;
    switch(harmonicLevel) {
        case 1: modulationFactor = 1.1; break;
        case 2: modulationFactor = 1.2; break;
        case 3: modulationFactor = 1.3; break;
        default: modulationFactor = 1.0;
    }
    
    double finalAmplitude = processed.amplitude * modulationFactor;
    std::cout << "Result: " << finalAmplitude << std::endl;
    return 0;
}