#define _USE_MATH_DEFINES
#include <iostream>
#include <map>
#include <regex>
#include <string>
#include <vector>

struct NucleotideNode {
    char nucleotide;
    int frequency;
    NucleotideNode* left;
    NucleotideNode* right;
    
    NucleotideNode(char n, int f) : nucleotide(n), frequency(f), left(nullptr), right(nullptr) {}
};

class DNATreeProcessor {
private:
    NucleotideNode* root;
    std::map<char, int> nucleotideCounts;
    
public:
    DNATreeProcessor() : root(nullptr) {}
    
    constexpr static int computeMutationScore(int original, int modifier) {
        return (original * 3 + modifier * 2) % 7;
    }
    
    void buildSampleTree() {
        // Creating a sample binary tree representing DNA sequence
        //       A(5)
        //      /    \
        //    C(3)   G(7)
        //   /  \      \
        // T(2) A(4)   T(6)
        
        root = new NucleotideNode('A', 5);
        root->left = new NucleotideNode('C', 3);
        root->right = new NucleotideNode('G', 7);
        root->left->left = new NucleotideNode('T', 2);
        root->left->right = new NucleotideNode('A', 4);
        root->right->right = new NucleotideNode('T', 6);
    }
    
    void processNucleotides(NucleotideNode* node) {
        if (!node) return;
        
        // Process current node
        std::string nodeData = std::string(1, node->nucleotide) + std::to_string(node->frequency);
        std::regex validPattern("^[ACGT][1-9][0-9]*$");
        
        if (std::regex_match(nodeData, validPattern)) {
            // Apply mutation scoring
            int score = computeMutationScore(node->frequency, 
                          nucleotideCounts[node->nucleotide]);
            nucleotideCounts[node->nucleotide] += score;
        }
        
        // Recursive processing
        processNucleotides(node->left);
        processNucleotides(node->right);
    }
    
    int calculateChecksum() {
        int checksum = 0;
        for (const auto& pair : nucleotideCounts) {
            checksum += static_cast<int>(pair.first) * pair.second;
        }
        return checksum;
    }
    
    int executeProcessingPipeline() {
        // Initialize counts
        nucleotideCounts = {{'A', 1}, {'C', 2}, {'G', 3}, {'T', 4}};
        
        // Build and process tree
        buildSampleTree();
        processNucleotides(root);
        
        // Calculate final checksum
        return calculateChecksum();
    }
    
    ~DNATreeProcessor() {
        // Simple cleanup (in real application, would need proper tree deletion)
        // For this problem, we only care about the computation
    }
};

int main() {
    DNATreeProcessor processor;
    int checksum = processor.executeProcessingPipeline();
    std::cout << "Result: " << checksum << std::endl;
    return 0;
}