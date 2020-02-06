
import CONSTANTS as constants
import help_script
import srt_processor
import tmx_processor
from error_manager import run_error

import re

from tmx_xml_vtt_handler import create_vtt_from_tmx


def sandbox(arguments):
    """
    Dev method for trying out methods.
    """
    print("sandbox")
    check_string = "00:12:44,412 --> 00:12:47,334"
    number_pattern = "([0-9]{2}:[0-9]{2}:[0-9]{2}),([0-9]{3})"
    pattern = number_pattern + " --> " + number_pattern
    # p = re.compile(pattern)
    # m = p.match(check_string)
    # print(m)
    x = re.split(pattern, check_string)
    create_vtt_from_tmx(r"C:\REPOS\tmxtool\supporting_documents\
    1.0 Video Introduction-01.tmx", 'de')


def parse_command_line_args(command_line_args):
    """
    Main entry point from the main script.
    This is a middle man to send arguments to other, more deserving functions.

    Arguments:
        command_line_args: Arguments from the main methods command line
    """
    if len(command_line_args) < constants.COMMAND_LINE_MIN_ARGS:
        run_error(constants.ERR_CODE_COMMAND_LINE_ARGS)

    command_name = command_line_args[
        constants.COMMAND_LINE_COMMAND_NAME_POSITION]

    # -- Figure out the command
    if command_name == constants.COMMAND_NAME_HELP:
        help_script.print_usage_and_switches()
    elif command_name == constants.COMMAND_NAME_CREATE_TMX:
        srt_processor.process_srt(command_line_args[2:])
    elif command_name == constants.COMMAND_NAME_CREATE_VTT:
        tmx_processor.process_tmx_file(command_line_args[2:])
    elif command_name == constants.COMMAND_NAME_DEV:
        sandbox(command_line_args[2:])
    else:
        run_error(constants.ERR_CODE_COMMAND_LINE_ARGS)
