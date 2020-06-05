import unittest
import os
import shutil
from itertools import chain
from rename_case import RenameCase
from rename_case import RenameCaseHelpers


class RenameCaseTestCase(unittest.TestCase):
    TEST_CASE = 'SW140915-01A'
    OTHER_CASE = 'SQ200101-01A'
    OUT_CASE = 'TC131342-01A'
    TEST_DIR = './test_files/'
    TEST_SUBFILE = 'SW140915-01A_2_01.tif'
    TEST_NOCASE = 'skip_me.tif'
    TEST_OTHERCASE = 'SQ200101-01A_2_01.tif'
    TEST_OUTCASE = 'TC131342-01A_2_01.tif'

    @classmethod
    def setUp(cls):
        for d in [cls.work_dir(), cls.case_dir()]:
            os.mkdir(d)
            for f in [cls.TEST_SUBFILE, cls.TEST_NOCASE, cls.TEST_OTHERCASE]: # don't make outcase!
                open(os.path.join(d, f), 'a').close()

    @classmethod
    def tearDown(cls):
        shutil.rmtree(cls.work_dir())

    @classmethod
    def work_dir(cls):
        return os.path.abspath(cls.TEST_DIR)

    @classmethod
    def case_dir(cls):
        return os.path.join(cls.work_dir(), cls.TEST_CASE)

    @classmethod
    def nocase_bases(cls):
        return [cls.TEST_OUTCASE, cls.TEST_OTHERCASE, cls.TEST_NOCASE]

    @classmethod
    def case_files(cls):
        return cls._subfiles(cls.TEST_SUBFILE)

    @classmethod
    def case_root(cls):
        return os.path.join(cls.work_dir(), cls.TEST_SUBFILE)

    @classmethod
    def case_subcase(cls):
        return os.path.join(cls.case_dir(), cls.TEST_SUBFILE)

    @classmethod
    def nocase_root(cls):
        return os.path.join(cls.work_dir(), cls.TEST_NOCASE)

    @classmethod
    def nocase_subcase(cls):
        return os.path.join(cls.case_dir(), cls.TEST_NOCASE)

    @classmethod
    def othercase_root(cls):
        return os.path.join(cls.work_dir(), cls.TEST_OTHERCASE)

    @classmethod
    def othercase_subcase(cls):
        return os.path.join(cls.case_dir(), cls.TEST_OTHERCASE)

    @classmethod
    def outcase_root(cls):
        return os.path.join(cls.work_dir(), cls.TEST_OUTCASE)

    @classmethod
    def outcase_subcase(cls):
        return os.path.join(cls.case_dir(), cls.TEST_OUTCASE)

    @classmethod
    def _subfiles(cls, basefn):
        return [os.path.join(d, basefn) for d in [cls.work_dir(), cls.case_dir()]]

    def test_testing(self):
        self.assertEqual(True, True)

    def test_is_case_in_path(self):
        for p in self.case_files():
            self.assertTrue(RenameCase.is_case_in_path(p, self.TEST_CASE))
        for p in self.nocase_bases():
            self.assertTrue(RenameCase.is_case_in_path(os.path.join(self.case_dir(), p)))
            self.assertFalse(RenameCase.is_case_in_path(os.path.join(self.work_dir(), p)))

    def test_find_files_with_case(self):
        expected = list(set(self.case_files() + [os.path.join(self.case_dir(), bn) for bn in self.nocase_bases()]))
        self.assertListEqual(expected, RenameCase.find_files_with_case(self.work_dir(), self.TEST_CASE))

    def test_replace_case(self):
        self.assertEqual(self.outcase_root(), RenameCase.replace_case(self.case_root(), self.TEST_CASE, self.OUT_CASE))

    def test_rename_file(self):
        RenameCase.rename_file(self.case_root(), self.outcase_root())
        self.assertTrue(os.path.isfile(self.outcase_root()))




if __name__ == '__main__':
    unittest.main()
