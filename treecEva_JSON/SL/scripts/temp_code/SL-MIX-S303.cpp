#define _USE_MATH_DEFINES
#include <iostream>
#include <memory>

class SecureChannel {
private:
    int verificationMask;
    mutable int processedPackets;

public:
    constexpr SecureChannel(int mask) : verificationMask(mask), processedPackets(0) {}
    
    constexpr int computeGCD(int a, int b) const {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    
    bool processPacket(int sequenceNumber, int& checksum) const {
        processedPackets++;
        if (sequenceNumber <= 0 || (sequenceNumber & 1) == 0) {
            return false;  // Invalid or even packet
        }
        
        checksum = computeGCD(sequenceNumber, verificationMask);
        return (checksum > 1) && ((sequenceNumber & verificationMask) != 0);
    }
    
    int getPacketsProcessed() const { return processedPackets; }
};

int main() {
    constexpr int initialMask = 45;
    const auto channel = std::make_unique<const SecureChannel>(initialMask);
    
    int packetSequences[] = {13, 22, 39, 15, 8, 27, 18, 33, 16, 25};
    int authenticationChecksum = 0;
    int validPacketCount = 0;
    
    for (int i = 0; i < 10; ++i) {
        int currentChecksum = 0;
        bool isValid = channel->processPacket(packetSequences[i], currentChecksum);
        
        if (isValid && (validPacketCount < 3 || (packetSequences[i] & 7) == 1)) {
            authenticationChecksum += currentChecksum;
            validPacketCount++;
        } else if (!isValid && currentChecksum > 0) {
            authenticationChecksum ^= currentChecksum;
        }
        
        if (validPacketCount >= 5) {
            break;
        }
    }
    
    std::cout << "Result: " << authenticationChecksum << std::endl;
    return 0;
}