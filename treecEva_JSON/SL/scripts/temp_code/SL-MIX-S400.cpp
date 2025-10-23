#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

class CharFrequency {
public:
    char character;
    int frequency;
    std::string code;
    
    CharFrequency(char c, int f) : character(c), frequency(f) {}
    
    bool operator<(const CharFrequency& other) const {
        return frequency > other.frequency; // For max-heap behavior
    }
};

class CompressionSystem {
private:
    std::vector<CharFrequency> frequencies;
    std::map<char, std::string> encodingMap;
    
public:
    void addCharacter(char c, int freq) {
        frequencies.emplace_back(c, freq);
    }
    
    void generateCodes() {
        std::sort(frequencies.begin(), frequencies.end());
        
        // Simple greedy assignment: more frequent = shorter code
        for (size_t i = 0; i < frequencies.size(); ++i) {
            frequencies[i].code = std::string(i+1, '1'); // Assign codes of increasing length
            encodingMap[frequencies[i].character] = frequencies[i].code;
        }
    }
    
    int calculateEncodedLength(const std::string& input) {
        int totalLength = 0;
        for (char c : input) {
            if (encodingMap.find(c) != encodingMap.end()) {
                totalLength += encodingMap[c].length();
            }
        }
        return totalLength;
    }
};

int main() {
    CompressionSystem compressor;
    
    // Add character frequencies
    compressor.addCharacter('a', 45);
    compressor.addCharacter('b', 13);
    compressor.addCharacter('c', 12);
    compressor.addCharacter('d', 16);
    compressor.addCharacter('e', 9);
    compressor.addCharacter('f', 5);
    
    compressor.generateCodes();
    
    std::string inputText = "abcdef";
    int encodedLength = compressor.calculateEncodedLength(inputText);
    
    std::cout << "Result: " << encodedLength << std::endl;
    return 0;
}