#define _USE_MATH_DEFINES
#include <iostream>
#include <unordered_map>
#include <vector>
#include <cmath>

class SensorReading {
public:
    int value;
    SensorReading() : value(0) {}
    SensorReading(int v) : value(v) {}
    SensorReading operator+(const SensorReading& other) const {
        return SensorReading(this->value + other.value);
    }
    constexpr bool operator<(const SensorReading& other) const {
        return this->value < other.value;
    }
};

constexpr long long polynomial_hash(const char* str, int len) {
    long long hash = 0;
    constexpr long long base = 31;
    constexpr long long mod = 1000000007;
    for (int i = 0; i < len; ++i) {
        hash = (hash * base + str[i]) % mod;
    }
    return hash;
}

struct HashNode {
    SensorReading data;
    HashNode* next;
    HashNode(SensorReading d) : data(d), next(nullptr) {}
};

int main() {
    std::unordered_map<long long, HashNode*> telemetry_table;
    std::vector<SensorReading> raw_readings = {SensorReading(15), SensorReading(23), SensorReading(9)};
    
    // Encoding phase with string hashing
    const char* identifiers[] = {"temp_a", "press_b", "flow_c"};
    int aggregated_checksum = 0;
    
    for (size_t i = 0; i < raw_readings.size(); ++i) {
        long long hash_key = polynomial_hash(identifiers[i], 6);
        HashNode* node = new HashNode(raw_readings[i]);
        
        if (telemetry_table.find(hash_key) == telemetry_table.end()) {
            telemetry_table[hash_key] = node;
        } else {
            HashNode* current = telemetry_table[hash_key];
            while (current->next != nullptr) {
                current = current->next;
            }
            current->next = node;
        }
    }
    
    // Processing phase with nested loops and early termination
    for (const auto& entry : telemetry_table) {
        HashNode* current = entry.second;
        while (current != nullptr) {
            for (int j = 1; j <= 3; ++j) {
                if (j > current->data.value) break;
                current->data = current->data + SensorReading(j * 2);
                if (current->data.value > 50) {
                    aggregated_checksum += current->data.value;
                    goto next_entry;
                }
            }
            aggregated_checksum += current->data.value;
            next_entry:
            current = current->next;
        }
    }
    
    std::cout << "Result: " << aggregated_checksum << std::endl;
    return 0;
}