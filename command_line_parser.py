
import CONSTANTS as constants
import help_script
import srt_line_extraction
from error_manager import run_error


def parse_command_line_args(command_line_args):
    if len(command_line_args) < constants.COMMAND_LINE_MIN_ARGS:
        run_error(constants.ERR_CODE_COMMAND_LINE_ARGS)

    command_name = command_line_args[
        constants.COMMAND_LINE_COMMAND_NAME_POSITION]

    # -- Figure out the command
    if command_name == constants.COMMAND_NAME_HELP:
        help_script.print_usage_and_switches()
    elif command_name == constants.COMMAND_NAME_CREATE_TMX:
        srt_line_extraction.line_extractor_full(command_line_args[2:])

    else:
        run_error(constants.ERR_CODE_COMMAND_LINE_ARGS)
