import java.util.*;
import java.util.stream.*;
import java.math.BigInteger;
import java.security.MessageDigest;

class DataPoint {
    private int id;
    private double value;
    private String category;
    private boolean active;
    
    public DataPoint(int id, double value, String category, boolean active) {
        this.id = id;
        this.value = value;
        this.category = category;
        this.active = active;
    }
    
    public int getId() { return id; }
    public double getValue() { return value; }
    public String getCategory() { return category; }
    public boolean isActive() { return active; }
    public void setValue(double value) { this.value = value; }
}

class DataProcessor {
    private List<DataPoint> dataPoints;
    private Map<String, Double> categoryWeights;
    private int[] transformationMatrix;
    private long finalResult;
    
    public DataProcessor() {
        this.dataPoints = new ArrayList<>();
        this.categoryWeights = new HashMap<>();
        this.transformationMatrix = new int[16];
        this.finalResult = 0L;
    }
    
    public void addDataPoint(DataPoint point) {
        dataPoints.add(point);
    }
    
    public void setCategoryWeight(String category, double weight) {
        categoryWeights.put(category, weight);
    }
    
    public long getFinalResult() { return finalResult; }
    
    public void processData() {
        // Initialize transformation matrix with Fibonacci-like sequence
        transformationMatrix[0] = 1;
        transformationMatrix[1] = 1;
        for (int i = 2; i < 16; i++) {
            transformationMatrix[i] = (transformationMatrix[i-1] + transformationMatrix[i-2]) % 1000;
        }
        
        // Stream operations for data filtering and transformation
        List<DataPoint> activePoints = dataPoints.stream()
            .filter(DataPoint::isActive)
            .filter(p -> p.getValue() > 0)
            .sorted(Comparator.comparing(DataPoint::getId))
            .collect(Collectors.toList());
        
        // Value transformations using category weights
        for (DataPoint point : activePoints) {
            String category = point.getCategory();
            double weight = categoryWeights.getOrDefault(category, 1.0);
            double transformedValue = point.getValue() * weight * Math.sin(point.getId() * Math.PI / 8);
            point.setValue(Math.round(transformedValue * 100.0) / 100.0);
        }
        
        // Grouping and aggregation
        Map<String, Double> categoryTotals = activePoints.stream()
            .collect(Collectors.groupingBy(
                DataPoint::getCategory,
                Collectors.summingDouble(DataPoint::getValue)
            ));
        
        // Hash calculation for string data
        StringBuilder categoryString = new StringBuilder();
        categoryTotals.keySet().stream().sorted().forEach(categoryString::append);
        
        int stringHash = 0;
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] hashBytes = md.digest(categoryString.toString().getBytes());
            stringHash = new BigInteger(1, hashBytes).intValue() & 0x7FFFFFFF;
        } catch (Exception e) {
            stringHash = categoryString.toString().hashCode() & 0x7FFFFFFF;
        }
        
        // Matrix operations with data points
        double[] dataVector = activePoints.stream()
            .mapToDouble(DataPoint::getValue)
            .limit(16)
            .toArray();
        
        // Pad or truncate to exactly 16 elements
        double[] paddedVector = new double[16];
        for (int i = 0; i < 16; i++) {
            paddedVector[i] = (i < dataVector.length) ? dataVector[i] : 0.0;
        }
        
        // Matrix-vector multiplication
        long matrixResult = 0;
        for (int i = 0; i < 16; i++) {
            matrixResult += (long)(paddedVector[i] * transformationMatrix[i]);
        }
        
        // Category analysis with bitwise operations
        int categoryFlags = 0;
        for (String category : categoryTotals.keySet()) {
            int categoryHash = category.hashCode() & 0xFF;
            categoryFlags ^= categoryHash;
            categoryFlags = (categoryFlags << 1) | (categoryFlags >>> 31);
        }
        
        // Statistical calculations
        OptionalDouble averageValue = activePoints.stream()
            .mapToDouble(DataPoint::getValue)
            .average();
        
        double stdDev = 0.0;
        if (averageValue.isPresent()) {
            double mean = averageValue.getAsDouble();
            stdDev = activePoints.stream()
                .mapToDouble(p -> Math.pow(p.getValue() - mean, 2))
                .average()
                .orElse(0.0);
            stdDev = Math.sqrt(stdDev);
        }
        
        // ID-based operations
        int idProduct = activePoints.stream()
            .mapToInt(DataPoint::getId)
            .reduce(1, (a, b) -> (a * b) % 10007);
        
        // Weighted sum calculation
        double weightedSum = 0.0;
        for (Map.Entry<String, Double> entry : categoryTotals.entrySet()) {
            double weight = categoryWeights.getOrDefault(entry.getKey(), 1.0);
            weightedSum += entry.getValue() * weight;
        }
        
        // Final result aggregation
        long tempResult = 0L;
        tempResult += (long)(weightedSum * 100);
        tempResult += (stringHash % 100000);
        tempResult += (matrixResult % 50000);
        tempResult += (categoryFlags & 0xFFFF);
        tempResult += (long)(stdDev * 1000) % 1000;
        tempResult += idProduct;
        tempResult += activePoints.size() * 777;
        
        // Apply transformation based on data characteristics
        if (activePoints.size() > 5) {
            tempResult = (tempResult * 3) / 2;
        }
        
        if (categoryTotals.size() > 2) {
            tempResult += 12345;
        }
        
        // Final modular arithmetic
        this.finalResult = tempResult % 999999;
    }
}

public class Main {
    public static void main(String[] args) {
        DataProcessor processor = new DataProcessor();
        
        // Initialize category weights
        processor.setCategoryWeight("A", 1.5);
        processor.setCategoryWeight("B", 2.0);
        processor.setCategoryWeight("C", 0.8);
        processor.setCategoryWeight("D", 1.2);
        
        // Add data points
        processor.addDataPoint(new DataPoint(1, 15.5, "A", true));
        processor.addDataPoint(new DataPoint(2, 23.8, "B", true));
        processor.addDataPoint(new DataPoint(3, 8.2, "C", false));
        processor.addDataPoint(new DataPoint(4, 31.7, "A", true));
        processor.addDataPoint(new DataPoint(5, 19.3, "D", true));
        processor.addDataPoint(new DataPoint(6, 42.1, "B", true));
        processor.addDataPoint(new DataPoint(7, 12.6, "C", true));
        processor.addDataPoint(new DataPoint(8, 27.9, "A", false));
        processor.addDataPoint(new DataPoint(9, 35.4, "D", true));
        processor.addDataPoint(new DataPoint(10, 18.7, "B", true));
        
        // Process data and compute final result
        processor.processData();
        
        System.out.println("Final result: " + processor.getFinalResult());
    }
}