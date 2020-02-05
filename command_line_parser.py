
import CONSTANTS as constants
from error_manager import run_error


def parse_command_line_args(command_line_args):
    if len(command_line_args) < constants.COMMAND_LINE_MIN_ARGS:
        run_error(constants.ERR_CODE_COMMAND_LINE_ARGS)

