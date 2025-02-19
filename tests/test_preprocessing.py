import unittest
from src.utils.preprocessing import clean_data, transform_data

class TestPreprocessing(unittest.TestCase):

    def test_clean_data(self):
        # Test case for cleaning data
        raw_data = {
            'Country': ['A', 'B', None, 'D'],
            'GDP': [1000, 2000, 3000, None]
        }
        cleaned_data = clean_data(raw_data)
        self.assertEqual(len(cleaned_data), 2)  # Expecting 2 rows after cleaning

    def test_transform_data(self):
        # Test case for transforming data
        raw_data = {
            'Country': ['A', 'B'],
            'GDP': [1000, 2000]
        }
        transformed_data = transform_data(raw_data)
        self.assertIn('GDP_transformed', transformed_data.columns)  # Check if transformation occurred

if __name__ == '__main__':
    unittest.main()