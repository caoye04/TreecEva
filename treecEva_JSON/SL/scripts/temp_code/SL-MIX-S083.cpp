#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_expression(int x, int y) {
    return pow(x, 2) + sqrt(abs(y)) + log(static_cast<double>(x + y + 1));
}

int main() {
    vector<map<string, pair<int, double>>> data = {
        {{"alpha", {5, 3.14}}, {"beta", {7, 2.71}}},
        {{"gamma", {10, 1.41}}, {"delta", {3, 0.57}}},
        {{"epsilon", {2, 0.70}}, {"zeta", {8, 1.73}}}
    };

    int accumulator = 0;
    double sum_of_computations = 0.0;
    string concatenated_keys = "";

    for (size_t i = 0; i < data.size(); ++i) {
        for (const auto& entry : data[i]) {
            const string& key = entry.first;
            const pair<int, double>& values = entry.second;
            int first_val = values.first;
            double second_val = values.second;

            accumulator ^= (first_val << static_cast<int>(second_val));
            sum_of_computations += compute_expression(first_val, static_cast<int>(second_val));
            concatenated_keys += key.substr(0, min(key.length(), static_cast<size_t>(2)));
        }
    }

    size_t key_length_mask = concatenated_keys.length() & 0xF;
    double adjusted_sum = sum_of_computations * (1.0 + key_length_mask / 10.0);
    int final_xor_operation = accumulator ^ static_cast<int>(adjusted_sum);
    int final_result = final_xor_operation % 1000;

    cout << "Result: " << final_result << endl;
    return 0;
}