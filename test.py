import unittest
from filesystem import Link, fileList, current_dir


class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.mkdir = Link("dir", "root/", True).__dict__
        self.touch = Link("file", "root/").__dict__
        self.fileList = fileList
        self.current_dir = current_dir

    # Create directory, check that object is a directory. #
    def test_mkdir(self):
        self.assertEqual(self.mkdir["is_directory"], True)

    # Create file, check that object is not a directory #
    def test_touch(self):
        self.assertFalse(self.touch["is_directory"], False)

    # Check that fileList exists and is empty by default#
    def test_fl(self):
        self.assertEqual(len(self.fileList), 0)

    # Check that current_dir is initialized as "root/" #
    def test_cd(self):
        self.assertTrue(current_dir, "root/")


if __name__ == '__main__':
    unittest.main()
