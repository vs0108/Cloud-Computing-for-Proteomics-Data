import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = "C://Users//acer//OneDrive//Desktop//Bnmit//Projects & Assignments//Cloud Computing Protemics//food.csv"

df = pd.read_csv(file_path)

# Set a Seaborn style
sns.set(style="whitegrid")

# 1. Enhanced Bar Plot of Nutrient Data Bank Number vs Carbohydrate Content
plt.figure(figsize=(12, 8))
bar_plot = sns.barplot(x='Nutrient Data Bank Number', y='Data.Carbohydrate', data=df, palette='viridis', hue='Nutrient Data Bank Number', dodge=False)
bar_plot.legend_.remove()  # Remove the legend
plt.title('Carbohydrate Content by Nutrient Data Bank Number', fontsize=16)
plt.xlabel('Nutrient Data Bank Number', fontsize=14)
plt.ylabel('Carbohydrate Content (g)', fontsize=14)
plt.xticks(rotation=90)
plt.grid(True, linestyle='--', linewidth=0.5)
# Add value labels
for p in bar_plot.patches:
    bar_plot.annotate(format(p.get_height(), '.2f'),
                      (p.get_x() + p.get_width() / 2., p.get_height()),
                      ha = 'center', va = 'center',
                      xytext = (0, 9),
                      textcoords = 'offset points')
plt.show()

# 2. Enhanced Histogram of Cholesterol Content
plt.figure(figsize=(12, 8))
sns.histplot(df['Data.Cholesterol'], bins=30, kde=True, color='skyblue')
plt.title('Histogram of Cholesterol Content', fontsize=16)
plt.xlabel('Cholesterol Content (mg)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.show()

# 3. Enhanced Scatter Plot of Potassium vs Sodium
plt.figure(figsize=(12, 8))
scatter_plot = sns.scatterplot(x='Data.Major Minerals.Potassium', y='Data.Major Minerals.Sodium', hue='Category', data=df, palette='deep', s=100, alpha=0.7)
plt.title('Scatter Plot of Potassium vs Sodium', fontsize=16)
plt.xlabel('Potassium (mg)', fontsize=14)
plt.ylabel('Sodium (mg)', fontsize=14)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.show()
