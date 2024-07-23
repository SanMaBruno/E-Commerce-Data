import unittest
from scripts.customer_cohort_analysis import load_data, analyze_customer_cohorts

class TestCustomerCohortAnalysis(unittest.TestCase):

    def setUp(self):
        self.data = load_data('data/data.csv')

    def test_analyze_customer_cohorts(self):
        result = analyze_customer_cohorts(self.data)
        # Añade tus aserciones aquí

if __name__ == '__main__':
    unittest.main()
