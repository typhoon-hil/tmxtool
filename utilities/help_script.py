from utilities import printing_utilities as pu


def print_usage_and_switches():
    """
    Prints the help text for the user.

    Arguments:
        None

    Returns:
        None
    """
    pu.display_message(" < Typhoon HIL Tmx Tool >")
    pu.display_message(" > Usage:")
    pu.display_message(" > pyton tmxtool.py (command-name) "
                       "(command-parameters)")
    pu.display_message("====================================================="
                       "===")
    pu.display_message(" > Command names and their parameters: ")
    pu.display_message("")
    pu.display_message(" >\t\tcommand-name          = '-help'")
    pu.display_message(" >\t\tcommand-parameters    = None")
    pu.display_message(" >\t\tdescription: Displays the usage of this script.")
    pu.display_message("")
    pu.display_message(" >\t\tcommand-name          = '-mktmx'")
    pu.display_message(" >\t\tcommand-parameters    = (1) 'path-to-source-file"
                       ".srt source-file-language path-to-translation-file.srt "
                       "translation-file-language'")
    pu.display_message(" >\t\t                      = (2) 'path-to-directory "
                       "source-language'")
    pu.display_message(" >\t\tdescription: (1) Creates .tmx file based on "
                       "provided .srt files and their languages. Tmx file is "
                       "saved as a timestamp, and the directory where it is "
                       "saved will be displayed once script is finished.")
    pu.display_message(" >\t\t             (2) Creates .tmx files using file "
                       "pairs from the specified directory using the specified"
                       " language as the source language. The directory must"
                       " contain file pairs - files named the same except for"
                       " the last 3 characters, which must be in the form of "
                       "'-XY' where XY is the language code eg. EN, DE ...")
    pu.display_message("")
    pu.display_message(" >\t\tcommand-name          = '-mkvtt'")
    pu.display_message(" >\t\tcommand-parameters    = (1) 'path-to-tmx-file "
                       "language-for-processing'")
    pu.display_message(" >\t\t                      = (2) 'path-to-directory "
                       "language-for-processing'")
    pu.display_message(" >\t\tdescription: (1) Creates a .vtt file based on "
                       "the provided path to the tmx file, extracting all "
                       "items tied to the language provided.")
    pu.display_message(" >\t\t             (2) Does (1) but for all .tmx "
                       "files in the directory from the provided directory.")
