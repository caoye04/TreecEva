#define _USE_MATH_DEFINES
#include <iostream>
#include <memory>
#include <vector>
#include <numeric>

class PrimeNode {
public:
    int value;
    std::shared_ptr<PrimeNode> next;
    PrimeNode(int val) : value(val), next(nullptr) {}
};

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    // Create linked list of first 5 primes: 2, 3, 5, 7, 11
    auto head = std::make_shared<PrimeNode>(2);
    head->next = std::make_shared<PrimeNode>(3);
    head->next->next = std::make_shared<PrimeNode>(5);
    head->next->next->next = std::make_shared<PrimeNode>(7);
    head->next->next->next->next = std::make_shared<PrimeNode>(11);
    
    int secure_token_value = 0;
    std::vector<int> processed_primes;
    
    auto current = head;
    while (current != nullptr) {
        int prime = current->value;
        processed_primes.push_back(prime);
        
        // For each new prime, compute GCD with all previous primes
        for (size_t i = 0; i < processed_primes.size() - 1; ++i) {
            secure_token_value += gcd(prime, processed_primes[i]);
        }
        
        current = current->next;
    }
    
    std::cout << "Result: " << secure_token_value << std::endl;
    return 0;
}