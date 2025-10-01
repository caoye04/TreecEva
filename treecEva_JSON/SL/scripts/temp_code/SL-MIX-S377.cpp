#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct DataPoint {
    int x;
    double y;
    DataPoint(int x_val, double y_val) : x(x_val), y(y_val) {}
};

struct ComplexData {
    vector<DataPoint> points;
    int meta_value;
    ComplexData(int mv) : meta_value(mv) {}
    void add_point(int x, double y) {
        points.emplace_back(x, y);
    }
};

int main() {
    // Initialize data structures
    ComplexData data(12);
    data.add_point(5, 3.14);
    data.add_point(7, 2.71);
    data.add_point(11, 1.41);
    
    // Perform mathematical transformations
    double accumulator = 0.0;
    for(size_t i = 0; i < data.points.size(); ++i) {
        DataPoint& p = data.points[i];
        double transformed = pow(p.x, 2) * sin(p.y) + log(p.x + 1);
        accumulator += transformed;
    }
    
    // Bitwise manipulations
    int mask = (data.meta_value << 2) ^ 0xF0;
    int shifted = (mask >> 1) & 0x7F;
    
    // Advanced calculations
    double base_calc = sqrt(accumulator) * 2.5;
    int rounded = static_cast<int>(round(base_calc));
    
    // Conditional logic with multiple branches
    int conditional_result;
    if(rounded > 50) {
        conditional_result = (rounded & 0xFF) | 0x100;
    } else if(rounded < 20) {
        conditional_result = (rounded << 3) ^ 0xAA;
    } else {
        conditional_result = rounded * 3 + 7;
    }
    
    // Final computation
    int target_result = (conditional_result + shifted) % 1000;
    // TARGET VARIABLE VALUE
    
    cout << "Result: " << target_result << endl;
    return 0;
}