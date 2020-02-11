import os

import utilities.printing_utilities as pu
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
    pu.display_message('#1 Processing items for directory: [' + directory + ']')
    for path in os.listdir(directory):
        full_path = os.path.join(directory, path)
        _process_single_file(full_path, language)
    pu.display_message('Processed everything in directory: [' + directory + ']')
    return file_handler.get_output_directory()


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
    pu.display_message('#1 Checking file format ...')
    input_filename = file_path.rsplit(os.path.sep, 1)[-1]
    if not input_filename.endswith('.tmx'):
        run_warning(WARNING_NOT_A_TMX_FILE, file_path)
        return
    pu.display_message("#1 ... file format valid!")

    # -- Get vtt file content
    pu.display_message("#2 Getting .vtt content ...")
    vtt_content = tmx_xml_vtt_handler.create_vtt_from_tmx(file_path, language)
    pu.display_message('#2 ... got all .vtt content!')

    # -- Get output directory
    pu.display_message('#3 Configuring file paths for outputs ...')
    output_directory = file_handler.get_output_directory()
    # -- Get only the filepath
    input_filename = file_path.rsplit(os.path.sep, 1)[-1]
    output_filename = os.path.split(input_filename)[1][:-4] + ".vtt"
    full_output_path = os.path.join(output_directory, output_filename)
    pu.display_message('#3 ... created all output paths: [' +
                       output_filename + ', ' + full_output_path + '] !')
    # -- Write to file
    pu.display_message('#4 Writing to output file ['
                       + full_output_path + '] ...')
    with open(full_output_path, mode='w') as file:
        file.write(vtt_content)
    pu.display_message('#4 ... all items written to output file!')
    return full_output_path


def process_tmx_file(arguments):
    """
    Processes tmx file so that all <tuv> items with the attribute the same as
    the supplied language. Creates a .vtt file.

    Arguments:
        arguments: In the form of 'path language'.

    Returns:
        None
    """
    pu.display_message('#1 Checking arguments ...')
    if arguments is None or len(arguments) not in VTT_MIN_ARGS:
        run_error(ERR_CODE_COMMAND_LINE_ARGS)
    pu.display_message('#1 ... Arguments valid!')

    # -- Extract arguments and check validity
    path = arguments[0]
    language = arguments[1]

    pu.display_message('#2 Checking if path is valid ...')
    if not os.path.exists(path):
        run_error(ERR_CODE_NON_EXISTING_W_E)
    pu.display_message('#2 ... path valid!')

    # -- Check if its a directory or not
    if os.path.isdir(path):
        return _process_directory_of_files(path, language)
    else:
        return _process_single_file(path, language)
