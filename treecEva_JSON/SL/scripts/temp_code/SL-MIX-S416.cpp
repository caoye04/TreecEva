#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct DataPoint {
    double x;
    double y;
    int category;
};

class DataProcessor {
private:
    vector<DataPoint> data;

public:
    DataProcessor(vector<DataPoint> input) : data(input) {}
    
    double computeWeightedVariance(int cat) {
        vector<double> values;
        for (const auto& point : data) {
            if (point.category == cat) {
                values.push_back(point.x * point.y);
            }
        }
        
        if (values.empty()) return 0.0;
        
        double sum = 0.0;
        for (double val : values) {
            sum += val;
        }
        double mean = sum / values.size();
        
        double variance = 0.0;
        for (double val : values) {
            variance += (val - mean) * (val - mean);
        }
        
        return variance / values.size();
    }
    
    int countPointsInRegion(double x_min, double x_max, double y_min, double y_max) {
        int count = 0;
        for (const auto& point : data) {
            if (point.x >= x_min && point.x <= x_max && 
                point.y >= y_min && point.y <= y_max) {
                count++;
            }
        }
        return count;
    }
};

int main() {
    vector<DataPoint> dataset = {
        {1.5, 2.3, 1},
        {2.7, 1.8, 2},
        {3.3, 4.1, 1},
        {0.9, 3.7, 3},
        {4.2, 2.5, 2},
        {1.1, 1.9, 1},
        {3.8, 3.3, 3},
        {2.2, 4.4, 2}
    };
    
    DataProcessor processor(dataset);
    
    double var1 = processor.computeWeightedVariance(1);
    double var2 = processor.computeWeightedVariance(2);
    double var3 = processor.computeWeightedVariance(3);
    
    int count1 = processor.countPointsInRegion(1.0, 3.0, 1.0, 3.0);
    int count2 = processor.countPointsInRegion(2.0, 4.0, 2.0, 4.0);
    
    double intermediate = pow(var1, 1.5) + sqrt(var2) * log(var3 + 1);
    
    vector<double> results;
    results.push_back(intermediate);
    results.push_back(sin(var1) * cos(var2));
    results.push_back(static_cast<double>(count1) / static_cast<double>(count2));
    
    sort(results.begin(), results.end());
    
    bool condition = (var1 > var2) && (count1 < count2) || (var3 < 2.0);
    
    double result;
    if (condition) {
        result = results[0] * 2.0 + results[2];
    } else {
        result = results[1] + results[2] * 1.5;
    }
    
    result = static_cast<int>(result * 1000) % 256;
    
    cout << "Result: " << result << endl;
    
    return 0;
}