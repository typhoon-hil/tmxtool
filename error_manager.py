import printing_utilities as pu
from CONSTANTS import ERR_CODE_NON_EXISTING_DIRECTORY, \
    ERR_CODE_NON_EXISTING_FILE, ERR_CODE_CREATING_XML, \
    ERR_CODE_COMMAND_LINE_ARGS, WARNING_CODE_INVALID_FORMAT, \
    WARNING_CODE_NO_PAIR_FOUND, ERR_CODE_NON_EXISTING_W_E


def run_error(err_code, err_content=None, exception=None):
    """
    Prints an error for the user and exists out of the program

    Arguments:
        err_code: Indicates which error happened. Can be used from CONSTANTS.
        err_content: Something custom to print in the console.
        exception: Optional exception that can be shown to the user.

    Returns:
        None
    """
    if err_code == ERR_CODE_NON_EXISTING_DIRECTORY:
        pu.display_message('Error: The directory you provided was not found ['
                           + err_content + ']. Script exited.')
        exit(ERR_CODE_NON_EXISTING_DIRECTORY)
    if err_code == ERR_CODE_NON_EXISTING_FILE:
        pu.display_message('Error: The file you provided was not found ['
                           + err_content + ']. Script exited.')
        exit(ERR_CODE_NON_EXISTING_FILE)
    if err_code == ERR_CODE_CREATING_XML:
        pu.display_message('Error: unable to create file ' + err_content +
                           '. The reason for this is currently unknown to '
                           'the system and must be analyzed by hand.')
        pu.display_message('Concrete exception:')
        pu.display_message(exception)
        exit(ERR_CODE_CREATING_XML)
    if err_code == ERR_CODE_COMMAND_LINE_ARGS:
        pu.display_message("Invalid number of command arguments.")
        pu.display_message("> Usage: tmxtool.py (command-name) "
                           "[command-params]")
        pu.display_message("> Type: 'tmxtool.py -help' for more information.")
        exit(ERR_CODE_COMMAND_LINE_ARGS)
    if err_code == ERR_CODE_NON_EXISTING_W_E:
        pu.display_message("Invalid path. Try another path and make sure it "
                           "exists and is written correctly.")
        exit(ERR_CODE_NON_EXISTING_W_E)


def run_warning(warn_code, warn_content, exception=None):
    """
    Prints a warning for the user and returns the warning code. Does not exit
    out of the program.

    Arguments:
        warn_code: Code for the warning message. Can be found in CONSTANTS.
        warn_content: Custom content to show the user.
        exception: Exception to show to the user.
    """
    if warn_code == WARNING_CODE_INVALID_FORMAT:
        pu.display_message('Warning: invalid content format found:')
        pu.display_message('|---ID: [' + warn_content[0] + ']')
        pu.display_message('|---Timestamp: [' + warn_content[1] + ']')
        pu.display_message('|---Content: [' + warn_content[2] + ']')
        pu.display_message('Continuing file conversion ...')
        return WARNING_CODE_INVALID_FORMAT
    if warn_code == WARNING_CODE_NO_PAIR_FOUND:
        pu.display_message('Warning: no pair found for [' + warn_content + ']')
        return WARNING_CODE_NO_PAIR_FOUND
