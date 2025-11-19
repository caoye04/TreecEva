import numpy as np

temperatures = np.array([18, 22, 19, 25, 17, 30, 16, 21, 23, 15])
warm_days = temperatures[temperatures > 20]
average_warm_temp = np.mean(warm_days)
print(f"Result: {average_warm_temp}")