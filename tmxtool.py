import os
import printing_utilities as pu
import sys
import time

from error_manager import run_error, ERR_CODE_COMMAND_LINE_ARGS
from srt_line_extraction import line_extractor_dir, line_extractor_full 
from tmx_xml_creator import create_xml_from_dicts


if __name__ == '__main__':
    if len(sys.argv) != 5 and len(sys.argv) != 3:
        run_error(ERR_CODE_COMMAND_LINE_ARGS)

    pu.display_message('--------------------------------------------------\n'
                       'NOTICE: Script was written with the assumption\n'
                       'that both .srt files selected are written in a way\n'
                       'that is familiar to the converter.'
                       '\n------------------------------------------------')

    if len(sys.argv) == 5:
        path1 = sys.argv[1]
        lang1 = sys.argv[2]

        path2 = sys.argv[3]
        lang2 = sys.argv[4]

        line_extractor_full(path1, lang1, path2, lang2)

    if len(sys.argv) == 3:
        dir_path = sys.argv[1]
        src_lang = sys.argv[2]
        line_extractor_dir(dir_path, src_lang)

    # -- Buffer for possible cleanup operations
    pu.display_message("#4 Cleaning up ...")
    pu.display_message("#4 ... Cleaned up!\n")
    pu.display_message("END tmxtool")
