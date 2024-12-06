import unittest
from unittest.mock import MagicMock, patch
from solution import scrap_animals, save_to_csv


class TestTasks(unittest.TestCase):
    @patch('solution.driver')
    def test_scrap_animals_success(self, mock_driver):
        mock_driver.find_elements.return_value = [
            MagicMock(text="Лев\nТигр\nВолк"),
        ]

        beasts_set = set()
        result = scrap_animals(beasts_set)

        self.assertEqual(len(result), 3)
        self.assertIn('Лев', result)
        self.assertIn('Тигр', result)

    def test_save_to_csv_empty_data(self):
        test_data = {}

        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            save_to_csv(test_data)

            mock_file.assert_called_once_with('beasts.csv', 'w', newline='')

            mock_file().write.assert_not_called()


if __name__ == '__main__':
    unittest.main()
