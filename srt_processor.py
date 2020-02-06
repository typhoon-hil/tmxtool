from CONSTANTS import ERR_CODE_COMMAND_LINE_ARGS, ERR_CODE_NON_EXISTING_FILE, \
    WARNING_CODE_INVALID_FORMAT, ERR_CODE_NON_EXISTING_DIRECTORY, \
    WARNING_CODE_NO_PAIR_FOUND, ERR_CODE_CREATING_XML
from error_manager import run_warning, run_error
from file_handler import get_file_content_safe, get_output_directory, \
    get_output_file_name
from tmx_xml_vtt_handler import create_tmx_from_dicts


import printing_utilities as pu
import time
import os


def _create_dict(lines):
    """
    Creates formatted dictionaries for processing and creating .tmx files.
    The form of the dictionary is {timestamp: (paragraph_id, text), ...}

    Arguments:
        lines: lines of text from a .srt file

    Returns:
        Dictionary that is formatted for processing and creating .tmx files.
    """
    ret = {}

    idx = 0
    # -- Idx specifies one line to process
    while idx < len(lines):
        # -- Skip any blank lines
        if lines[idx].strip() == '':
            idx += 1
            continue

        # -- Get the id of this line
        # -- The id is just the number from a .srt file paragraph
        local_id = lines[idx].strip()
        idx += 1

        # -- Get the timestamp from the paragraph
        timestamp = lines[idx].strip()
        idx += 1

        # -- Fetch all content until the first empty line
        content = ""
        while len(lines) > idx and lines[idx].strip() != '':
            content += lines[idx]
            idx += 1

        # -- If anything that was parsed is actually blank, toss it and
        # inform the user of the warning
        if local_id.strip() == '' or timestamp.strip() == '' or \
                content.strip() == '':
            run_warning(WARNING_CODE_INVALID_FORMAT,
                        [local_id, timestamp, content])
            continue

        # -- Add the (id, content) pair on the key of the timestamp because
        # it is the only thing that is actually unique
        ret[timestamp] = (local_id, content)
        idx += 1

    return ret


def _process_srt_by_dir(directory_path, src_lang):
    """
    Essentially processes .srt files in the same way as _full_srt_process, but
    takes an entire directory as the input. Files are taken as pairs, so that
    pairs have the same name except the postfix of the filename (not the
    extension). The postfix of exactly one of the pairs must be the same as the
    src_lang parameter eg. filename-one-EN.srt, filename-one-DE.srt, for a
    src_lang parameter of either EN or DE.

    Arguments:
        directory_path: The directory from which to pull .srt file pairs
        src_lang: The language of the source file, and also the postfix of
        exactly one of the file pairs

    Returns:
        None
    """
    if not os.path.exists(directory_path):
        run_error(ERR_CODE_NON_EXISTING_DIRECTORY, directory_path)

    # -- Transform the src_lang to lower at once so that no problems are caused
    # later due to casing
    src_lang = src_lang.lower()

    # -- Filename - {source-file, source-lang, trans-file, trans-lang}
    files_to_translate = {}

    # -- Create {"path1":"path1", lang1:"lang1",
    # "path2":"path2", "lang2":"lang2"} dicts for
    # each unique filename with it's trailing
    # language sliced off.
    for item in os.listdir(directory_path):
        filename = item.split(".srt")[0][:-3]
        if filename not in files_to_translate:
            files_to_translate[filename] = {}

        t = {}
        file_lang = item.split(".srt")[0][-2:].lower()
        if file_lang == src_lang:
            path_key = 'path1'
            lang_key = 'lang1'
        else:
            path_key = 'path2'
            lang_key = 'lang2'
        t[path_key] = os.path.join(directory_path, item)
        t[lang_key] = file_lang

        files_to_translate[filename].update(t)

    for k, v in files_to_translate.items():
        # Check if any files or paths are found by themselves, and raise a
        # warning
        if not ('path1' in v and
                'lang1' in v and
                'path2' in v and
                'lang2' in v):
            run_warning(WARNING_CODE_NO_PAIR_FOUND, k)
            continue
        # -- If all is well, forward items to the _full_srt_process function
        # with predetermined filename
        path1 = v['path1']
        lang1 = v['lang1']
        path2 = v['path2']
        lang2 = v['lang2']
        _full_srt_process(path1, lang1, path2, lang2, str(k) + ".tmx")


def process_srt(arguments):
    """
    Processes arguments for creating tmx files.

    Arguments:
        arguments: arguments from the command line which must have either 4 or
        2 args. The arguments can be seen in the help_script section of the
        project.
    """
    if arguments is None or (len(arguments) != 4 and len(arguments) != 2):
        run_error(ERR_CODE_COMMAND_LINE_ARGS)

    if len(arguments) == 4:
        _full_srt_process(arguments[0],
                          arguments[1],
                          arguments[2],
                          arguments[3])
    else:
        _process_srt_by_dir(arguments[0], arguments[1])


def _full_srt_process(path1, lang1, path2, lang2, result_name=None):
    """
    Creates a .tmx file based on .srt files specified by parh1, and path2,
    taking into account the languages specified by lang1 and lang2.

    Arguments:
        path1: path to the source .srt file
        lang1: language of the source .srt file
        path2: path to the translation .srt file
        lang2: language of the translation .srt file
        result_name: (optional) name of the resulting .tmx file. If left blank
        the name will be generated based on the current time

    Returns:
        None
    """
    # -- Check both files existence and read all content
    pu.display_message('#1 Searching for files and '
                       'scanning all lines in files ...')
    lines_1 = get_file_content_safe(path1)
    lines_2 = get_file_content_safe(path2)
    pu.display_message('#1 ... Files found and all lines '
                       'in both files were read!\n')

    # -- Create dictionaries from all scanned lines in files
    pu.display_message('#2 Creating dictionaries from scanned lines ...')
    dict_1 = _create_dict(lines_1)
    dict_2 = _create_dict(lines_2)
    pu.display_message('#2 ... Created dictionaries from scanned lines!\n')

    # -- Create xml file
    # -- Create full filepath
    pu.display_message("#3 Generating tmx file ...")
    if result_name is None:
        xml_filename = str(time.time()) + '.tmx'
    else:
        xml_filename = result_name
    full_file_path = get_output_file_name(xml_filename)
    pu.display_message("File will be generated in: [" + full_file_path + "]")
    # -- Create root
    xml_string = create_tmx_from_dicts(dict_1, lang1, dict_2, lang2)
    try:
        with open(full_file_path, mode='w') as result_file:
            result_file.write(xml_string)
    except Exception as e:
        run_error(ERR_CODE_CREATING_XML, full_file_path, e)
    pu.display_message("#3 ... File " + full_file_path + " generated!\n")
