#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>

double compute_inner(double x, int n) {
    double acc = 1.0;
    for (int i = 1; i <= n; ++i) {
        acc *= (x + i) / i;
    }
    return acc;
}

int main() {
    std::vector<std::map<std::string, double>> data = {
        {{"value", 2.5}},
        {{"value", 3.0}},
        {{"value", 4.2}}
    };

    double accumulator = 0.0;
    int counter = 0;
    bool flag = true;

    for (auto& entry : data) {
        double val = entry["value"];
        if (val > 3.0) {
            accumulator += compute_inner(val, 3);
            counter += 2;
        } else {
            accumulator += val * 1.5;
            counter += 1;
        }
        flag = flag && (accumulator < 50.0);
    }

    double result = 0.0;
    if (flag) {
        result = pow(accumulator, 1.0 / counter) + log(counter + 1);
    } else {
        result = sqrt(accumulator) * counter;
    }

    // Bitwise manipulation
    int mask = 0xF0;
    int shifted = (static_cast<int>(result) << 2) & mask;
    result += (shifted ^ 0xAA);

    std::cout << "Result: " << result << std::endl;
    return 0;
}