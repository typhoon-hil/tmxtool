import os

from CONSTANTS import VTT_MIN_ARGS, ERR_CODE_COMMAND_LINE_ARGS, \
    ERR_CODE_NON_EXISTING_W_E
from error_manager import run_error


def _process_directory_of_files(directory, language):
    """
    Processes all files from a directory using _process_single_file.

    Arguments:
        directory: Directory from where to fetch files.
        language: The language in which to process the files.

    Returns:
        None
    """

    pass


def _process_single_file(file_path, language):
    """
    Processes only one file from file_path and takes all items marked with
    language. Creates a .vtt file.

    Arguments:
        file_path: Path of file to process.
        language: The language of the file to process.

    Returns:
        None
    """
    pass


def process_tmx_file(arguments):
    """
    Processes tmx file so that all <tuv> items with the attribute the same as
    the supplied language. Creates a .vtt file.

    Arguments:
        arguments: In the form of 'path language'.

    Returns:
        None
    """
    if arguments is None or len(arguments) not in VTT_MIN_ARGS:
        run_error(ERR_CODE_COMMAND_LINE_ARGS)

    # -- Extract arguments and check validity
    path = arguments[0]
    language = arguments[1]

    if not os.path.exists(path):
        run_error(ERR_CODE_NON_EXISTING_W_E)

    # -- Check if its a directory or not
    if os.path.isdir(path):
        _process_directory_of_files(path, language)
    else:
        _process_single_file(path, language)
