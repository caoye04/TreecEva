#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * sin(c);
}

struct DataPoint {
    int id;
    vector<double> values;
};

int main() {
    const double PI = 3.141592653589793;
    
    // Initialize variables
    int x = 5;
    double y = 2.5;
    int z = x * 3 - 2;
    
    // Bitwise operations
    int bitmask = (x << 2) & (z >> 1);
    
    // Conditional logic with short-circuit evaluation
    bool condition = (bitmask > 10) && (y < 3.0);
    
    // Nested data structures
    vector<DataPoint> dataset = {
        {1, {1.1, 2.2, 3.3}},
        {2, {4.4, 5.5, 6.6}},
        {3, {7.7, 8.8, 9.9}}
    };
    
    // Mathematical computation
    double intermediate = compute_expression(x, z, PI / 4);
    
    // Modify dataset based on condition
    if (condition || (intermediate > 50)) {
        for (auto& point : dataset) {
            for (double& val : point.values) {
                val = val * 1.5 + 0.5;
            }
        }
    }
    
    // Aggregate results from dataset
    double sum_values = 0.0;
    for (const auto& point : dataset) {
        sum_values += accumulate(point.values.begin(), point.values.end(), 0.0);
    }
    
    // Final complex calculation
    double final_result = (intermediate + sum_values) / (bitmask + 1) + static_cast<int>(condition);
    
    cout << "Result: " << final_result << endl;
    return 0;
}