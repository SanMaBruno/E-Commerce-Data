import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath, encoding='ISO-8859-1', low_memory=False)

def preprocess_data(data):
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    data['YearMonth'] = data['InvoiceDate'].dt.to_period('M')
    data['Quantity'] = pd.to_numeric(data['Quantity'], errors='coerce')
    data['UnitPrice'] = pd.to_numeric(data['UnitPrice'], errors='coerce')
    data['TotalPrice'] = data['Quantity'] * data['UnitPrice']

    # Filtrar valores atípicos
    data = data[(data['TotalPrice'] > 0) & (data['Quantity'] > 0)]

    return data

if __name__ == "__main__":
    data = load_data('data/data.csv')
    processed_data = preprocess_data(data)
    processed_data.to_csv('data/preprocessed_data.csv', index=False)
