import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = "data/dataset.csv"
df = pd.read_csv(file_path)

print("===== Dataset Preview =====")
print(df.head())

print("\n===== Dataset Info =====")
print(df.info())

print("\n===== Missing Values =====")
print(df.isnull().sum())

numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

if len(numeric_columns) == 0:
    print("\nNo numeric columns found for analysis.")
    exit()

selected_column = numeric_columns[0]
average_value = df[selected_column].mean()

print(f"\n===== Average of {selected_column} =====")
print(f"Average: {average_value:.2f}")

os.makedirs("output", exist_ok=True)

plt.figure(figsize=(10, 6))
df[selected_column].value_counts().head(10).plot(kind="bar")
plt.title(f"Bar Chart of Top 10 Values in {selected_column}")
plt.xlabel(selected_column)
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output/bar_chart.png")
plt.show()

if len(numeric_columns) >= 2:
    col1 = numeric_columns[0]
    col2 = numeric_columns[1]

    plt.figure(figsize=(10, 6))
    plt.scatter(df[col1], df[col2], alpha=0.6)
    plt.title(f"Scatter Plot: {col1} vs {col2}")
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.tight_layout()
    plt.savefig("output/scatter_plot.png")
    plt.show()
else:
    print("\nNot enough numeric columns for scatter plot.")

plt.figure(figsize=(10, 6))
correlation_matrix = df[numeric_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("output/heatmap.png")
plt.show()

print("\n===== Insights =====")
print(f"1. The average of '{selected_column}' is {average_value:.2f}")

if len(numeric_columns) >= 2:
    strongest_corr = correlation_matrix.unstack().sort_values(ascending=False)
    strongest_corr = strongest_corr[strongest_corr < 1].head(1)
    print(f"2. Strongest correlation found: {strongest_corr.index[0]} = {strongest_corr.values[0]:.2f}")

print("3. Heatmap helps identify which columns have strong positive/negative relationships.")
print("4. Scatter plot shows distribution and relationship between two numeric columns.")
print("5. Bar chart shows frequency distribution of top values.")
