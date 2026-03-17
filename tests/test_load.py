import pandas as pd
import unittest
from unittest.mock import patch
from utils.load import load_to_csv, load_to_postgres, load_to_gsheets

class TestLoad(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({'Title': ['A'], 'Price': [1000]})

    @patch("pandas.DataFrame.to_csv")
    def test_load_to_csv(self, mock_to_csv):
        load_to_csv(self.df, "test.csv")
        mock_to_csv.assert_called_once_with("test.csv", index=False)

    @patch("utils.load.create_engine")
    @patch("pandas.DataFrame.to_sql")
    def test_load_to_postgres(self, mock_to_sql, mock_create_engine):
        load_to_postgres(self.df, "sqlite:///:memory:", "test_table")
        mock_create_engine.assert_called_once()
        mock_to_sql.assert_called_once()

if __name__ == "__main__":
    unittest.main()