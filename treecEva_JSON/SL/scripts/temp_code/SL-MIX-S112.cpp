#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>

template<int N>
struct Factorial {
    static constexpr int value = N * Factorial<N - 1>::value;
};

template<>
struct Factorial<0> {
    static constexpr int value = 1;
};

class SensorArray {
private:
    std::vector<int> signals;

public:
    SensorArray(std::initializer_list<int> list) : signals(list) {}
    
    template<typename... Args>
    int computeModularSum(Args... vals) const {
        int sum = (vals + ...);
        return sum % signals.size();
    }
    
    int getSignal(int index) const {
        return signals[index];
    }
};

int main() {
    SensorArray sensors{3, 7, 2, 5, 9};
    int transmissionScore = 0;
    
    for (int i = 0; i < 4; ++i) {
        for (int j = i + 1; j < 5; ++j) {
            int combinationIndex = Factorial<3>::value / (Factorial<2>::value * Factorial<1>::value); // 3C2
            int modularResult = sensors.computeModularSum(sensors.getSignal(i), sensors.getSignal(j));
            transmissionScore += (combinationIndex * modularResult) % 7;
        }
    }
    
    std::cout << "Result: " << transmissionScore << std::endl;
    return 0;
}