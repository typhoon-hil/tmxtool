import os
import sys

from CONSTANTS import ERR_CODE_NON_EXISTING_FILE
from utilities.error_manager import run_error


def get_file_content_safe(path):
    """
    Checks if the file on location 'path' exists, and if it does it returns
    each line of text in the file as a list of strings. If not, the function
    runs an ERR_CODE_NON_EXISTING_FILE error.

    Arguments:
        path: path to file

    Returns:
        List of lines of text read from the specified file path.
    """
    try:
        with open(path) as file:
            # -- process everything for file 1
            lines = file.readlines()
    except FileNotFoundError:
        run_error(ERR_CODE_NON_EXISTING_FILE, path)
    return lines


def get_output_directory():
    """
    Checks if the default output directory exists. If it does not exist, it is
    created first, then returned. (created as script_location/output/)
    """
    output_directory_path = os.path.join(
        # os.path.dirname(os.path.abspath(__file__)), "output")
        os.path.dirname(os.path.abspath(sys.argv[0])), "output"
    )
    if not os.path.exists(output_directory_path):
        os.mkdir(output_directory_path)
    return output_directory_path


def get_output_file_name(file_name):
    """
    Connects the supplied 'file_name' with the default output directory.

    Arguments:
        file_name: the file name that is to be connected to the default
        output directory

    Returns:
        Absolute path to a file named like the supplied file name.
    """
    return os.path.join(get_output_directory(), file_name)
