#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

double recursive_power_sum(vector<int>& nums, int index) {
    if (index >= nums.size()) return 0;
    double val = pow(nums[index], 3);
    return val + recursive_power_sum(nums, index + 1);
}

int main() {
    vector<vector<int>> matrix = {{2, 3}, {4, 5}, {6, 7}};
    int xor_accum = 0;
    double sum_powers = 0;
    
    for(int i=0; i<matrix.size(); i++) {
        vector<int> row = matrix[i];
        int local_xor = row[0] ^ row[1];
        xor_accum |= local_xor;
        sum_powers += recursive_power_sum(row, 0);
    }
    
    long long factorial = 1;
    for(int i=1; i<=xor_accum; i++) {
        factorial *= i;
    }
    
    double log_val = log(factorial);
    double sin_component = sin(log_val);
    double cos_component = cos(sum_powers / 100.0);
    
    double computed_value = round((sin_component + cos_component) * 1000);
    
    cout << "Result: " << computed_value << endl;
    return 0;
}