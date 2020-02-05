from scripts.ce.pysynch import print_error

from error_manager import ERR_CODE_NON_EXISTING_DIRECTORY, \
    WARNING_CODE_NO_PAIR_FOUND, WARNING_CODE_INVALID_FORMAT, \
    run_warning, run_error, ERR_CODE_NON_EXISTING_FILE, \
    ERR_CODE_CREATING_XML
from tmx_xml_creator import create_xml_from_dicts


import printing_utilities as pu
import time
import os


def get_file_content_safe(path):
    try:
        with open(path) as file:
            # -- process everything for file 1
            lines = file.readlines()
    except FileNotFoundError as e:
        run_error(ERR_CODE_NON_EXISTING_FILE, path)
    return lines


def create_dicts(lines):
    ret = {}

    idx = 0
    while idx < len(lines):
        if lines[idx].strip() == '':
            idx += 1
            continue

        id = lines[idx].strip()
        idx += 1

        timestamp = lines[idx].strip()
        idx += 1

        content = ""
        while len(lines) > idx and lines[idx].strip() != '':
            content += lines[idx]
            idx += 1

        if id.strip() == '' or timestamp.strip() == '' or content.strip() == '':
            run_warning(WARNING_CODE_INVALID_FORMAT, [id, timestamp, content])
            continue

        ret[timestamp] = (id, content)
        idx += 1

    return ret


def line_extractor_dir(directory_path, src_lang):
    src_lang = src_lang.lower()
    if not os.path.exists(directory_path):
        print_error(ERR_CODE_NON_EXISTING_DIRECTORY, directory_path)

    files_to_translate = {}
    # -- filename - {source-file, source-lang, trans-file, trans-lang}

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
        if not ('path1' in v and
                'lang1' in v and
                'path2' in v and
                'lang2' in v):
            run_warning(WARNING_CODE_NO_PAIR_FOUND, k)
            continue
        path1 = v['path1']
        lang1 = v['lang1']
        path2 = v['path2']
        lang2 = v['lang2']
        line_extractor_full(path1, lang1, path2, lang2, k + ".tmx")


def line_extractor_full(path1, lang1, path2, lang2, result_name=None):
    # -- Creates a file in output directory based on result_name, 
    # -- or generates a timestamp as the name if None provided
    # -- Pull system arguments and create vars
    dict_1 = {}
    lines_1 = []

    dict_2 = {}
    lines_2 = []

    # -- Check both files existence and read all content
    pu.display_message('#1 Searching for files and '
                       'scanning all lines in files ...')
    lines_1 = get_file_content_safe(path1)
    lines_2 = get_file_content_safe(path2)
    pu.display_message('#1 ... Files found and all lines '
                       'in both files were read!\n')

    # -- Create dictionaries from all scanned lines in files
    pu.display_message('#2 Creating dictionaries from scanned lines ...')
    dict_1 = create_dicts(lines_1)
    dict_2 = create_dicts(lines_2)
    pu.display_message('#2 ... Created dictionaries from scanned lines!\n')

    # -- Create xml file
    # -- Create full filepath
    pu.display_message("#3 Generating tmx file ...")
    if result_name is None:
        xml_filename = str(time.time()) + '.tmx'
    else:
        xml_filename = result_name
    xml_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'output')
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
