import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(filepath):
    return pd.read_csv(filepath, encoding='ISO-8859-1', low_memory=False)

def analyze_customer_cohorts(data):
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    data['CohortMonth'] = data.groupby('CustomerID')['InvoiceDate'].transform('min').dt.to_period('M')
    data['CohortIndex'] = (data['InvoiceDate'].dt.to_period('M') - data['CohortMonth']).apply(lambda x: x.n)
    
    cohort_data = data.groupby(['CohortMonth', 'CohortIndex']).agg({
        'CustomerID': 'nunique',
        'Quantity': 'sum'
    }).reset_index()
    
    cohort_pivot = cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='CustomerID')
    cohort_size = cohort_pivot.iloc[:, 0]
    retention = cohort_pivot.divide(cohort_size, axis=0)
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(retention, annot=True, fmt='.0%', cmap='Blues')
    plt.title('Customer Retention by Cohort')
    plt.xlabel('Months since First Purchase')
    plt.ylabel('Cohort Month')
    plt.show()
