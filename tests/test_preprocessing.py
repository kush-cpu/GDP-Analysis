import unittest
import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils.preprocessing import load_data, clean_data

class TestPreprocessing(unittest.TestCase):
    def setUp(self):
        # Create test data
        self.test_data = {
            'Country': ['USA', 'UK', 'France'],
            'GDP': ['$20,000', '$15,000', '$18,000'],
            'Growth': ['2.5%', '1.8%', '2.1%']
        }
        self.test_df = pd.DataFrame(self.test_data)

    def test_load_data_csv(self):
        # Create a test CSV file
        self.test_df.to_csv('test.csv', index=False)
        
        # Test loading
        loaded_df = load_data('test.csv', 'csv')
        self.assertIsNotNone(loaded_df)
        self.assertEqual(len(loaded_df), 3)
        
        # Cleanup
        os.remove('test.csv')

    def test_clean_data(self):
        # Test data cleaning
        cleaned_df = clean_data(self.test_df)
        
        self.assertIsNotNone(cleaned_df)
        self.assertTrue(pd.api.types.is_numeric_dtype(cleaned_df['GDP']))
        self.assertEqual(cleaned_df['GDP'].iloc[0], 20000.0)
        
        # Test mean calculation
        self.assertIsInstance(cleaned_df['GDP'].mean(), float)

if __name__ == '__main__':
    unittest.main()