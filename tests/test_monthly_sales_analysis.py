import unittest
import pandas as pd  # Asegúrate de importar pandas
from scripts.monthly_sales_analysis import load_data, preprocess_data, analyze_monthly_sales

class TestMonthlySalesAnalysis(unittest.TestCase):
    def setUp(self):
        self.data = load_data('data/preprocessed_data.csv')
        self.data = preprocess_data(self.data)

    def test_analyze_monthly_sales(self):
        result = analyze_monthly_sales(self.data)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.Series)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()
