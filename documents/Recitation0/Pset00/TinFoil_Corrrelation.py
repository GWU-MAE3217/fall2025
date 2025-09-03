import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load data
df = pd.read_csv('boat_data.csv')

# Scatter plot
plt.figure(figsize=(8,6))
plt.scatter(df['Number of Pennies'], df['Boat Volume'], alpha=0.7)
plt.title('Number of Pennies vs Boat Volume')
plt.xlabel('Number of Pennies')
plt.ylabel('Boat Volume <cm^3>')
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate Pearson correlation
correlation, p_value = pearsonr(df['Number of Pennies'], df['Boat Volume'])
print('Correlation Coefficient:', correlation)
print('P-value:', p_value)
