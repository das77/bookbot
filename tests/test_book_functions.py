import unittest
import sys
import os
from unittest.mock import patch
# Add parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import main, gen_report, get_book, count_words, count_characters, dict_to_list_of_dicts, sort_on

class TestBookFunctions(unittest.TestCase):

    def test_gen_report(self):
        
        # Test gen_report function with sample inputs
        book = '/home/dspera/Projects/bookbot/books/frankenstein.txt'
        words = 1000
        chars = [{'a': 10}, {'b': 5}, {'c': 15}]
        expected_report = '--- Begin report of /home/dspera/Projects/bookbot/books/frankenstein.txt ---\n'
        expected_report += '1000 words found in the document\n'
        expected_report += 'The a character was found 10 times\n'
        expected_report += 'The b character was found 5 times\n'
        expected_report += 'The c character was found 15 times\n'
        expected_report += '--- End Report ---'
        
        actual_report = gen_report(book, words, chars)
        self.assertEqual(actual_report, expected_report)

    # Write more test cases for gen_report function as needed

    def test_main(self):
        # Test main function
        # Mock the necessary functions to return sample data
        book_loc = '/home/dspera/Projects/bookbot/books/frankenstein.txt'
        book_text = "This is a sample book text."
        num_words = 10
        num_chars = {'a': 5, 'b': 3, 'c': 2}
        char_list = [{'a': 5}, {'b': 3}, {'c': 2}]
        
        # Mock the necessary functions
        with patch('app.get_book') as mock_get_book, \
             patch('app.count_words') as mock_count_words, \
             patch('app.count_characters') as mock_count_characters, \
             patch('app.dict_to_list_of_dicts') as mock_dict_to_list_of_dicts, \
             patch('app.sort_on') as mock_sort_on, \
             patch('builtins.print') as mock_print:
            
            # Set the return values of mocked functions
            mock_get_book.return_value = book_text
            mock_count_words.return_value = num_words
            mock_count_characters.return_value = num_chars
            mock_dict_to_list_of_dicts.return_value = char_list
            
            # Call the main function
            main()
            
            # Check if print function was called with the expected report
            expected_report = gen_report(book_loc, num_words, char_list)
            mock_print.assert_called_with(expected_report)

    def test_get_book(self):
        # Test get_book function with a known file path
        file_contents = get_book("tests/test_book.txt")
        self.assertIsInstance(file_contents, str)

    def test_count_words(self):
        # Test count_words function with a known input
        word_count = count_words("This is a test book.")
        self.assertEqual(word_count, 5)

    def test_count_characters(self):
        # Test count_characters function with a known input
        char_counts = count_characters("This is a test book.")
        self.assertEqual(char_counts['t'], 3)

    def test_dict_to_list_of_dicts(self):
        # Test dict_to_list_of_dicts function with a known input
        input_dict = {'a': 1, 'b': 2, 'c': 3}
        list_of_dicts = dict_to_list_of_dicts(input_dict)
        self.assertEqual(len(list_of_dicts), len(input_dict))

    def test_sort_on(self):
        # Test sort_on function with a known input
        input_list = [{'a': 3}, {'b': 1}, {'c': 2}]
        sort_on(input_list)
        self.assertEqual(input_list, [{'a': 3}, {'c': 2}, {'b': 1}])

if __name__ == '__main__':
    unittest.main()
