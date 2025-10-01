#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <string>

using namespace std;

class DataProcessor {
private:
    map<string, vector<int>> data_map;
public:
    void insertData(const string& key, const vector<int>& values) {
        data_map[key] = values;
    }
    
    int computeAggregate(const string& key) {
        int sum = 0;
        if (data_map.find(key) != data_map.end()) {
            for (int val : data_map[key]) {
                sum += val * val;
            }
        }
        return static_cast<int>(sqrt(sum));
    }
};

int main() {
    // Initialize variables
    int x = 15;
    int y = 27;
    int z = 9;
    
    // Bitwise and arithmetic operations
    int a = (x << 2) & (y >> 1);
    int b = (z ^ a) + 0x1F;
    
    // Conditional logic with short-circuit evaluation
    int c = 0;
    if ((a > 10) && (b < 100 || (x & 1))) {
        c = a * b;
    } else {
        c = a + b;
    }
    
    // String manipulation
    string s1 = "Hello";
    string s2 = "World";
    string s3 = s1 + s2;
    int d = static_cast<int>(s3.length()) ^ (c & 0xFF);
    
    // Nested data structure operations
    vector<vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int e = 0;
    for (size_t i = 0; i < matrix.size(); ++i) {
        for (size_t j = 0; j < matrix[i].size(); ++j) {
            if ((i + j) % 2 == 0) {
                e += matrix[i][j] << (i + j);
            }
        }
    }
    
    // Object-oriented computation
    DataProcessor processor;
    vector<int> data = {a, b, c, d, e};
    processor.insertData("key1", data);
    int f = processor.computeAggregate("key1");
    
    // Final calculation
    int result = ((f ^ 0xAA) * 3) % 256;
    
    cout << "Result: " << result << endl;
    return 0;
}