#define _USE_MATH_DEFINES
#include <iostream>
#include <array>
#include <cmath>

class TriangularWindow {
public:
    static constexpr double windowFunction(int n, int N) {
        return 1.0 - std::abs((n - (N-1)/2.0)) / ((N-1)/2.0);
    }
};

int main() {
    constexpr int N = 5;
    std::array<double, N> raw_samples = {10.0, 20.0, 30.0, 40.0, 50.0};
    double processed_sum = 0.0;
    
    for (int i = 0; i < N; ++i) {
        double window_value = TriangularWindow::windowFunction(i, N);
        processed_sum += raw_samples[i] * window_value;
    }
    
    std::cout << "Result: " << processed_sum << std::endl;
    return 0;
}