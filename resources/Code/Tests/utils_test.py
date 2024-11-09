import os
import unittest
import utils

class UtilsTest(unittest.TestCase):
    def test_get_dir_path(self):
        data_path = utils.get_dir_path(utils.WorkDirectory.Data)
        print(f"Data path: {data_path}")
        self.assertEqual(data_path, os.path.abspath('../Code/Data'), f'Test result {data_path} is incorrect')

if __name__ == '__main__':
    unittest.main()