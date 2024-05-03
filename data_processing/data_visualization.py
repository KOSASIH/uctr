import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_data(df, target_column):
    # Plot histogram of target variable
    sns.histplot(df[target_column], kde=True)
    plt.title('Distribution of Target Variable')
    plt.show()

    # Plot correlation matrix
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

    # Plot pairplot
    sns.pairplot(df)
    plt.title('Pairplot of All Variables')
    plt.show()
