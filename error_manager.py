import printing_utilities as pu

ERR_CODE_NON_EXISTING_FILE = 404
ERR_CODE_CREATING_XML = 406
ERR_CODE_COMMAND_LINE_ARGS = 407
ERR_CODE_NON_EXISTING_DIRECTORY = 408

WARNING_CODE_INVALID_FORMAT = 405
WARNING_CODE_NO_PAIR_FOUND = 406


def run_error(err_code, err_content=None, exception=None):
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
        pu.display_message("> Usage: tmxtool.py [source-file-path] "
                           "[source-language] [translation-file-path] "
                           "[translation-language]")
        pu.display_message("> Example:")
        pu.display_message(">> tmxtool.py C:\\Documents\\src-en.txt en "
                           "C:\\Documents\\src-de.txt de")
        exit(ERR_CODE_COMMAND_LINE_ARGS)


def run_warning(warn_code, warn_content, exception=None):
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
