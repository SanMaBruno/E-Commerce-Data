import unittest
from scripts.price_quantity_correlation import load_data, analyze_price_quantity_correlation

class TestPriceQuantityCorrelation(unittest.TestCase):

    def setUp(self):
        self.data = load_data('data/preprocessed_data.csv')

    def test_analyze_price_quantity_correlation(self):
        self.assertTrue('TotalPrice' in self.data.columns)
        self.assertTrue('Quantity' in self.data.columns)
        # Aquí puedes agregar aserciones específicas para el análisis de correlación

if __name__ == '__main__':
    unittest.main()
