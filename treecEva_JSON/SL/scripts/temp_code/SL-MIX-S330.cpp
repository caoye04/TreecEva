#define _USE_MATH_DEFINES
#include <iostream>

template<int Depth>
constexpr int encodeSignal(int signalStrength) {
    if constexpr (Depth <= 0) {
        return signalStrength;
    } else {
        int transformed = (signalStrength * 3 + 7) & 0xFF;
        return encodeSignal<Depth-1>(transformed) ^ (signalStrength >> 2);
    }
}

int main() {
    constexpr int initialSignal = 12;
    constexpr int maxDepth = 4;
    
    int encodedSignal = encodeSignal<maxDepth>(initialSignal);
    
    std::cout << "Result: " << encodedSignal << std::endl;
    return 0;
}