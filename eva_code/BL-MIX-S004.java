import java.util.*;

class ConsensusNode {
    int nodeId;
    int proposedValue;
    Map<Integer, Integer> receivedProposals;
    Set<Integer> byzantineNodes;
    boolean isLeader;
    int round;
    int agreedValue;
    boolean hasAgreed;
    
    public ConsensusNode(int id, int value) {
        this.nodeId = id;
        this.proposedValue = value;
        this.receivedProposals = new HashMap<>();
        this.byzantineNodes = new HashSet<>();
        this.isLeader = false;
        this.round = 0;
        this.agreedValue = -1;
        this.hasAgreed = false;
    }
}

class DistributedConsensus {
    List<ConsensusNode> nodes;
    int totalNodes;
    int byzantineFaultTolerance;
    int currentLeader;
    int agreedValue;
    boolean consensusReached;
    int maxRounds;
    
    public DistributedConsensus(int[] proposals) {
        this.totalNodes = proposals.length;
        this.byzantineFaultTolerance = (totalNodes - 1) / 3;
        this.nodes = new ArrayList<>();
        this.currentLeader = 0;
        this.agreedValue = -1;
        this.consensusReached = false;
        this.maxRounds = 10;
        
        for (int i = 0; i < totalNodes; i++) {
            nodes.add(new ConsensusNode(i, proposals[i]));
        }
        nodes.get(currentLeader).isLeader = true;
    }
    
    public void simulateByzantineFailures() {
        if (totalNodes > 3) {
            nodes.get(totalNodes - 1).proposedValue = 999; // Byzantine behavior
            for (ConsensusNode node : nodes) {
                if (node.nodeId != totalNodes - 1) {
                    node.byzantineNodes.add(totalNodes - 1);
                }
            }
        }
    }
    
    public void exchangeProposals() {
        for (ConsensusNode sender : nodes) {
            if (sender.byzantineNodes.contains(sender.nodeId)) continue;
            
            for (ConsensusNode receiver : nodes) {
                if (receiver.nodeId == sender.nodeId) continue;
                if (receiver.byzantineNodes.contains(sender.nodeId)) continue;
                
                receiver.receivedProposals.put(sender.nodeId, sender.proposedValue);
            }
        }
    }
    
    public int calculateMajorityValue(ConsensusNode node) {
        Map<Integer, Integer> valueCount = new HashMap<>();
        
        // Count own proposal
        valueCount.put(node.proposedValue, valueCount.getOrDefault(node.proposedValue, 0) + 1);
        
        // Count received proposals (excluding byzantine nodes)
        for (Map.Entry<Integer, Integer> entry : node.receivedProposals.entrySet()) {
            if (!node.byzantineNodes.contains(entry.getKey())) {
                int value = entry.getValue();
                valueCount.put(value, valueCount.getOrDefault(value, 0) + 1);
            }
        }
        
        int maxCount = 0;
        int majorityValue = -1;
        int requiredMajority = (totalNodes - byzantineFaultTolerance) / 2 + 1;
        
        for (Map.Entry<Integer, Integer> entry : valueCount.entrySet()) {
            if (entry.getValue() > maxCount && entry.getValue() >= requiredMajority) {
                maxCount = entry.getValue();
                majorityValue = entry.getKey();
            }
        }
        
        return majorityValue;
    }
    
    public void performConsensusRound() {
        // Phase 1: Leader proposes value
        ConsensusNode leader = nodes.get(currentLeader);
        if (leader.byzantineNodes.contains(leader.nodeId)) {
            // Leader is byzantine, select new leader
            currentLeader = (currentLeader + 1) % totalNodes;
            while (nodes.get(currentLeader).byzantineNodes.contains(currentLeader)) {
                currentLeader = (currentLeader + 1) % totalNodes;
            }
            leader = nodes.get(currentLeader);
            leader.isLeader = true;
        }
        
        int proposedValue = leader.proposedValue;
        
        // Phase 2: All nodes exchange and vote
        exchangeProposals();
        
        int agreeCount = 0;
        int agreedValue = -1;
        
        for (ConsensusNode node : nodes) {
            if (node.byzantineNodes.contains(node.nodeId)) continue;
            
            int majorityValue = calculateMajorityValue(node);
            if (majorityValue != -1 && majorityValue == proposedValue) {
                node.hasAgreed = true;
                node.agreedValue = majorityValue;
                agreeCount++;
                agreedValue = majorityValue;
            } else {
                // Update proposal based on majority
                if (majorityValue != -1) {
                    node.proposedValue = majorityValue;
                }
            }
            node.round++;
        }
        
        // Phase 3: Check consensus
        int requiredAgreement = totalNodes - byzantineFaultTolerance;
        if (agreeCount >= requiredAgreement) {
            this.consensusReached = true;
            this.agreedValue = agreedValue;
        } else {
            // Rotate leader for next round
            currentLeader = (currentLeader + 1) % totalNodes;
            while (nodes.get(currentLeader).byzantineNodes.contains(currentLeader)) {
                currentLeader = (currentLeader + 1) % totalNodes;
            }
            
            // Reset agreements for next round
            for (ConsensusNode node : nodes) {
                node.hasAgreed = false;
                node.receivedProposals.clear();
            }
        }
    }
    
    public int runConsensus() {
        simulateByzantineFailures();
        
        int round = 0;
        while (!consensusReached && round < maxRounds) {
            performConsensusRound();
            round++;
        }
        
        return agreedValue;
    }
    
    public static void main(String[] args) {
        int[] proposals = {10, 15, 10, 20, 10};
        DistributedConsensus consensus = new DistributedConsensus(proposals);
        int result = consensus.runConsensus();
        System.out.println("Consensus agreed value: " + result);
    }
}