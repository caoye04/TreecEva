#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_inner_value(const vector<vector<int>>& matrix, int row) {
    double sum = 0;
    for (int val : matrix[row]) {
        sum += sqrt(abs(val));
    }
    return sum;
}

int main() {
    vector<vector<int>> data = {{-16, 9, -4}, {25, -36, 49}, {-64, 81, -100}};
    vector<double> intermediates(3);
    
    for (int i = 0; i < 3; i++) {
        intermediates[i] = compute_inner_value(data, i);
    }
    
    double max_val = *max_element(intermediates.begin(), intermediates.end());
    int max_index = 0;
    for (int i = 0; i < 3; i++) {
        if (intermediates[i] == max_val) {
            max_index = i;
            break;
        }
    }
    
    bool conditions[3];
    for (int i = 0; i < 3; i++) {
        conditions[i] = (intermediates[i] > 10.0) && (data[i][0] < 0);
    }
    
    int count = 0;
    for (int i = 0; i < 3; i++) {
        count += conditions[i] ? 1 : 0;
    }
    
    double result = 0;
    if (count >= 2) {
        result = pow(intermediates[max_index], 2) + 2 * M_PI * max_index;
    } else {
        double product = 1;
        for (double val : intermediates) {
            product *= val;
        }
        result = product / (max_val + 1);
    }
    
    result = floor(result * 1000) / 1000; // Round to 3 decimal places
    cout << "Result: " << result << endl;
    return 0;
}