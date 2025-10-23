#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>

struct TelemetryNode {
    int temperature;
    TelemetryNode* next;
    
    TelemetryNode(int temp) : temperature(temp), next(nullptr) {}
};

class TelemetryBuffer {
private:
    TelemetryNode* head;
    
public:
    TelemetryBuffer() : head(nullptr) {}
    
    void addReading(int temp) {
        TelemetryNode* newNode = new TelemetryNode(temp);
        if (!head) {
            head = newNode;
        } else {
            TelemetryNode* current = head;
            while (current->next) {
                current = current->next;
            }
            current->next = newNode;
        }
    }
    
    int computeWeightedChecksum() {
        int runningTotal = 0;
        TelemetryNode* current = head;
        int position = 1;
        int selectedCount = 1;
        
        while (current != nullptr) {
            if (position % 3 == 1) {  // Every third reading starting from first (positions 1, 4, 7, ...)
                int contribution = static_cast<int>(std::pow(current->temperature, 2)) * selectedCount;
                runningTotal += contribution;
                
                if (runningTotal > 1000) {
                    break;  // Early return when threshold exceeded
                }
                
                selectedCount++;
            }
            
            position++;
            current = current->next;
        }
        
        return runningTotal;
    }
    
    ~TelemetryBuffer() {
        while (head) {
            TelemetryNode* temp = head;
            head = head->next;
            delete temp;
        }
    }
};

int main() {
    TelemetryBuffer buffer;
    
    // Satellite temperature readings
    buffer.addReading(5);   // Position 1 - Selected (5^2 * 1 = 25)
    buffer.addReading(12);  // Position 2 - Not selected
    buffer.addReading(8);   // Position 3 - Not selected
    buffer.addReading(7);   // Position 4 - Selected (7^2 * 2 = 98)
    buffer.addReading(3);   // Position 5 - Not selected
    buffer.addReading(11);  // Position 6 - Not selected
    buffer.addReading(9);   // Position 7 - Selected (9^2 * 3 = 243)
    buffer.addReading(6);   // Position 8 - Not selected
    buffer.addReading(14);  // Position 9 - Not selected
    buffer.addReading(4);   // Position 10 - Selected (4^2 * 4 = 64)
    buffer.addReading(10);  // Position 11 - Not selected
    buffer.addReading(2);   // Position 12 - Not selected
    buffer.addReading(13);  // Position 13 - Selected (13^2 * 5 = 845)
    
    int checksum = buffer.computeWeightedChecksum();
    std::cout << "Result: " << checksum << std::endl;
    
    return 0;
}