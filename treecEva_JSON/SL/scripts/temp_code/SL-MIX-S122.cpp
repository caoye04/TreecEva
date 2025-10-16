#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

constexpr int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

class SignalProcessor {
private:
    std::vector<int> heap;
    
    void heapifyUp(int index) {
        while (index > 0) {
            int parent = (index - 1) / 2;
            if (heap[index] <= heap[parent]) break;
            std::swap(heap[index], heap[parent]);
            index = parent;
        }
    }
    
    void heapifyDown(int index) {
        int size = heap.size();
        while (true) {
            int largest = index;
            int left = 2 * index + 1;
            int right = 2 * index + 2;
            
            if (left < size && heap[left] > heap[largest])
                largest = left;
            if (right < size && heap[right] > heap[largest])
                largest = right;
            
            if (largest == index) break;
            std::swap(heap[index], heap[largest]);
            index = largest;
        }
    }

public:
    void insert(int signal_strength) {
        heap.push_back(signal_strength);
        heapifyUp(heap.size() - 1);
    }
    
    int extractMax() {
        if (heap.empty()) return 0;
        int max_val = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        if (!heap.empty()) heapifyDown(0);
        return max_val;
    }
    
    bool empty() const {
        return heap.empty();
    }
    
    int size() const {
        return heap.size();
    }
};

int main() {
    SignalProcessor processor;
    
    // Test signal strengths
    std::vector<int> signals = {48, 18, 24, 12, 36, 9, 27, 15};
    
    // Insert all signals
    for (int signal : signals) {
        processor.insert(signal);
    }
    
    std::vector<int> processed_signals;
    
    // Process signals in priority order
    while (!processor.empty()) {
        int signal = processor.extractMax();
        processed_signals.push_back(signal);
    }
    
    // Calculate synchronization index using GCD of all processed signals
    int synchronization_index = processed_signals[0];
    for (size_t i = 1; i < processed_signals.size(); ++i) {
        synchronization_index = gcd(synchronization_index, processed_signals[i]);
        if (synchronization_index == 1) break; // Early termination optimization
    }
    
    std::cout << "Result: " << synchronization_index << std::endl;
    return 0;
}