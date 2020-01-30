import os
import printing_utilities as pu
import sys
import time

from error_manager import run_error, ERR_CODE_NON_EXISTING_FILE, ERR_CODE_CREATING_XML, ERR_CODE_COMMAND_LINE_ARGS
from srt_line_extraction import create_dicts
from tmx_xml_creator import create_xml_from_dicts


def get_file_content_safe(path):
    try:
        with open(path) as file:
            # -- process everything for file 1
            lines = file.readlines()
    except FileNotFoundError as e:
        run_error(ERR_CODE_NON_EXISTING_FILE, path)
    return lines


if __name__ == '__main__':
    if len(sys.argv) != 5:
        run_error(ERR_CODE_COMMAND_LINE_ARGS)

    pu.display_message('--------------------------------------------------\n'
                       'NOTICE: Script was written with the assumption\n'
                       'that both .srt files selected are written in a way\n'
                       'that is familiar to the converter.'
                       '\n------------------------------------------------')

    # -- Pull system arguments and create vars
    path1 = sys.argv[1]
    lang1 = sys.argv[2]

    path2 = sys.argv[3]
    lang2 = sys.argv[4]

    dict_1 = {}
    lines_1 = []

    dict_2 = {}
    lines_2 = []

    # -- Check both files existence and read all content
    pu.display_message('#1 Searching for files and scanning all lines in files ...')
    lines_1 = get_file_content_safe(path1)
    lines_2 = get_file_content_safe(path2)
    pu.display_message('#1 ... Files found and all lines in both files were read!\n')

    # -- Create dictionaries from all scanned lines in files
    pu.display_message('#2 Creating dictionaries from scanned lines ...')
    dict_1 = create_dicts(lines_1)
    dict_2 = create_dicts(lines_2)
    pu.display_message('#2 ... Created dictionaries from scanned lines!\n')

    # -- Create xml file
    # -- Create full filepath
    pu.display_message("#3 Generating tmx file ...")
    xml_filename = str(time.time()) + '.tmx'
    xml_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
    full_file_path = os.path.join(xml_directory, xml_filename)
    pu.display_message("File will be generated in: [" + full_file_path + "]")
    # -- Create root
    xml_string = create_xml_from_dicts(dict_1, lang1, dict_2, lang2)
    try:
        if not os.path.exists(xml_directory):
            os.mkdir(xml_directory)
        with open(full_file_path, mode='w') as result_file:
            result_file.write(xml_string)
    except Exception as e:
        run_error(ERR_CODE_CREATING_XML, full_file_path, e)
    pu.display_message("#3 ... File " + full_file_path + " generated!\n")

    # -- Buffer for possible cleanup operations
    pu.display_message("#4 Cleaning up ...")
    pu.display_message("#4 ... Cleaned up!\n")
    pu.display_message("END tmxtool")
