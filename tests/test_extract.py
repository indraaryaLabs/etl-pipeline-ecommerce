import unittest
from unittest.mock import patch, Mock
from utils.extract import extract_data

class TestExtract(unittest.TestCase):
    
    @patch("utils.extract.requests.get")
    def test_extract_data_success(self, mock_get):
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        
        # Simulasi elemen HTML dengan class yang BENAR sesuai website
        html_content = """
        <div class="collection-card">
            <h3 class="product-title">T-shirt 2</h3>
            <span class="price">$102.15</span>
            <p>Rating: ⭐ 3.9 / 5</p>
            <p>3 Colors</p>
            <p>Size: M</p>
            <p>Gender: Women</p>
        </div>
        """
        mock_response.text = html_content
        mock_get.return_value = mock_response

        # Jalankan fungsi
        result = extract_data("https://fashion-studio.dicoding.dev/", total_pages=1)
        
        # Validasi hasil
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["Title"], "T-shirt 2")
        self.assertEqual(result[0]["Price"], "$102.15")

    @patch("utils.extract.requests.get")
    def test_extract_data_failure(self, mock_get):
        # Setup mock untuk menghasilkan exception
        mock_get.side_effect = Exception("Connection Error")
        
        result = extract_data("https://fashion-studio.dicoding.dev/", total_pages=1)
        
        # Fungsi harus mengembalikan None saat terjadi error
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()