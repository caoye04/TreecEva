#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>

template<int N>
struct ModifiedFibonacci {
    static constexpr int value = ModifiedFibonacci<N-1>::value + ModifiedFibonacci<N-2>::value;
};

template<>
struct ModifiedFibonacci<0> {
    static constexpr int value = 13;
};

template<>
struct ModifiedFibonacci<1> {
    static constexpr int value = 21;
};

constexpr int getPackageWeight(int index) {
    return ModifiedFibonacci<0>::value * (index == 0) +
           ModifiedFibonacci<1>::value * (index == 1) +
           ModifiedFibonacci<2>::value * (index == 2) +
           ModifiedFibonacci<3>::value * (index == 3) +
           ModifiedFibonacci<4>::value * (index == 4) +
           ModifiedFibonacci<5>::value * (index == 5) +
           ModifiedFibonacci<6>::value * (index == 6) +
           ModifiedFibonacci<7>::value * (index == 7) +
           ModifiedFibonacci<8>::value * (index == 8) +
           ModifiedFibonacci<9>::value * (index == 9);
}

int main() {
    const int truckCapacity = 2000;
    std::vector<int> packageWeights;
    
    // Generate package weights following modified Fibonacci sequence
    for (int i = 0; i < 10; ++i) {
        packageWeights.push_back(getPackageWeight(i));
    }
    
    // Sort packages in ascending order for greedy approach
    std::sort(packageWeights.begin(), packageWeights.end());
    
    // Greedy algorithm: load as many packages as possible
    int loadedPackages = 0;
    int currentLoad = 0;
    
    for (int weight : packageWeights) {
        if (currentLoad + weight <= truckCapacity) {
            currentLoad += weight;
            loadedPackages++;
        } else {
            break;
        }
    }
    
    std::cout << "Result: " << loadedPackages << std::endl;
    return 0;
}