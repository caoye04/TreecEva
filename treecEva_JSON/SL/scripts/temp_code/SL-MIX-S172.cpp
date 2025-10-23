#define _USE_MATH_DEFINES
#include <iostream>

class Signal {
public:
    int amplitude;
    constexpr Signal(int amp = 0) : amplitude(amp) {}
    
    Signal operator+(const Signal& other) const {
        return Signal(this->amplitude + other.amplitude);
    }
    
    Signal operator*(int factor) const {
        return Signal(this->amplitude * factor);
    }
};

constexpr int attenuate(int level) {
    return (level <= 1) ? 1 : (level % 2 == 0) ? attenuate(level / 2) + 2 : attenuate(level - 1) - 1;
}

int processSignal(Signal sig, int depth) {
    if (depth <= 0) return sig.amplitude;
    int adjusted = attenuate(sig.amplitude);
    Signal nextSig = (adjusted > 5) ? (sig * 2) : (sig + Signal(3));
    return processSignal(nextSig, depth - 1);
}

int main() {
    Signal initialSignal(7);
    int processedSignalStrength = processSignal(initialSignal, 3);
    std::cout << "Result: " << processedSignalStrength << std::endl;
    return 0;
}