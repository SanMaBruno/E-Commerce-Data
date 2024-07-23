import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    return pd.read_csv(filepath, encoding='ISO-8859-1', low_memory=False)

def preprocess_data(data):
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    data['YearMonth'] = data['InvoiceDate'].dt.to_period('M')
    data['Quantity'] = pd.to_numeric(data['Quantity'], errors='coerce')
    data['TotalPrice'] = data['Quantity'] * data['UnitPrice']
    return data

def analyze_monthly_sales(data):
    monthly_sales = data.groupby('YearMonth').sum(numeric_only=True)['TotalPrice']
    plt.figure(figsize=(12, 6))
    sns.barplot(x=monthly_sales.index.astype(str), y=monthly_sales.values)
    plt.xticks(rotation=45)
    plt.title('Ventas Mensuales')
    plt.xlabel('Mes')
    plt.ylabel('Total Vendido')
    plt.show()
    return monthly_sales

def main():
    data = load_data('data/preprocessed_data.csv')
    data = preprocess_data(data)
    result = analyze_monthly_sales(data)
    return result

if __name__ == '__main__':
    main()
