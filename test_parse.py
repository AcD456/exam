import unittest
import xml.etree.ElementTree as ETree
from main import parse_person_data

class TestParsePersonData(unittest.TestCase):
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            parse_person_data("non_existing_file.xml")



if __name__ == "__main__":
    unittest.main()