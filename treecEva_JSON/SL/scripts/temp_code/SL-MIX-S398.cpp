#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

double compute_recursive(double base, int exp) {
    if (exp == 0) return 1.0;
    if (exp % 2 == 0) {
        double half = compute_recursive(base, exp / 2);
        return half * half;
    }
    return base * compute_recursive(base, exp - 1);
}

struct DataPoint {
    vector<int> values;
    double weight;
    bool flag;
};

int main() {
    vector<DataPoint> dataset(2);
    dataset[0] = {{2, 4, 8}, 1.5, true};
    dataset[1] = {{3, 9, 27}, 2.0, false};
    
    double accumulator = 0.0;
    int xor_result = 0;
    
    for(int i=0; i<dataset.size(); i++) {
        DataPoint dp = dataset[i];
        double local_sum = 0;
        for(int j=0; j<dp.values.size(); j++) {
            local_sum += pow(dp.values[j], 1.0/3.0); // Cube root
        }
        if(dp.flag) {
            local_sum *= dp.weight;
            xor_result ^= static_cast<int>(floor(local_sum));
        } else {
            local_sum /= dp.weight;
            xor_result ^= static_cast<int>(ceil(local_sum));
        }
        accumulator += local_sum;
    }
    
    int bit_shifted = (xor_result << 2) | 3;
    double exponent = compute_recursive(accumulator, 2);
    double sine_val = sin(exponent);
    int result = static_cast<int>(floor(sine_val * bit_shifted * 1000));
    
    cout << "Result: " << result << endl;
    return 0;
}