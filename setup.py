import unittest
import sys
import os

# Ajustar la ruta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

from customer_cohort_analysis import load_data, analyze_customer_cohorts

class TestCustomerCohortAnalysis(unittest.TestCase):

    def setUp(self):
        self.data = load_data('../data/data.csv')

    def test_analyze_customer_cohorts(self):
        try:
            analyze_customer_cohorts(self.data)
        except Exception as e:
            self.fail(f"analyze_customer_cohorts() raised {e}")

if __name__ == '__main__':
    unittest.main()
