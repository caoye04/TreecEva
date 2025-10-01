#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * c - sin(c);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<int> flat;
    for (const auto& row : matrix) {
        for (int val : row) {
            flat.push_back(val);
        }
    }
    
    int sum = 0;
    for (int i = 0; i < flat.size(); i++) {
        if (i % 2 == 0) {
            sum += flat[i];
        } else {
            sum -= flat[i];
        }
    }
    
    string s = "ComplexReasoning";
    int char_sum = 0;
    for (char c : s) {
        char_sum += static_cast<int>(c);
    }
    
    double x = compute_expression(sum, char_sum, 1.5);
    
    vector<double> results;
    for (int i = 1; i <= 5; i++) {
        results.push_back(x / i + pow(i, 1.5));
    }
    
    double max_val = *max_element(results.begin(), results.end());
    double min_val = *min_element(results.begin(), results.end());
    
    int a = static_cast<int>(max_val);
    int b = static_cast<int>(min_val);
    
    int final_result = (a & b) ^ (a | b);
    final_result >>= 2;
    
    cout << "Result: " << final_result << endl;
    return 0;
}