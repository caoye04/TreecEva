#include <iostream>
#include <vector>
#include <cmath>

class DataProcessor {
private:
    std::vector<int> data;
    int size;

public:
    DataProcessor(std::vector<int> input) : data(input), size(input.size()) {}
    
    int hash(int index) {
        return (index * 31) ^ (data[index % size] << 2);
    }
    
    int recursiveCompute(int n) {
        if (n <= 1) return n;
        return (n & 1) ? recursiveCompute(n-1) + recursiveCompute(n-2) : 
               recursiveCompute(n/2) * 2;
    }
    
    int process() {
        int accumulator = 0;
        for (int i = 0; i < size; ++i) {
            int hashed = hash(i);
            int masked = hashed & 0xFF;
            int shifted = masked >> 2;
            int computed = recursiveCompute(shifted);
            accumulator += (computed ^ data[i]) * (i + 1);
        }
        return accumulator;
    }
};

int main() {
    std::vector<int> values = {7, 14, 3, 21, 9, 15, 6, 18};
    DataProcessor processor(values);
    int intermediate = processor.process();
    int result = (intermediate % 1000) + (intermediate & 0x3FF) - (intermediate >> 10);
    return 0;
}