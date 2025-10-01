#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <string>

using namespace std;

double compute_inner_value(const vector<int>& nums, int index) {
    if (index < 0 || index >= nums.size()) return 0;
    double val = pow(nums[index], 2) + sqrt(abs(nums[index]));
    return val;
}

int main() {
    vector<int> data = {4, -9, 16, -25, 36};
    map<string, double> results;
    
    for (int i = 0; i < data.size(); i++) {
        string key = "val_" + to_string(i);
        double inner = compute_inner_value(data, i);
        results[key] = inner;
    }
    
    double accumulator = 0;
    for (const auto& entry : results) {
        accumulator += entry.second;
    }
    
    int bitwise = (data[0] & data[1]) | (data[2] ^ data[3]);
    double trig_result = sin(accumulator) + cos(bitwise);
    
    vector<vector<double>> matrix(3, vector<double>(3, 0.0));
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            matrix[i][j] = trig_result * (i + 1) * (j + 1);
        }
    }
    
    double diag_sum = 0;
    for (int i = 0; i < 3; i++) {
        diag_sum += matrix[i][i];
    }
    
    double final_result = round((diag_sum + accumulator) * 1000) / 1000;
    cout << "Result: " << final_result << endl;
    return 0;
}