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
    pu.display_message(" >\t\tcommand-name       = '-help'")
    pu.display_message(" >\t\tcommand-parameters = None")
    pu.display_message(" >\t\tdescription: Displays the usage of this script.")
