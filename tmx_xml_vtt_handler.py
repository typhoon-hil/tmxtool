import xml.etree.ElementTree as ET
import xml.dom.minidom

import re


def _format_time(time_string):
    # patter: don't care if it has a dot or comma, just split all numbers
    # universally, then connect them with dots
    number_pattern = "([0-9]{2}:[0-9]{2}:[0-9]{2})[,.]([0-9]{3})"
    number_pattern += ' --> ' + number_pattern
    result = re.split(number_pattern, time_string)
    # -- Remove blanks
    result = [res for res in result if len(res) != 0]
    return result[0] + "." + result[1] + " --> " + result[2] + "." + result[3]


def create_xml_from_dicts(src_dict, src_lang, tr_dict, tr_lang):
    # -- Create root
    root = ET.Element('tmx')
    root.set('version', "1.4")

    # -- Configure file header
    # TODO: This could be specified in a .conf file or
    #  some-such and then created from that file
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
    # -- Before returning, remove the first line of the string
    tempstring = xml.dom.minidom.parseString(dom).toprettyxml()
    # tempstring = tempstring.split('\n', 1)[1]
    return tempstring


def create_vtt_from_tmx(path_to_tmx, target_language):
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
