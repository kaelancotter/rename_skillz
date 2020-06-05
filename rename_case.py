import re
import glob
import os
import shutil
import argparse


class RenameCase:
    CASE_RE = re.compile('[a-zA-Z]{2}[0-9]{6}-[0-9]{2}[A-Z]')  #this is a regular expression, we'll discuss

    @staticmethod
    def is_case_in_path(path, case):
        '''
        This tests a provided path and returns True or False if the case if found
        :param path: path to evaluate (string)
        :param case: case to search for (string)
        :return: True or False depending on search results
        '''
        #TODO
        return False

    @staticmethod
    def find_files_with_case(parent_folder, case):
        '''
        :param parent_folder: the path we want to search in
        :param case: the case we want to look for in any file in parent folder
        :return: a list of files that have case in the name
        '''
        # HINT!! We have a helper function that gets a list of all the files in a given path
        # HINT!! it can be called like: RenameCaseHelpers.files_in_path(parent_folder)
        # this should be used with the below is_case_in_path function
        # TODO
        return []


    @staticmethod
    def replace_case(path, old_case, new_case):
        '''
        Rename a file with old_case to one with new_case in the filename
        :param path: path with old_case as part of the filename
        :param old_case: case to change from
        :param new_case: case to change to
        :return: new path where old_case has been replaced with new_case
        '''
        #TODO
        return path

    @staticmethod
    def rename_file(src, dst, create_folders=False):
        '''
        :param src: the original path to the file
        :param dst: the new name for the file
        :param create_folders: if true - create missing parent folders in output file path (extra credit!!!)
        :return: None
        '''
        # TODO
        # HINT!! both os and shutil have functions for renaming files - move and rename are synonymous
        # https://docs.python.org/3/library/os.html
        # https://docs.python.org/3.7/library/shutil.html
        return None


class RenameCaseHelpers:

    @staticmethod
    def files_in_path(parent_folder):
        '''
        This helper function will list all full file paths within a provided parent folder
        :param parent_folder: folder to list contents of
        :return: a list of all file paths within a parent folder
        '''

        def yiter_files(top):
            for dirpath, dirnames, filenames in os.walk(top):
                for fn in filenames:
                    yield os.path.join(dirpath, fn)
        start = os.path.abspath(parent_folder)
        return list(yiter_files(start))

    @staticmethod
    def is_valid_case(case):
        '''
        This is another helper function that will validate a given case string
        :param case: case string to test
        :return: True/False for validity as a Case identifier
        '''
        return bool(re.search(RenameCase.CASE_RE, case))


def run():
    parser = argparse.ArgumentParser(description="Rename files with an old case ID to a new case ID")
    parser.add_argument('old_case', help="Old case ID to rename with new case")
    parser.add_argument('new_case', help='New case ID to use in renamed output')
    parser.add_argument('parent_dir', help='Directory to start at for files to rename')
    parser.add_argument('--create-dirs', '-d', action='store_true', help="Create missing directories for output")
    args = parser.parse_args()
    for case in [args.old_case, args.new_case]:
        if not RenameCaseHelpers.is_valid_case(case):
            parser.error(f"{case} is not a valid case")
    if not os.path.isdir(args.parent_dir):
        parser.error(f"Cannot find directory: {args.parent_dir}")
    for src_path in RenameCase.find_files_with_case(args.parent_dir, args.old_case):
        dst_path = RenameCase.replace_case(src_path, args.old_case, args.new_case)
        RenameCase.rename_file(src_path, dst_path, create_folders=args.create_dirs)


if __name__ == '__main__':
    run()