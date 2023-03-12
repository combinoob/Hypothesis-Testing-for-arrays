import numpy as np
from scipy.stats import chi2
import math

# Input parameters
m, n = map(int, input("Enter m and n separated by space: ").split())

# Initialize observed frequency array for chi^2 test
obs_freq_chi2 = np.zeros(2)

# Initialize count variables for normal test
count_M = 0
count_W = 0

# Loop over each row
for i in range(m):
    # Get row input
    row = input(f"Enter row {i+1}: ").split()
    
    # Update observed frequency array for chi^2 test
    obs_freq_chi2[0] += row.count('M')
    obs_freq_chi2[1] += row.count('W')
    
    # Update count variables for normal test
    count_M += row.count('M')
    count_W += row.count('W')

# Calculate expected frequency array for chi^2 test
exp_freq_chi2 = np.array([n/2, n/2])

# Calculate Chi-squared test statistic
chi2_stat = np.sum((obs_freq_chi2 - exp_freq_chi2)**2 / exp_freq_chi2)

# Calculate critical value from Chi-squared distribution
crit_val_chi2 = chi2.ppf(0.95, df=1)

# Calculate total count and proportions for normal test
total_count = count_M + count_W
p_expected = 0.5
p_observed = count_M / total_count
standard_error = math.sqrt(p_expected*(1-p_expected)/total_count)
z_score = (p_observed - p_expected) / standard_error

# Compare Chi-squared test statistic to critical value
if chi2_stat > crit_val_chi2:
    print("chi^2: The observed distribution is not random.")
else:
    print("chi^2: The observed distribution is random.")

# Compare z-score to critical value for normal test
if abs(z_score) >= 1.96:
    print("normal: The observed distribution is not random.")
else:
    print("normal: The observed distribution is random.")
