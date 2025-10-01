#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_inner_sum(const vector<int>& nums) {
    double sum = 0;
    for (int num : nums) {
        sum += sqrt(abs(num));
    }
    return sum;
}

int main() {
    vector<vector<int>> matrix = {{-4, 9, -16}, {25, -36, 49}, {-64, 81, -100}};
    
    vector<double> row_sums(3);
    for (int i = 0; i < 3; ++i) {
        row_sums[i] = compute_inner_sum(matrix[i]);
    }
    
    double total_sum = 0;
    for (double val : row_sums) {
        total_sum += val;
    }
    
    int xor_accum = 0;
    for (const auto& row : matrix) {
        for (int elem : row) {
            xor_accum ^= abs(elem);
        }
    }
    
    double trig_result = sin(total_sum) + cos(xor_accum);
    
    int bit_shifted = (xor_accum << 2) & 255;
    
    double final_result = pow(trig_result, 3) * bit_shifted + log(row_sums[0] + row_sums[1] + row_sums[2]);
    
    cout << "Result: " << static_cast<long long>(final_result) << endl;
    
    return 0;
}