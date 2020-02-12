import xml.etree.ElementTree as ET
import xml.dom.minidom

import re


def _format_time(time_string):
    """
    Takes the time string and replaces all commas with full stops.

    The time string can contain commas or full stops.
    Arguments:
        time_string: A string in the format "00:00:00,000 --> 00:00:00,000"

    Returns:
        The same as the time_string but with commas turned into full stops.
    """
    # pattern: don't care if it has a dot or comma, just split all numbers
    # universally, then connect them with dots
    number_pattern = "([0-9]{2}:[0-9]{2}:[0-9]{2})[,.]([0-9]{3})"
    number_pattern += ' --> ' + number_pattern
    result = re.split(number_pattern, time_string)
    # -- Remove blanks
    result = [res for res in result if len(res) != 0]
    return result[0] + "." + result[1] + " --> " + result[2] + "." + result[3]


def create_tmx_from_dicts(src_dict, src_lang, tr_dict, tr_lang):
    """
    Creates tmx file using the formatted dictionaries.

    Arguments:
        src_dict: Dictionary containing source .srt file items
        src_lang: Source .srt file language
        tr_dict: Dictionary containing translation .srt file items
        tr_lang: Translation .srt file language
    """
    # -- Create root
    root = ET.Element('tmx')
    root.set('version', "1.4")

    # -- Configure file header
    header = ET.SubElement(root, 'header')
    header.set('creationtool', 'tmxtool')
    header.set('creationtoolversion', '1.0.0')
    header.set('datatype', 'PlainText')
    header.set('segtype', 'phrase')
    header.set('adminlang', src_lang + '-' + tr_lang)
    header.set('srclang', src_lang)
    header.set('o-tmf', '.srt')

    # -- Configure file body
    body = ET.SubElement(root, 'body')

    for key in src_dict.keys():
        tu = ET.SubElement(body, 'tu')

        tuv_src = ET.SubElement(tu, 'tuv')
        tuv_src.set('xml:lang', src_lang)
        seg_src = ET.SubElement(tuv_src, 'seg')
        seg_src.text = '\n' + key + '\n' + src_dict[key][1] + '\n'

        tuv_tr = ET.SubElement(tu, 'tuv')
        tuv_tr.set('xml:lang', tr_lang)
        seg_tr = ET.SubElement(tuv_tr, 'seg')
        seg_tr.text = '\n' + key + '\n' + tr_dict[key][1] + '\n'

    dom = ET.tostring(root, encoding='unicode', method='xml')
    tempstring = xml.dom.minidom.parseString(dom).toprettyxml()
    # -- Before returning, remove the first line of the string
    # tempstring = tempstring.split('\n', 1)[1]
    return tempstring


def create_vtt_from_tmx(path_to_tmx, target_language):
    """
    Creates a .vtt document text to be saved in a .vtt file.

    Arguments:
        path_to_tmx: Path to the .tmx file to be processed.
        target_language: Language to filer out from the .tmx file.

    Returns:
        Text to be saved into a .vtt file.
    """
    # -- Gets the root of the file, and then parses for any <tuv> tags
    # -- When <tuv> tags are found, all children with the target_language
    # as the attribute are added to the list of items to process further
    tree = ET.parse(path_to_tmx)
    root = tree.getroot()
    text_items = []
    for child in root.iter('tuv'):
        if target_language in child.attrib.values():
            text_items.append(
                tuple([item for item in child[0].text.split('\n')
                       if len(item.strip()) != 0]))

    vtt_document_text = "WEBVTT\n"

    for item_tuple in text_items:
        # -- Get and process the time from the tuple
        # (it will always be on first place)
        time = _format_time(item_tuple[0])
        # -- Configure alignment text
        alignment_text = " align:middle line:" + \
                         ("84%" if len(item_tuple[1:]) > 1 else "90%") + "\n"
        # -- Configure rest of text
        rest_of_text = "\n".join([text.strip() for text in item_tuple[1:]])
        vtt_document_text += "\n" + time + alignment_text + rest_of_text + "\n"

    return vtt_document_text
