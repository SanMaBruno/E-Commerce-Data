import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(filepath):
    return pd.read_csv(filepath, encoding='ISO-8859-1', low_memory=False)

def analyze_price_quantity_correlation(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='TotalPrice', y='Quantity', data=data)
    plt.title('Correlation between Total Price and Quantity')
    plt.xlabel('Total Price')
    plt.ylabel('Quantity')
    plt.show()

if __name__ == "__main__":
    data = load_data('data/preprocessed_data.csv')
    analyze_price_quantity_correlation(data)
