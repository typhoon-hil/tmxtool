import os

from utilities import file_handler
from processors import tmx_xml_vtt_handler
from CONSTANTS import VTT_MIN_ARGS, ERR_CODE_COMMAND_LINE_ARGS, \
    ERR_CODE_NON_EXISTING_W_E, WARNING_NOT_A_TMX_FILE
from utilities.error_manager import run_error, run_warning


def _process_directory_of_files(directory, language):
    """
    Processes all files from a directory using _process_single_file.

    Arguments:
        directory: Directory from where to fetch files.
        language: The language in which to process the files.

    Returns:
        None
    """
    for path in os.listdir(directory):
        full_path = os.path.join(directory, path)
        _process_single_file(full_path, language)
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
    input_filename = file_path.rsplit(os.path.sep, 1)[-1]
    if not input_filename.endswith('.tmx'):
        run_warning(WARNING_NOT_A_TMX_FILE, file_path)
        return

    # -- Get vtt file content
    vtt_content = tmx_xml_vtt_handler.create_vtt_from_tmx(file_path, language)

    # -- Get output directory
    output_directory = file_handler.get_output_directory()
    # -- Get only the filepath
    input_filename = file_path.rsplit(os.path.sep, 1)[-1]
    output_filename = input_filename[:-4] + ".vtt"
    full_output_path = os.path.join(output_directory, output_filename)
    with open(full_output_path, mode='w') as file:
        file.write(vtt_content)


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
